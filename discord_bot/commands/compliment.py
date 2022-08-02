from discord.ext import commands
import random

from ..bot import bot
from ..util.get_file_lines import get_file_lines

phrases = get_file_lines('discord_bot/content/phrases/compliment.txt')

@bot.command(name='elogiar', aliases=['compliment'])
async def compliment(ctx: commands.Context, who):
    phrase = phrases[random.randrange(len(phrases))]
    await ctx.send(f'{who} {phrase}')
