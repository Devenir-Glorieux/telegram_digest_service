from openai import OpenAI
from core.config.settings import settings
from telethon.tl.types import Message


class LLMClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.LLM_API, base_url=settings.LLM_URL)

    def generate_summary(self, messages: list[Message]) -> str:
        pass
