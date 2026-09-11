from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "CyberSentinel AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Security & JWT
    SECRET_KEY: str = "dev-insecure-secret-key-change-in-production-cybersentinel-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Database: Defaults to local SQLite for instant zero-dependency setup, easily switched to PostgreSQL
    DATABASE_URL: str = "sqlite:///./cybersentinel.db"

    # Vector Database & Embeddings
    CHROMA_PERSIST_DIR: str = "./chroma_db"
    CHROMA_COLLECTION_NAME: str = "mitre_attack_enterprise"

    # LLM API Keys (optional at startup, required for AI analysis)
    GEMINI_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    LLM_PROVIDER: str = "gemini"  # or "openai"

    # CORS Origins
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")


settings = Settings()
