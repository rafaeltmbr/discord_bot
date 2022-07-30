import discord
from discord.ext import commands

from ..bot import bot
from ..controllers.dog.get_dog_image import get_dog_image

@bot.command(name='cachorro', aliases=['dog'])
async def dog(ctx: commands.Context):
    image_url = await get_dog_image()
    message: discord.Message = await ctx.send(image_url)
    await message.add_reaction('❤')
    await message.add_reaction('💔')