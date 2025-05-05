# Imports
import bin.commands
import logging
import os

# Classes
class Config:
    ## General
    NAME = 'hooker-bot'
    VERSION = os.environ.get('VERSION', 'v0.0')

    ## Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
    if LOG_LEVEL not in logging.getLevelNamesMapping(): raise ValueError('Invalid LOG_LEVEL environment variable value! Allowed: {}'.format(','.join(logging.getLevelNamesMapping())))

    ## Discord
    DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
    DISCORD_GENERAL_CHANNELID = os.environ.get('DISCORD_GENERAL_CHANNELID', None)
    if not DISCORD_GENERAL_CHANNELID.isdigit(): raise ValueError('Invalid DISCORD_GENERAL_CHANNELID environment variable value! Must be numeric.')
    DISCORD_GENERAL_CHANNELID = int(DISCORD_GENERAL_CHANNELID)
    DISCORD_COMMAND_STARTING_CHAR = '/'
    DISCORD_COMMANDS = {
        'help': {
            'call': bin.commands.help,
            'usage': '',
            'description': 'Help guide'
        },
        'joke': {
            'call': bin.commands.joke,
            'usage': '',
            'description': 'Random dad joke'
        },
        'meme': {
            'call': bin.commands.meme,
            'usage': '',
            'description': 'Random meme'
        }
    }

    ## OLLAMA
    OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL')
