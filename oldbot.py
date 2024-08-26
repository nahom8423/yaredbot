import discord
from discord.ext import commands
import os

# Assuming you're correctly using an environment variable now
TOKEN = os.getenv("OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents, application_id=971210123248803872)

async def load_extensions():
    await bot.load_extension("cogs.misbak")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await load_extensions()

bot.run(TOKEN)
