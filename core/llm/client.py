from core.config.settings import settings
from openai import OpenAI
from telethon.tl.types import Message
from core.llm.promts import SUMMARY_PROMT
from core.config.logging import get_logger

logger = get_logger()


class LLMClient:
    def __init__(self, client: OpenAI):
        self.client = client
        self.model = settings.LLM_MODEL_NAME
        self.temperature = settings.TEMPERATURE
        self.timeout = settings.LLM_TIMEOUT

    def health_check(self):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Hello, world!"}],
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error: {e}")

    # GET /api/v1/credits

    def generate_summary(self, messages: list[Message]) -> str:
        try:
            logger.info(f"Messages: {type(messages)}")
            formatted_messages = self._format_messages(messages)
            logger.info(f"Formatted messages: {type(formatted_messages)}")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SUMMARY_PROMT},
                    {"role": "user", "content": formatted_messages},
                ],
                temperature=self.temperature,
                timeout=self.timeout,
            )

            summary = response.choices[0].message.content
            logger.info("Summary generated successfully")
            return summary

        except Exception as e:
            logger.error(f"Error generating summary: {str(e)}")
            raise

    def _format_messages(self, messages: list[tuple[str, Message]]) -> str:
        logger.info("Run _format_messages")
        formatted = []
        for channel_name, msg in messages:
            ts = msg.date.strftime("%Y-%m-%d %H:%M")
            text = (msg.text or "").replace("\n", " ").strip()
            # TODO add message.media
            line = f"[{ts}] @{channel_name}: {text}"
            formatted.append(line)
        return "\n".join(formatted)
