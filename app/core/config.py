# app/core/config.py
import os
from pydantic_settings import BaseSettings
from typing import Optional, List
import secrets

class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "Cheo-RAG service"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Notion Configuration
    NOTION_TOKEN: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True   
    
settings = Settings()