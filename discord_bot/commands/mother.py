from discord.ext import commands
import random

from ..bot import bot
from ..util.get_file_lines import get_file_lines

phrases = get_file_lines('discord_bot/content/phrases/mother.txt')

AUTHORIZED_ROLES = ['adm', 'adms', 'admin', 'admins', "Pk's Academy"]
NOT_AUTHORIZED_MESSAGE = 'com grandes poderes vem grandes responsabilidades.'

@bot.command(name='mae', aliases=['mãe', 'mother'])
async def mother(ctx: commands.Context, who):
    author_roles = [role.name.lower() for role in ctx.author.roles]

    if set(AUTHORIZED_ROLES) & set(author_roles):
        phrase = phrases[random.randrange(len(phrases))]
        await ctx.send(f'{who} {phrase}')
        return
    
    await ctx.send(f'{ctx.author.name}, {NOT_AUTHORIZED_MESSAGE}')

