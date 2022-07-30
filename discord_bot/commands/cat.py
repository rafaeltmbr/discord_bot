import discord
from discord.ext import commands

from ..bot import bot
from ..controllers.cat.get_cat_image import get_cat_image

@bot.command(name='gato', aliases=['cat'])
async def cat(ctx: commands.Context):
    image_url = await get_cat_image()
    message: discord.Message = await ctx.send(image_url)
    await message.add_reaction('❤')
    await message.add_reaction('💔')