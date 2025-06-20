# Imports
import bin.config
import bin.chat
import traceback
import discord
import logging
import random

# Attributes
config = bin.config.Config()
log = logging.getLogger(config.NAME)

# Class
class BotClient(discord.Client):
    async def on_ready(self):
        log.info(f'Starting up {config.NAME} discord bot...')

        # Set activity status
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'@{self.user.name} {config.DISCORD_COMMAND_STARTING_CHAR}help'))

        log.info(f'Bot ready to work in dark alleys!')

        if config.DISCORD_GENERAL_CHANNELID:
            await self.get_channel(config.DISCORD_GENERAL_CHANNELID).send(f'I can do services for ${random.randint(1, 10)} :dollar:')

    # async def on_member_join(self, member):
    #     print() # TODO
    # await member.create_dm()
    # await member.dm_channel.send(
    #     f'Hi {member.name}, welcome to my Discord server!'
    # )

    async def on_message(self, message):
        try:
            # Prevent bot from talking to itself
            if message.author == self.user:
                return

            # Process commands
            if message.content.startswith(f'<@{self.user.id}>'):
                CONTENT = message.content.split(' ')[1:]

                if message.content.split(' ')[1][0] == config.DISCORD_COMMAND_STARTING_CHAR:
                    COMMAND = message.content.split(' ')[1][1:].lower()
                    if COMMAND in config.DISCORD_COMMANDS:
                        await config.DISCORD_COMMANDS[COMMAND]['call'](self, message)

                elif CONTENT.lower() == 'fuck you':
                    await message.reply(f'That\'ll cost ya ${random.randint(1, 10)} :dollar:', mention_author=True)

                else:
                    # await bin.chat.query_ai(self, message)
                    await message.reply('I\'m on 5min break (not ready for AI responses yet).', mention_author=True)

            elif message.content.lower().contains('bitch'):
                await message.reply('hoe', mention_author=True)

        except Exception as ex:
            log.error(f'Unexpected error when trying to process message from {message.author.name} ({message.author.id}): [{message.content}]. Reason: {str(ex)}\n{traceback.format_exc()}')
