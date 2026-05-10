import discord
from discord.ext import commands
import re
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)


CANAL_MUSICA_ID = 1502012822811574432


YOUTUBE_REGEX = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be|music\.youtube\.com)/[^\s]+', re.IGNORECASE)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CANAL_MUSICA_ID:
        return

    tiene_youtube = YOUTUBE_REGEX.search(message.content)

    try:
        if tiene_youtube:
            
            await message.delete()
            await message.channel.send(f"**Nueva canción compartida**\n{message.content}")
        else:
            
            await message.delete()
    except discord.Forbidden:
        print(" No tengo permisos para borrar mensajes")
    except Exception as e:
        print(f" Error: {e}")

bot.run(os.getenv("TOKEN"))


