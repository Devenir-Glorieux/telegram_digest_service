from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    TELEGRAM_SESSION_NAME: str = Field(alias="TELEGRAM_SESSION_NAME", default="anon")
    TELEGRAM_API_ID: str = Field(alias="TELEGRAM_API_ID")
    TELEGRAM_API_HASH: str = Field(alias="TELEGRAM_API_HASH")



    # MODEL: str = Field(alias="MODEL")
    # TEMPERATURE: float = Field(alias="TEMPERATURE")
    # TOP_P: float = Field(alias="TOP_P")
    # LLM_TIMEOUT: int = Field(alias="LLM_TIMEOUT")
    # MAX_NUMBER_OF_CALLS: int = Field(alias="MAX_NUMBER_OF_CALLS")
    LOG_LEVEL: str = Field(alias="LOG_LEVEL")



@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
