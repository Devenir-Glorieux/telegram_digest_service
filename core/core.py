from core.config.settings import settings
from core.telegram.client import TelegramClientWrangler
from core.config.logging import get_logger
from core.llm.client import LLMClient
from openai import OpenAI


logger = get_logger()


async def app():
    service = TelegramClientWrangler()
    await service.start()
    target_channels = await service.get_list_of_chanels()
    logger.info(f"Get channels: {len(target_channels)}")

    all_messages = []
    try:
        for channel in target_channels:
            messages = await service.get_recent_messages(channel, settings.NUMBER_OF_RECENT_MESSAGES)
            logger.info(f"Get {len(messages)} messages from channel {channel}")
            for message in messages:
                all_messages.append((channel, message))

        logger.info(f"Get {len(all_messages)} messages from channels")

        llm_client = OpenAI(
            api_key=settings.LLM_API_KEY, base_url=settings.LLM_BASE_URL
        )
        logger.info("LLM client was created")
        llm_service = LLMClient(llm_client)
        # health_check = llm_service.health_check()
        # logger.info(f"Health check: {health_check}")
        digest_content = llm_service.generate_summary(all_messages)
        logger.info(f"Digest content: {digest_content}")
        await service.publish_digest(digest_content)

    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        await service.stop()
