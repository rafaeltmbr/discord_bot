import os
import dotenv

from .commands import commands
from .bot import bot

def main():
    dotenv.load_dotenv()
    bot.run(os.environ.get('DISCORD_TOKEN'))