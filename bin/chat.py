# Imports
import bin.config
import logging
import ollama

# Chat Function
# https://github.com/ollama/ollama-python/tree/main/examples
async def query_ai(bot, message):
    config = bin.config.Config()
    log = logging.getLogger(config.NAME)
    CONTENT = message.content.split(' ')[1:]

    URL = 'https://ai.potatolab.dev'
    async with message.channel.typing():
        try:
            api = ollama.AsyncClient(
                host=URL
            )
            r = await api.chat(model=config.OLLAMA_MODEL, message=[{ 
                'role': 'user', 
                'content': CONTENT
            }])
            await message.reply(r.message.content)

        except Exception as ex:
            log.error(f'Unable to get response from {URL} endpoint! Reason: {str(ex)}')
            log.debug(str(ex))
            await message.reply('Unable to reply to your message...ran out of cash (server issue).')
