from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.incident import Incident
from app.models.user import User
from app.services.pdf_generator import generate_incident_pdf

router = APIRouter(prefix="/reports", tags=["Incident Reporting & Compliance"])


@router.get("/incident/{incident_id}/pdf")
def export_incident_report_pdf(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Generate and stream an audit-ready, professional NIST SP 800-61 Incident Triage PDF.
    """
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incident #{incident_id} not found",
        )

    pdf_buffer = generate_incident_pdf(incident)
    filename = f"CyberSentinel_Incident_{incident.id}_NIST_Report.pdf"

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
            "Access-Control-Expose-Headers": "Content-Disposition",
        },
    )
