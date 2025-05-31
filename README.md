## Telegram Digest Service

A modular microservice for aggregating content from Telegram channels, generating summaries using an LLM, and publishing digests to a target channel.

### Overview
This service automates the following workflow:

**Collect Messages:** Fetch recent messages from a configurable list of Telegram channels.  
**Build Digest:** Use an LLM to generate a concise summary of collected content.  
**Publish Digest:** Send the summary as a scheduled to a designated Telegram channel.  
**Extensible Architecture:** Designed with clear separation between core business logic and external adapters.  