import os
from pathlib import Path
from pydantic_settings import BaseSettings


DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "govtech.db"
DEFAULT_DB_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH.as_posix()}")


class Settings(BaseSettings):
    app_name: str = "GovTech Grievance AI"
    environment: str = "development"
    database_url: str = DEFAULT_DB_URL
    secret_key: str = os.getenv("SECRET_KEY", "changeme-secret")
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"
        env_file_encoding = "utf-8"


settings = Settings()
