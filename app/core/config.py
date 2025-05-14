import os
from dotenv import load_dotenv
import secrets
from typing import List, Union
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, Field, field_validator

DATABASE_URL=os.getenv("DATABASE_URL")

# Base Configuration
class Settings(BaseSettings):
    # API settings
    API_STR: str = "/api"

    # Security
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))

    # Access token expiry
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # CORS
    CORS_ORIGINS: List[Union[AnyHttpUrl, str]] = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str = DATABASE_URL

    # AI model config
    AI_MODEL_NAME: str = "gpt-4o"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    # Validate CORS
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v

settings = Settings()
