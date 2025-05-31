import asyncio
from core.telegram.client import TelegramClientWrangler
from core.config.logging import get_logger

logger = get_logger()


async def main():
    service = TelegramClientWrangler()
    await service.start()
    target_channels = await service.get_list_of_chanels()
    logger.info(f"Найдены каналы: {target_channels}")

    for channel in target_channels:
        messages = await service.get_recent_messages(channel, 1)
        print(f"Получено {len(messages)} сообщений из канала {channel}")
        
        for msg in messages:
            print(f"Message: {msg.text[:1]}...")
    # finally:
    #     await service.stop()

if __name__ == "__main__":
    asyncio.run(main())