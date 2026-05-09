import discord
from discord.ext import commands
import re
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

CANAL_MUSICA_ID = 1502012822811574432

YOUTUBE_REGEX = re.compile(r'(https?://)?(www\.)?(youtube|youtu|music\.youtube)\.(com|be)/.+')


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CANAL_MUSICA_ID:
        return

    if YOUTUBE_REGEX.search(message.content):
        try:
            await message.delete()
        except:
            pass

        await message.channel.send(f" **Nueva canción compartida**\n{message.content}")

bot.run(os.getenv("TOKEN"))





