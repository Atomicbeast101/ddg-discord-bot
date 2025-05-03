# Imports
import bin.config
import bin.bot
import traceback
import logging
import discord
import sys

# Attributes
config = bin.config.Config()

# Functions
def setup_log(config):
    log = None

    logFormatter = logging.Formatter('{"time":"%(asctime)s","type":"app","level":"%(levelname)s","message":"%(message)s"}')
    log = logging.getLogger()

    # Add console logging
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    log.addHandler(consoleHandler)

    # Add syslog logging
    # address = config.LOG_SYSLOG_HOST.split(':')[0]
    # port = int(config.LOG_SYSLOG_HOST.split(':')[-1]) if ':' in config.LOG_SYSLOG_HOST else 514
    # syslogHandler = logging.handlers.SysLogHandler(address=(address, port))
    # syslogHandler.setFormatter(logFormatter)
    # log.addHandler(syslogHandler)

    log.setLevel(config.LOG_LEVEL)

    return log

# Main
if __name__ == '__main__':
    # Setup logging
    log = setup_log(config)

    try:
        log.info(f'Starting up {config.NAME} {config.VERSION}...')

        # Configure discord bot
        intents = discord.Intents.default()
        intents.message_content = True
        bot = bin.bot.BotClient(intents=intents)

        log.info(f'{config.NAME} {config.VERSION} ready to serve!')
        bot.run(config.DISCORD_TOKEN, log_handler=None)

    except Exception as ex:
        log.error(ex)
        log.debug(traceback.format_exc())
        exit(2)
