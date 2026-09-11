from contextlib import asynccontextmanager
from pathlib import Path
import logging
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.api.v1 import auth, chat, incidents, logs, reports
from app.core.config import settings
from app.core.security import get_password_hash
from app.db.session import Base, SessionLocal, engine, get_db
from app.models.incident import Incident
from app.models.user import User
from app.parsers.linux_parser import LinuxSyslogParser
from app.parsers.windows_parser import WindowsEventParser
from app.parsers.apache_parser import ApacheAccessLogParser
from app.ai.agent import analyze_security_events
from app.rag.vector_store import get_mitre_collection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cybersentinel")


def seed_initial_data(db: Session):
    """Seed default credentials and baseline demo incidents if database is fresh."""
    # 1. Seed Users
    if db.query(User).count() == 0:
        admin = User(
            username="admin",
            email="admin@cybersentinel.local",
            hashed_password=get_password_hash("admin123"),
            role="admin",
        )
        analyst = User(
            username="analyst",
            email="analyst@cybersentinel.local",
            hashed_password=get_password_hash("analyst123"),
            role="tier1_analyst",
        )
        db.add_all([admin, analyst])
        db.commit()
        logger.info("Default users seeded: admin/admin123, analyst/analyst123")

    # 2. Seed Baseline Incidents for Instant Demo
    if db.query(Incident).count() == 0:
        sample_dir = Path(__file__).resolve().parent.parent.parent / "sample_logs"
        
        # Ingest Linux SSH Attack
        linux_file = sample_dir / "linux_auth_ssh_attack.log"
        if linux_file.exists():
            events = LinuxSyslogParser().parse(linux_file.read_text())
            analysis = analyze_security_events(events)
            if analysis:
                inc1 = Incident(
                    title=analysis.title,
                    severity=analysis.severity,
                    risk_score=analysis.risk_score,
                    attack_category=analysis.attack_category,
                    mitre_technique_id=analysis.mitre_technique_id,
                    mitre_technique_name=analysis.mitre_technique_name,
                    source_ip=analysis.source_ip,
                    target_host=analysis.target_host,
                    confidence_score=analysis.confidence_score,
                    summary=analysis.summary,
                    technical_details=analysis.technical_details,
                    recommended_mitigation=analysis.recommended_mitigation,
                    status="OPEN",
                )
                db.add(inc1)

        # Ingest Apache Web Attack
        apache_file = sample_dir / "apache_web_attacks.log"
        if apache_file.exists():
            events = ApacheAccessLogParser().parse(apache_file.read_text())
            analysis = analyze_security_events(events)
            if analysis:
                inc2 = Incident(
                    title=analysis.title,
                    severity=analysis.severity,
                    risk_score=analysis.risk_score,
                    attack_category=analysis.attack_category,
                    mitre_technique_id=analysis.mitre_technique_id,
                    mitre_technique_name=analysis.mitre_technique_name,
                    source_ip=analysis.source_ip,
                    target_host=analysis.target_host,
                    confidence_score=analysis.confidence_score,
                    summary=analysis.summary,
                    technical_details=analysis.technical_details,
                    recommended_mitigation=analysis.recommended_mitigation,
                    status="INVESTIGATING",
                )
                db.add(inc2)

        db.commit()
        logger.info("Baseline security incidents seeded for live demonstration.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize DB tables, seed default data, and warm up ChromaDB
    logger.info("Starting CyberSentinel AI Engine...")
    Base.metadata.create_all(bind=engine)
    
    # Warm up ChromaDB collection & embeddings
    get_mitre_collection()

    db = SessionLocal()
    try:
        seed_initial_data(db)
    finally:
        db.close()
        
    yield
    # Shutdown
    logger.info("Shutting down CyberSentinel AI Engine...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Intelligent Security Operations Center (SOC) Assistant using RAG & LLMs",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API Routers
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(logs.router, prefix=settings.API_V1_STR)
app.include_router(incidents.router, prefix=settings.API_V1_STR)
app.include_router(chat.router, prefix=settings.API_V1_STR)
app.include_router(reports.router, prefix=settings.API_V1_STR)


@app.get("/health", tags=["Health Check"])
def health_check():
    """System health check verifying API readiness."""
    return {"status": "healthy", "version": settings.VERSION, "engine": "CyberSentinel AI"}


# Root Convenience & Fallback Aliases (Handles un-prefixed browser or test queries)
@app.get("/logs", tags=["Root Aliases"])
def root_logs_alias(db: Session = Depends(get_db)):
    from app.models.log_batch import LogBatch
    batches = db.query(LogBatch).order_by(LogBatch.uploaded_at.desc()).limit(20).all()
    return batches


@app.get("/alerts", tags=["Root Aliases"])
@app.get("/incidents", tags=["Root Aliases"])
def root_alerts_alias(db: Session = Depends(get_db)):
    from app.models.incident import Incident
    return db.query(Incident).order_by(Incident.created_at.desc()).limit(20).all()


@app.get("/stats", tags=["Root Aliases"])
def root_stats_alias(db: Session = Depends(get_db)):
    from app.models.incident import Incident
    total = db.query(Incident).count()
    critical = db.query(Incident).filter(Incident.severity == "CRITICAL").count()
    return {"total_incidents": total, "critical_count": critical}


# Production Unified Serving: Serve compiled React SPA if frontend/dist exists
frontend_dist = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"
if (frontend_dist / "assets").exists():
    app.mount("/assets", StaticFiles(directory=str(frontend_dist / "assets")), name="static_assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    def serve_frontend_spa(full_path: str):
        # Allow API routes and documentation to pass through
        if full_path.startswith("api") or full_path.startswith("docs") or full_path.startswith("openapi.json"):
            raise HTTPException(status_code=404, detail="API route not found")
        target_file = frontend_dist / full_path
        if target_file.exists() and target_file.is_file():
            return FileResponse(target_file)
        return FileResponse(frontend_dist / "index.html")

