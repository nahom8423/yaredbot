import discord
import requests
import pdf2image
import os
from discord.ext import commands, tasks
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False  # You can customize these based on your bot's requirements
intents.presences = False

TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'
GUILD_ID = '970490174565928960'
CHANNEL_ID = '972131288251240579'  # The ID of the channel where you want to send the picture

# List of URLs for each week
IMAGE_URLS = [
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/meskerem/01meskerem.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/meskerem/02meskerem.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/meskerem/03meskerem.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenetsige/01meskeremzemenetsige.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenetsige/01meskeremzemenetsige.pdf', # 1ST WEEK TSIGE
    '',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenetsige/03zemene%20Tsege.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/hidar/04hidarastemehro.pdf',
    '',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenetsige/06zemenetsige.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenesibket/01zemenesibket.pdf', # 1ST WEEK ስብከት
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenesibket/02zemenesibket.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenesibket/03zemenesibket.pdf',
    'https://www.ethiopianorthodox.org/amharic/holybooks/sundaysmisbakwengel/zemenesibket/04lidet.pdf',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',

    # Add the URLs for all 62 weeks here
]

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def misbak(ctx):
    # Check if today is a Monday
    today = datetime.today()
    if today.weekday() == 0:
        for url_index in range(len(IMAGE_URLS)):
            await download_and_send_image(ctx, url_index)

async def download_and_send_image(ctx, url_index):
    try:
        # Download the PDF or image
        response = requests.get(IMAGE_URLS[url_index])
        extension = IMAGE_URLS[url_index].split('.')[-1]
        file_name = f'image_{url_index + 1}.{extension}'
        with open(file_name, 'wb') as file:
            file.write(response.content)

        # Send the image to the specified channel
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(file=discord.File(file_name))

        # Clean up
        os.remove(file_name)

    except Exception as e:
        await ctx.send(f'Error: {e}')

bot.run(TOKEN)
