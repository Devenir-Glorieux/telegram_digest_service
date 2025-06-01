from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    TELEGRAM_SESSION_NAME: str = Field(alias="TELEGRAM_SESSION_NAME", default="anon")
    TELEGRAM_API_ID: str = Field(alias="TELEGRAM_API_ID")
    TELEGRAM_API_HASH: str = Field(alias="TELEGRAM_API_HASH")
    NUMBER_OF_RECENT_MESSAGES: int = Field(alias="NUMBER_OF_RECENT_MESSAGES")
    
    LLM_API_KEY: str = Field(alias="LLM_API_KEY")
    LLM_BASE_URL: str = Field(alias="LLM_BASE_URL")
    LLM_MODEL_NAME: str = Field(alias="LLM_MODEL_NAME")
    TEMPERATURE: float = Field(alias="TEMPERATURE")
    LLM_TIMEOUT: int = Field(alias="LLM_TIMEOUT")
    LOG_LEVEL: str = Field(alias="LOG_LEVEL")
    TARGET_CHANNEL: str = Field(alias="TARGET_CHANNEL")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
