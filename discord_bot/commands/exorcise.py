from discord.ext import commands

from ..bot import bot
from ..util.get_file_text import get_file_text

text = get_file_text('discord_bot/content/phrases/exorcise.txt')

@bot.command(name='exorcizar', aliases=['exorcise'])
async def exorcise(ctx: commands.Context, who):
    await ctx.send(f'{who} {text}')
