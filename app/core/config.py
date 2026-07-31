from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ==========================================
    # Application
    # ==========================================
    app_name: str = "Penalty Shootout Backend"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    # ==========================================
    # API
    # ==========================================
    api_v1_prefix: str = "/api/v1"
    host: str = "0.0.0.0"
    port: int = 8000

    # ==========================================
    # Database
    # ==========================================
    database_url: str

    # ==========================================
    # Logging
    # ==========================================
    log_level: str = "INFO"
    log_format: str = "json"

    # ==========================================
    # Time
    # ==========================================
    timezone: str = "UTC"

    # ==========================================
    # CORS
    # ==========================================
    cors_origins: str = "*"

    # ==========================================
    # Security
    # ==========================================
    secret_key: str


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
