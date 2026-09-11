from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.incident import Incident
from app.models.user import User
from app.schemas.incident import IncidentResponse, IncidentStats, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["Incidents & Triage"])


@router.get("", response_model=List[IncidentResponse])
def list_incidents(
    severity: Optional[str] = Query(None, description="Filter by severity: CRITICAL, HIGH, MEDIUM, LOW"),
    status_filter: Optional[str] = Query(None, alias="status", description="Filter by status: OPEN, INVESTIGATING, CONTAINED, RESOLVED"),
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve security incidents with optional severity and status filters."""
    query = db.query(Incident)
    if severity:
        query = query.filter(Incident.severity == severity.upper())
    if status_filter:
        query = query.filter(Incident.status == status_filter.upper())
    return query.order_by(Incident.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/stats/summary", response_model=IncidentStats)
def get_incident_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Aggregated metrics for the SOC monitoring dashboard."""
    total = db.query(Incident).count()
    critical = db.query(Incident).filter(Incident.severity == "CRITICAL").count()
    high = db.query(Incident).filter(Incident.severity == "HIGH").count()
    medium = db.query(Incident).filter(Incident.severity == "MEDIUM").count()
    low = db.query(Incident).filter(Incident.severity == "LOW").count()

    open_inc = db.query(Incident).filter(Incident.status == "OPEN").count()
    investigating = db.query(Incident).filter(Incident.status == "INVESTIGATING").count()
    resolved = db.query(Incident).filter(Incident.status.in_(["CONTAINED", "RESOLVED"])).count()

    # Top MITRE techniques aggregation
    tech_counts = (
        db.query(Incident.mitre_technique_id, func.count(Incident.id))
        .filter(Incident.mitre_technique_id.isnot(None))
        .group_by(Incident.mitre_technique_id)
        .order_by(func.count(Incident.id).desc())
        .limit(5)
        .all()
    )
    top_techniques = [{k or "Other": v} for k, v in tech_counts]

    recent_alerts = db.query(Incident).order_by(Incident.created_at.desc()).limit(5).all()

    return IncidentStats(
        total_incidents=total,
        critical_count=critical,
        high_count=high,
        medium_count=medium,
        low_count=low,
        open_count=open_inc,
        investigating_count=investigating,
        resolved_count=resolved,
        top_techniques=top_techniques,
        recent_alerts=recent_alerts,
    )


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve detailed forensic profile of a specific incident."""
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incident #{incident_id} not found",
        )
    return incident


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident_status(
    incident_id: int,
    incident_update: IncidentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update status, severity, or remediation playbook for an ongoing incident."""
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incident #{incident_id} not found",
        )

    if incident_update.status:
        incident.status = incident_update.status.upper()
    if incident_update.severity:
        incident.severity = incident_update.severity.upper()
    if incident_update.recommended_mitigation:
        incident.recommended_mitigation = incident_update.recommended_mitigation

    db.commit()
    db.refresh(incident)
    return incident
