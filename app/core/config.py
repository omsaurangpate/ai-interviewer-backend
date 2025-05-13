import secrets
from typing import List, Union
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, Field, field_validator

# Base Configuration
class Settings(BaseSettings):
    # API settings
    API_STR: str = "/api"

    # Security
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))

    # CORS
    CORS_ORIGINS: List[Union[AnyHttpUrl, str]] = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/ai_interviewer"  #TODO: CHANGE URL

    # AI model config
    AI_MODEL_NAME: str = "gpt-4o"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    # Validate CORS
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",")]
        return value

settings = Settings()
