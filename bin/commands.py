# Imports
import bin.config
import requests
import logging

# Command Functions
async def help(bot, message):
    config = bin.config.Config()
    CONTENT = message.content.split(' ')[1:]

    msg = '''**Help Guide:**
```'''
    for cmd in config.DISCORD_COMMANDS:
        usage = ' ' + config.DISCORD_COMMANDS[cmd]['usage'] if config.DISCORD_COMMANDS[cmd]['usage'] else ''
        description = config.DISCORD_COMMANDS[cmd]['description']

        msg += f'''@{bot.user.name} {config.DISCORD_COMMAND_STARTING_CHAR}{cmd}{usage} ({description})
'''
    msg +='''```'''

    await message.reply(msg, mention_author=True)

# https://icanhazdadjoke.com/api
async def joke(bot, message):
    config = bin.config.Config()
    log = logging.getLogger(config.NAME)
    CONTENT = message.content.split(' ')[1:]

    URL = 'https://icanhazdadjoke.com/'
    async with message.channel.typing():
        try:
                r = requests.get(
                    URL,
                    headers={
                        'User-Agent': f'DDG {config.NAME} Discord Bot',
                        'Accept': 'application/json'
                    }
                )
                if r.status_code == 200:
                    await message.reply(r.json()['joke'])
                else:
                    await message.reply('Unable to get you a random joke...ran out of cash (server issue).')

        except Exception as ex:
            log.error(f'Unable to get response from {URL} endpoint! Reason: {str(ex)}')
            log.debug(str(ex))
            await message.reply('Unable to get you a random joke...ran out of cash (server issue).')

# https://github.com/D3vd/Meme_Api
# https://meme-api.com/gimme
async def meme(bot, message):
    config = bin.config.Config()
    log = logging.getLogger(config.NAME)
    CONTENT = message.content.split(' ')[1:]

    URL = 'https://meme-api.com/gimme'
    async with message.channel.typing():
        try:
                r = requests.get(
                    URL,
                    headers={
                        'User-Agent': f'DDG {config.NAME} Discord Bot',
                        'Accept': 'application/json'
                    }
                )
                if r.status_code == 200:
                    await message.reply(r.json()['url'])
                else:
                    await message.reply('Unable to get you a random meme...ran out of cash (server issue).')

        except Exception as ex:
            log.error(f'Unable to get response from {URL} endpoint! Reason: {str(ex)}')
            log.debug(str(ex))
            await message.reply('Unable to get you a random meme...ran out of cash (server issue).')

# Ideas:
# - @Hookerbot /gif - random PG-13 gif (find API for this)
# - @Hookerbot /topic - give random topic (could use llama to come up with one)
# - chat with @Hookerbot (responses from llama)
