import asyncio
from core.telegram.client import TelegramService
from core.config import settings

async def main():
    service = TelegramService()
    await service.start()
    
    try:
        for channel in settings.TARGET_CHANNELS:
            messages = await service.get_recent_messages(channel)
            print(f"Получено {len(messages)} сообщений из канала {channel}")
            
            for msg in messages:
                print(f"Message: {msg.text[:100]}...")
    finally:
        await service.stop()

if __name__ == "__main__":
    asyncio.run(main())