# core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_TITLE: str = "My FastAPI Project"
    API_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./test.db"
    DEBUG: bool = True
    REDIS_URL: str = "redis://default:password@localhost:6379"
    ORIGINS: list = [  # CORS
        # "*"
        "http://localhost",
        "http://localhost:8000",
    ]
    ALLOWED_HOSTS: list = [
        'localhost',
        'localhost:8000',
        '127.0.0.1',
        '127.0.0.1:8000'
    ]

    class Config:
        env_file = ".env"

settings = Settings()
    