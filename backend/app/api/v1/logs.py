from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.ai.agent import analyze_security_events
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.incident import Incident
from app.models.log_batch import LogBatch
from app.models.user import User
from app.parsers.factory import auto_detect_parser, get_parser
from app.schemas.log_event import LogBatchResponse

router = APIRouter(prefix="/logs", tags=["Log Ingestion & Normalization"])


@router.post("/upload", response_model=LogBatchResponse, status_code=status.HTTP_201_CREATED)
async def upload_log_file(
    file: UploadFile = File(...),
    source_type: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Ingests a raw security log file, normalizes events, creates a LogBatch,
    and triggers automated AI threat correlation.
    """
    try:
        content_bytes = await file.read()
        raw_text = content_bytes.decode("utf-8", errors="replace")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to read uploaded file: {str(e)}",
        )

    # 1. Select appropriate parser
    if source_type and get_parser(source_type):
        parser = get_parser(source_type)
    else:
        parser = auto_detect_parser(file.filename, raw_text)

    # 2. Parse raw logs into NormalizedLogEvents
    events = parser.parse(raw_text)
    if not events:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unable to parse log format for file '{file.filename}'. Please verify file contents.",
        )

    # 3. Create LogBatch Record
    batch = LogBatch(
        filename=file.filename,
        source_type=parser.source_type,
        raw_count=len(events),
        status="PARSED",
        uploaded_by_id=current_user.id,
        uploaded_at=datetime.now(timezone.utc),
    )
    db.add(batch)
    db.commit()
    db.refresh(batch)

    # 4. Trigger AI & RAG Threat Analysis
    ai_result = analyze_security_events(events)
    if ai_result and ai_result.threat_detected:
        incident = Incident(
            batch_id=batch.id,
            title=ai_result.title,
            severity=ai_result.severity,
            risk_score=ai_result.risk_score,
            attack_category=ai_result.attack_category,
            mitre_technique_id=ai_result.mitre_technique_id,
            mitre_technique_name=ai_result.mitre_technique_name,
            source_ip=ai_result.source_ip,
            target_host=ai_result.target_host,
            confidence_score=ai_result.confidence_score,
            summary=ai_result.summary,
            technical_details=ai_result.technical_details,
            recommended_mitigation=ai_result.recommended_mitigation,
            status="OPEN",
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        db.add(incident)
        batch.status = "ANALYZED"
        db.commit()

    return batch


@router.get("/batches", response_model=List[LogBatchResponse])
def list_log_batches(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve historical log ingestion batches."""
    batches = db.query(LogBatch).order_by(LogBatch.uploaded_at.desc()).offset(skip).limit(limit).all()
    return batches
