from telethon import TelegramClient
from telethon.tl.types import Message
from core.config.settings import settings
from core.config.logging import get_logger

from datetime import datetime
from typing import Optional

logger = get_logger()


class TelegramClientWrangler:
    def __init__(self):
        self.client = TelegramClient(
            settings.TELEGRAM_SESSION_NAME,
            settings.TELEGRAM_API_ID,
            settings.TELEGRAM_API_HASH,
        )
        self.target_channel = settings.TARGET_CHANNEL

    async def start(self):
        await self.client.start()

    async def stop(self):
        await self.client.disconnect()

    async def get_list_of_chanels(self) -> list:
        channels_list = []
        async for dialog in self.client.iter_dialogs():
            entity = dialog.entity
            if getattr(entity, "broadcast", False):
                channels_list.append(str(entity.username))
                logger.debug(f"{entity.title} — @{entity.username}")

        return list(set(channels_list))

    async def get_recent_messages(
        self, channel_name: str, limit_messages: int
    ) -> list[Message]:
        entity = await self.client.get_entity(channel_name)
        messages = await self.client.get_messages(
            entity,
            limit=limit_messages,
        )

        return messages

    async def publish_digest(
        self, content: str, schedule_time: Optional[datetime] = None
    ) -> None:
        entity = await self.client.get_entity(self.target_channel)

        formatted_content = f"""📰
                    {content}

        Generated automatically • {datetime.now().strftime("%d.%m.%Y")}
                            """

        if schedule_time:
            await self.client.send_message(
                entity, formatted_content, schedule=schedule_time
            )
        else:
            await self.client.send_message(entity, formatted_content)
