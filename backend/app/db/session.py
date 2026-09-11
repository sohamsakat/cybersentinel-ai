from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# In SQLite, connect_args={"check_same_thread": False} is required for multi-threaded FastAPI handlers
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    echo=False,  # Set to True if SQL query debugging is needed
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency that yields a SQLAlchemy database session and ensures cleanup."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
