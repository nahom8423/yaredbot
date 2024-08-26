from discord import ApplicationContext
import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from discord import Interaction
from datetime import datetime
from datetime import datetime, timedelta
import pytz
import os
import asyncio
from discord.ui import View, Button
from discord import Embed
import math
from discord.ext import tasks

# Use environment variables or a config file to store these values securely
TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
GUILD_ID = '970490174565928960'

# Allowed channels for the misbak command
ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063', '970857256251953162']  # Add other channel IDs as needed

# Paths to the images for each week
# Each week can have multiple images
IMAGE_PATHS = {
    1: ["week1_image1.png"], #"week1_image2.png"],
    2: ["week2_image1.png"],
    3: ["week3_image1.png"],
    4: ["week4_image1.png"],
    5: ["week5_image1.png"],
    6: ["week6_image1.png"],
    7: ["week7_image1.png"],
    8: ["week8_image1.png"],
    9: ["week9_image1.png"],
    10: ["week10_image1.png"],
    11: ["week11_image1.png"],
    12: ["week12_image1.png"],
    13: ["week13_image1.png"],
    14: ["week14_image1.png"],
    15: ["week15_image1.png"],
    16: ["week16_image1.png"],
    17: ["week17_image1.png"],
    18: ["week18_image1.png"],
    19: ["week19_image1.png"],
    20: ["week20_image1.png"],
    21: ["week21_image1.png"],
    22: ["week22_image1.png"],
    23: ["week23_image1.png"],
    24: ["week24_image1.png"],
    25: ["week25_image1.png"],
    26: ["week26_image1.png"],
    27: ["week27_image1.png"],
    28: ["week28_image1.png"],
    29: ["week29_image1.png"],
    30: ["week30_image1.png"],
    31: ["week31_image1.png"],
    32: ["week32_image1.png"],
    33: ["week33_image1.png"],
    34: ["week34_image1.png"],
    35: ["week35_image1.png"],
    36: ["week36_image1.png"],
    37: ["week37_image1.png"],
    38: ["week38_image1.png"],
    39: ["week39_image1.png"],
    40: ["week40_image1.png"],
    41: ["week41_image1.png", "week41_image2.png"], 
    42: ["week42_image1.png"], 
    43: ["week43_image1.png"], 
    44: ["week44_image1.png"], 
    45: ["week45_image1.png"],
    46: ["week46_image1.png"],
    47: ["week47_image1.png"],
    48: ["week48_image1.png"],
    49: ["week49_image1.png"],
    50: ["week50_image1.png"],
    51: ["week51_image1.png"],
    52: ["week52_image1.png"],
}

MEZMUR_PATHS = {
    43: ["week43.txt"],
    44: ["week44.txt"],
    45: ["week45.txt"],
    46: ["week46.txt"],
    
}


# Base directory where all images are stored
BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"

BASE_MEZMUR_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\mezmurs"

# Dictionary to store text for each week
week_texts = {}

bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())



SPECIFIC_CHANNEL_ID = '972131288251240579'  # Channel where bot reacts to new images

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# rich presence
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    # Set the rich presence
    activity = discord.Game(name="ጸናጽል", type=0)  # Type 3 is "Watching" 0=playing 1=streaming 2=listening 3=watching 4=custom(notforbot) 5=competing
    await bot.change_presence(status=discord.Status.online, activity=activity) 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    # Set the rich presence with an image
    activity = discord.Activity(name="ጸናጽል", type=discord.ActivityType.playing, large_image="tsenatsil_silver")
    await bot.change_presence(activity=activity)

    #rich presense 2
import logging

# Configure logging to print to stdout (console)
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

@bot.event
async def on_ready():
    logging.info(f'We have logged in as {bot.user}')
    try:
        # Set the rich presence
        activity = discord.Game(name="ጸናጽል", type=0)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        logging.info("Rich presence set successfully.")
    except Exception as e:
        logging.error(f"Error setting rich presence: {e}")

# ... rest of your bot code ...

# end of rich presence

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message is in the specified channel and has attachments
    if str(message.channel.id) == SPECIFIC_CHANNEL_ID and message.attachments:
        # Call the logic that sends weekly images based on attachments
        await send_weekly_images(message.channel)

    # Important: process other commands including slash commands
    await bot.process_commands(message)

@bot.slash_command(name="misbak")
async def misbak(ctx: ApplicationContext):
    # Check if the command is used in an allowed channel
    if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
        await ctx.respond("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
        return

    # Defer the response if the operation might take longer
    await ctx.defer()

    # Call the logic that sends weekly images for the slash command
    try:
        await send_weekly_images(ctx.channel)
        await ctx.respond("ዘሰንበት ምስባክ")  # Send a response message indicating success
    except Exception as e:
        await ctx.respond(f"An error occurred: {e}")  # Send a response message indicating failure

async def send_weekly_images(channel):
    week_number = datetime.now().isocalendar()[1]
    
    # Check if there are images for this week
    if week_number in IMAGE_PATHS:
        # Send all images for this week
        for image_file in IMAGE_PATHS[week_number]:
            image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
            if os.path.exists(image_file_path):
                await channel.send(file=discord.File(image_file_path))
        
        # If there's text associated with this week, send it as well
        if week_number in week_texts:
            await channel.send(week_texts[week_number])
    else:
        # If there are no images set for this week, inform the channel
        await channel.send('No ምስባክ set for this week.')


@bot.slash_command(name="mezmur")
async def mezmur(ctx: ApplicationContext):
    # Check if the command is used in an allowed channel
    if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
        await ctx.respond("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
        return

    week_number = datetime.now().isocalendar()[1]

    if week_number in MEZMUR_PATHS:
        for mezmur_file in MEZMUR_PATHS[week_number]:
            # Use os.path.join to construct the file path
            file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)

            # Debug: Print the variables to check them
            print(f"BASE_MEZMUR_DIR: {BASE_MEZMUR_DIR}")
            print(f"mezmur_file: {mezmur_file}")
            print(f"Constructed file_path: {file_path}")

            if os.path.exists(file_path):
                # If the file exists, open and read it
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    await ctx.respond(content)
            else:
                # If the file does not exist, log a warning and send a response
                logging.warning(f"Mezmur file for week {week_number} not found at path: {file_path}")
                await ctx.respond(f"Mezmur file for week {week_number} not found.")
    else:
        # If no mezmur is set for the week, log the information and send a response
        logging.info(f"No mezmur set for this week {week_number}")
        await ctx.respond('No mezmur set for this week.')




# url vc join
@bot.slash_command(name="join")
async def join(ctx):
    """Join the voice channel."""
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.slash_command(name="leave")
async def leave(ctx):
    """Leave the voice channel."""
    await ctx.voice_client.disconnect()

@bot.slash_command(name="play")
async def play(ctx: ApplicationContext, url: str):
    """Play audio from a direct link."""
    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()
    ctx.voice_client.play(FFmpegPCMAudio(executable="ffmpeg", source=url))

@bot.slash_command(name="stop")
async def stop(ctx):
    """Stop audio playback."""
    if ctx.voice_client:
        ctx.voice_client.stop()    


# NEXT MAHLET (BEAL) COMMAND
mahlets = [
    {"date": "2023-11-05", "channel_id": 974280014390501376, "description": "ማኅሌተ ጽጌ"},
    {"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
    {"date": "2023-11-12", "channel_id": 974280676130029608, "description": "ማኅሌተ ጽጌ"},
    {"date": "2023-11-17", "channel_id": 974281498482053170, "description": "ቁስቋም"},
    #{"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
    #{"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
    #{"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
    #{"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
    # Add more mahlets as needed
]

# ... (your existing bot code) ...

# Updated Command: ?nextbeal (previously ?nextmahlet)
@bot.slash_command(name="nextbeal")
async def next_beal(ctx: ApplicationContext):
    # Get the current date and time
    now = datetime.now(pytz.UTC)
    
    # Find the next mahlet (beal)
    next_mahlet = None
    for mahlet in mahlets:
        mahlet_date = datetime.strptime(mahlet["date"], "%Y-%m-%d").replace(tzinfo=pytz.UTC)
        if mahlet_date > now:
            next_mahlet = mahlet
            break
    
    # If a next mahlet (beal) is found, send a message with a link to the specified channel
    if next_mahlet:
        channel = bot.get_channel(next_mahlet["channel_id"])
        if channel:
            await ctx.respond(f"{next_mahlet['date']} in {channel.mention}. {next_mahlet['description']}")
        else:
            await ctx.respond("The specified channel for the next beal was not found.")
    else:
        await ctx.respond("There are no upcoming beals.")


############################################################################

# DATE UPDATER



# Voice channel IDs
DATE_CHANNEL_ID = 1167180226451746876  # Replace with the actual channel ID
DAY_NAME_CHANNEL_ID = 1167180947918168074  # Replace with the actual channel ID



# Ethiopian month names
ethiopian_months = ["የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሳስ", "ጥር"]

# Names for each day
day_names = [
    "ልደታ ፤ ራጉኤል ፤ ኤልያስ",
    "ታዴዎስ ሐዋርያ ፤ ኢዮብ ጻድቅ",
    "በዓታ ማርያም ፤ ዜና ማርቆስ ፤ ነአኲቶ ለአብ",
    "ዮሐንስ ወልደ ንጐድጓድ",
    "ጴጥሮስ ወጳውሎስ ፤ አቡነ ገብረ መንፈስ ቅዱስ",
    "ኢየሱስ ፤ ቁስቋም ፤ ቅድስት አርሴማ",
    "ሥላሴ ፤ ፊሊሞን ፤ አብላንዮስ",
    "ማቴዎስ ፤ ዮልያኖስ ፤ አባ ኪሮስ",
    "ቶማስ ሐዋርያ ፤ አንድርያስ ሐዋርያ ፤ አውሳብዮስ ፤ አርባ ሰማዕታት",
    "በዓለ መስቀሉ ለእግዚእነ",
    "ሐና ወኢያቄም ፤ ቅዱስ ፋሲለደስ ሰማዕት ፤ ቅዱስ ያሬድ",
    "ሚካኤል ፤ ክርስቶስ ሠመራ ፤ አባ ሳሙኤል",
    "እግዚአብሔር አብ ፤ ቅዱስ ሩፋኤል ፤ ተዓምረ ባስልዮስ",
    "አቡነ አረጋዊ ፤ አባ ገብረ ክርስቶስ ፤ ድምጥያኖስ ሰማዕት",
    "ቂርቆስና ኢየሉጣ ፤ ስልፋኮስ",
    "ኪዳነ ምሕረት ፤ ሚካኤል ጳጳስ",
    "ቅዱስ እስጢፋኖስ ፤ ሉቃስ ዘዓምደ ብርሃን ፤ አባ ግርማ",
    "ፊልጶስ ሐዋርያ ፤ ኤስድሮስ ሰማዕት ፤ ተክለ አልፋ ኤውስጣቴዎስ ሰማዕት",
    "ቅዱስ ገብርኤል ፤ አርቃዲዎስ ፤ ጎርጎርዮስ ሊቀ ጳጳስ",
    "ጽንጸታ ለማርያም ፤ ነቢዩ ኤልሳ ፤ ሐጌ ነቢይ ፤ አባ ሰላማ መተርጉም ፤ ሕንጸተ አትናቴዮስ ሊቀጳጳስ",
    "ማርያም",
    "ቅዱስ ዑራኤል ፤ ደቅስዮስ ፤ ያዕቆብ ምሥራቃዊ",
    "ጊዮርጊስ ፤ ልጊኖስ ሰማዕት",
    "አቡነ ተክለ ሃይማኖት",
    "መርቆሬዎስ ፤ አኒፍኖስ",
    "ሆሴዕ ነቢይ ፤ ሳዶቅ ሰማዕት ፤ ቶምስ ደቀመዝሙር",
    "መድኃኔዓለም ፤ ሕዝቅያስ ነቢይ ፤ አባ ዮሐንስ",
    "አማኑኤል ፤ ቆስጠንጢስኖስ ፤ አብርሃም",
    "በዓለ ወልድ ፤ ሳሙኤል ዘወገግ",
    "ማርቆስ ወንጌላዊ"
]


async def check_and_update_voice_channels(bot, date_channel_id, day_name_channel_id):
    # Get the current date and time in EST and adjust for Ethiopian calendar
    now = datetime.now(pytz.timezone('America/New_York')) - timedelta(days=11)
    
    # Ethiopian month names
    ethiopian_months = [
        "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", 
        "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሳስ", "ጥር"
    ]
    
    # Names for each day
    day_names = [
    "ልደታ ፤ ራጉኤል ፤ ኤልያስ",
    "ታዴዎስ ሐዋርያ ፤ ኢዮብ ጻድቅ",
    "በዓታ ማርያም ፤ ዜና ማርቆስ ፤ ነአኲቶ ለአብ",
    "ዮሐንስ ወልደ ንጐድጓድ",
    "ጴጥሮስ ወጳውሎስ ፤ አቡነ ገብረ መንፈስ ቅዱስ",
    "ኢየሱስ ፤ ቁስቋም ፤ ቅድስት አርሴማ",
    "ሥላሴ ፤ ፊሊሞን ፤ አብላንዮስ",
    "ማቴዎስ ፤ ዮልያኖስ ፤ አባ ኪሮስ",
    "ቶማስ ሐዋርያ ፤ አንድርያስ ሐዋርያ ፤ አውሳብዮስ ፤ አርባ ሰማዕታት",
    "በዓለ መስቀሉ ለእግዚእነ",
    "ሐና ወኢያቄም ፤ ቅዱስ ፋሲለደስ ሰማዕት ፤ ቅዱስ ያሬድ",
    "ሚካኤል ፤ ክርስቶስ ሠመራ ፤ አባ ሳሙኤል",
    "እግዚአብሔር አብ ፤ ቅዱስ ሩፋኤል ፤ ተዓምረ ባስልዮስ",
    "አቡነ አረጋዊ ፤ አባ ገብረ ክርስቶስ ፤ ድምጥያኖስ ሰማዕት",
    "ቂርቆስና ኢየሉጣ ፤ ስልፋኮስ",
    "ኪዳነ ምሕረት ፤ ሚካኤል ጳጳስ",
    "ቅዱስ እስጢፋኖስ ፤ ሉቃስ ዘዓምደ ብርሃን ፤ አባ ግርማ",
    "ፊልጶስ ሐዋርያ ፤ ኤስድሮስ ሰማዕት ፤ ተክለ አልፋ ኤውስጣቴዎስ ሰማዕት",
    "ቅዱስ ገብርኤል ፤ አርቃዲዎስ ፤ ጎርጎርዮስ ሊቀ ጳጳስ",
    "ጽንጸታ ለማርያም ፤ ነቢዩ ኤልሳ ፤ ሐጌ ነቢይ ፤ አባ ሰላማ መተርጉም ፤ ሕንጸተ አትናቴዮስ ሊቀጳጳስ",
    "ማርያም",
    "ቅዱስ ዑራኤል ፤ ደቅስዮስ ፤ ያዕቆብ ምሥራቃዊ",
    "ጊዮርጊስ ፤ ልጊኖስ ሰማዕት",
    "አቡነ ተክለ ሃይማኖት",
    "መርቆሬዎስ ፤ አኒፍኖስ",
    "ሆሴዕ ነቢይ ፤ ሳዶቅ ሰማዕት ፤ ቶምስ ደቀመዝሙር",
    "መድኃኔዓለም ፤ ሕዝቅያስ ነቢይ ፤ አባ ዮሐንስ",
    "አማኑኤል ፤ ቆስጠንጢስኖስ ፤ አብርሃም",
    "በዓለ ወልድ ፤ ሳሙኤል ዘወገግ",
    "ማርቆስ ወንጌላዊ"
]

    
    # Construct the new channel names
    date_channel_name = f"{ethiopian_months[now.month-1]} {now.day}"
    day_channel_name = day_names[(now.day-1) % len(day_names)]  # Use modulo to avoid IndexError
    
    # Get the channels
    date_channel = bot.get_channel(date_channel_id)
    day_name_channel = bot.get_channel(day_name_channel_id)

    # Check if channels exist and their names need updating
    if date_channel and date_channel.name != date_channel_name:
        await date_channel.edit(name=date_channel_name)
    
    if day_name_channel and day_name_channel.name != day_channel_name:
        await day_name_channel.edit(name=day_channel_name)

@tasks.loop(hours=24)
async def update_voice_channels():
    # Get the current date and time in EST and adjust for Ethiopian calendar
    now = datetime.now(pytz.timezone('America/New_York')) - timedelta(days=11)
    
    # Construct the new channel names
    date_channel_name = f"{ethiopian_months[now.month-1]} {now.day}"
    day_channel_name = day_names[(now.day-1) % len(day_names)]  # Use modulo to avoid IndexError
    
    # Get the channels and update their names
    date_channel = bot.get_channel(DATE_CHANNEL_ID)
    day_name_channel = bot.get_channel(DAY_NAME_CHANNEL_ID)

    if date_channel:
        await date_channel.edit(name=date_channel_name)
    else:
        print("Date channel not found")

    if day_name_channel:
        await day_name_channel.edit(name=day_channel_name)
    else:
        print("Day name channel not found")




@tasks.loop(hours=24)
async def scheduled_channel_update():
        await check_and_update_voice_channels(bot, DATE_CHANNEL_ID, DAY_NAME_CHANNEL_ID)

# Start the loop when the bot is ready
@scheduled_channel_update.before_loop
async def before_scheduled_channel_update():
    await bot.wait_until_ready()

scheduled_channel_update.start()
       

###############################################################################


READING_MESSAGES = {
    43: {
        "d1": "፯ ዝቅ ሮሜ ም. ፯ ቊ. ፩ - ፲፬",
        "d2": "ጴጥሮስ ፩ ም. ፩ ቊ. ፳፩ - ፍ፡ም፡",
        "kahin": "ግብ፡ ሐዋ፡ ም. ፳፪ ቊ. ፩ - ፮",
        "wengel": "",
    },
    44: {
        "d1": "፲፪ ዘቅ `ሮሜ ም. ፲፩ ቍ. ፲፫ - ፪፭`",
        "d2": "'ራእይ ዮሐንስ ም. ፲፪ ቍ. ፲፫ - ፍ፡ም፡'",
        "kahin": "'ሐዋርያት ሥራ ም. ፲፩ ቍ. ፩ - ፲፪'",
        "wengel": "'ማቴዎስ ም. ፳፩ ቍ. ፴፫ - ፍ፡ም፡'"
    },
    #... Add messages for other weeks as needed
}






@bot.slash_command(name="readingd1")
async def readingd1(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.respond(READING_MESSAGES.get(week_number, {'d1': 'Reading message for this week is not available.'})['d1'])
    image_path = f"readings/deacon1/week{week_number}_readingd1.png"
    await ctx.respond(file=discord.File(image_path))

@bot.slash_command(name="readingd2")
async def readingd2(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.respond(READING_MESSAGES.get(week_number, {'d2': 'Reading message for this week is not available.'})['d2'])
    image_path = f"readings/deacon2/week{week_number}_readingd2.png"
    await ctx.respond(file=discord.File(image_path))

@bot.slash_command(name="readingkahin")
async def readingkahin(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.respond(READING_MESSAGES.get(week_number, {'kahin': 'Reading message for this week is not available.'})['kahin'])
    image_path = f"readings/kahin/week{week_number}_readingkahin.png"
    await ctx.respond(file=discord.File(image_path))

@bot.slash_command(name="wengel")
async def wengel(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.respond(READING_MESSAGES.get(week_number, {'wengel': 'ወንጌል for this week is not available.'})['ወንጌል'])
    image_path = f"readings/wengel/week{week_number}_wengel.png"
    if os.path.exists(image_path):
        await ctx.respond(file=discord.File(image_path))
    else:
        await ctx.respond(f"Wengel image for week {week_number} not found.")



################


class PaginatedView(View):
    def __init__(self, embeds):
        super().__init__()
        self.embeds = embeds
        self.current_page = 0
        self.total_pages = len(embeds)
        self.update_buttons()
    
    def update_buttons(self):
        self.children[0].disabled = self.current_page == 0
        self.children[1].disabled = self.current_page == self.total_pages - 1
    
    @discord.ui.button(label='◀', style=discord.ButtonStyle.primary)
    async def previous_button_callback(self, button, interaction):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @discord.ui.button(label='▶', style=discord.ButtonStyle.primary)
    async def next_button_callback(self, button, interaction):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

@bot.slash_command(name="commandpage")
async def commandpage(ctx):
    # Define your command pages here
    command_pages = [
        # discord.Embed(title="Commands Page 1", description="List of commands"),
        # discord.Embed(title="Commands Page 2", description="List of commands"), #examples
discord.Embed(title="Commands List", description="""
**ዘሰንበት**
`?misbak`
`?mezmur`

**በዓላት**
`?nextbeal`

**Music Controls - `a work in progress`**
`?join`
`?play`
`?stop`
`?leave`

**ዘሰንበት ንባብ**
`?nibabd1`
`?nibabd2`
`?nibabkahin`
`?wengel`

**Utilities**
`?help`
`?commands`
`?setweektext`
    """),
    discord.Embed(title="Commands List 2", description="More coming soon...."),
    ]
    
    view = PaginatedView(command_pages)
    await ctx.respond(embed=command_pages[0], view=view)


mahlet_recordings = {
    "ማኅሌተ ጽጌ": {
        "description": "አመ፳ወ፭ ለጥቅ ዘሣብዓይ ( ፯ ) ዓመት - ኃምሳይ ( ፭ ) ሰንበት",
        "recordings": [
            {"title": "ለወልድኪ ሕፃን", "url": "https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/5%20-%20ame%2025%20letikemt%20zesabeaye%20hamesaye%20amet/49.mp3"},
            # ... more recordings
        ],
        "transcript": """ለወልድኪ ሕፃን ዘስሙ ናዝራዊ ናዝራዊ ሕፃን/፪/
                        እምግብፅ እምግብፅ ይፄውዖ አቡሁ ራማዊ አቡሁ/፪/"""
    },
    # ... more mahlet recordings
}


@bot.slash_command(name="mahletzema")
async def mahletzema_command(ctx):
    view = PaginatedButtons()
    await ctx.respond('Choose a button:', view=view)
    
class PaginatedButtons(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_buttons(page=1)

    def add_buttons(self, page):
        self.clear_items()
        button_names = [
            "ማኅሌተ ጽጌ", "ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሳስ", 
        ]
        for i, name in enumerate(button_names, start=1):
            self.add_item(Button(label=name, custom_id=f'button_{i}', row=(i-1)//5))

    @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Update to the next set of buttons or pages
        self.add_buttons(page=2)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.red)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Update to the previous set of buttons or pages
        self.add_buttons(page=1)
        await interaction.response.edit_message(view=self)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.custom_id.startswith('button_'):
            # When a button from the first set is clicked, show the second set of buttons
            view = SecondSetOfButtons()
            await interaction.response.edit_message(content='Choose a button from the second set:', view=view)
            return False  # Return False to stop listening for interactions on this view
        return await super().interaction_check(interaction)


class SecondSetOfButtons(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_buttons()

    def add_buttons(self):
        second_set_button_names = [
            "6th ማኅሌተ ጽጌ", "Second Button 2", "Second Button 3", 
            "Second Button 4", "Second Button 5"
        ]
        for i, name in enumerate(second_set_button_names, start=1):
            self.add_item(Button(label=name, custom_id=f'second_set_button_{i}', row=(i-1)//5))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Make sure to handle the interaction here
        if interaction.custom_id.startswith('second_set_button_'):
            # Handle your interaction or update your message here
            await interaction.response.send_message("Button pressed!", ephemeral=True)
            return True  # Continue listening for interactions on this view
        return await super().interaction_check(interaction)



def create_paginated_content_for_6th_mahlet_tsige():
    # Define your sections here. Each section is a dictionary with title, description, and links.
    sections = [
        {
            "title": "መልክአ ሥላሴ",
            "description": """ሰላም ለአፉክሙ ዘማዕጾሁ ሰላም፤ 
            ጽጌያቲሁ ሥላሴ ለተዋህዶ ገዳም፤ 
            መንገለ አሐዱ አምላክ ንዋየ መጻኢት ዓለም፤ 
            ወልጡ አምልኮትየ በጸጋክሙ ፍጹም፤ 
            እምአምልኮ ጣኦት ግሉፍ አሐዱ ድርኅም።""",
            "links": [
                ("መልክእ", "link_to_መልክእ"),
                ("ጸናጽል", "link_to_ጸናጽል"),
                ("መረግድ", "link_to_መረግድ")
            ]
        },
        {
            "title": "ዚቅ",
            "description": """ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ...""",
            "links": [
                ("ቂም ዜማ", "link_to_ቂም_ዜማ"),
                ("ጸናጽል", "link_to_ጸናጽል_ዚቅ"),
                ("መረግድ", "link_to_መረግድ_ዚቅ")
            ]
        },
        {
            "title": "ዓዲ ዚቅ",
            "description": """አሠርገወ ገዳማተ ስን ፤ ...""",
            "links": [
                ("ቂም ዜማ", "link_to_ቂም_ዜማ_ዓዲ"),
                ("ጸናጽል", "link_to_ጸናጽል_ዓዲ"),
                ("መረግድ", "link_to_መረግድ_ዓዲ")
            ]
        },
        # ... more sections for additional pages as needed ...
    ]

    # Creating the embeds for each section
    embeds = []
    for section in sections:
        embed = discord.Embed(title=section["title"], description=section["description"])
        for name, url in section["links"]:
            embed.add_field(name=name, value=f"[{name}]({url})", inline=True)
        embeds.append(embed)

    return embeds


            

#     async def interaction_check(self, interaction: discord.Interaction) -> bool:
#         if interaction.custom_id.startswith('second_set_button_'):
#         # Define your paginated content here using triple-quoted strings
#             paginated_content = [
#             discord.Embed(title="አመ፪ ለኅዳር ዘሣብዓይ ( ፯ ) ዓመት - ሣድሳይ ( ፮ ) ሰንበት", description="""መልክአ ሥላሴ
# ሰላም ለአፉክሙ ዘማዕጾሁ ሰላም፤
#                            ጽጌያቲሁ ሥላሴ ለተዋህዶ ገዳም፤ መንገለ አሐዱ አምላክ ንዋየ መጻኢት ዓለም፤ ወልጡ አምልኮትየ በጸጋክሙ ፍጹም፤ 
#                           እምአምልኮ ጣኦት ግሉፍ አሐዱ ድርኅም።
#             """)
#             .add_field(name="Links", value="- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/1.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/2.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/3.mp3)"
#                         """ዚቅ
#                         ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/1.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/2.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/3.mp3)"
#                        """ዚቅ (ዓዲ)
# አሠርገወ ገዳማተ ስን ፤ በመንክር ኪን አርአያሁ ዘገብረ ፤ ሰሎሞን ጥቀ ኢለብሰ በኲሉ ክብሩ ፤ ከመ እሎን ጽጌያት ፤ ኢቀደምት ወኢደኃርት ፤ አራዛተ ሠርጕ ነሢኦሙ ፤ ኢክህሉ ከመ ክርስቶስ መዊዓ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/4.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/5.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/6.mp3)"
#                        """ማኅሌተ ጽጌ
# ኢየኃፍር ቀዊመ ቅድመ ስዕልኪ ወርኃ ጽጌረዳ አመ ኃልቀ፤ 
# ዘኢየኃልቅ ስብሐተ እንዘ እሴብሐኪ ጥቀ፤ 
# ተአምርኪ ማርያም ከመ አጠየቀ፤ 
# ጸውዖ ስምኪ ያነሥእ ዘወድቀ፤ 
# ኃጥአኒ ይሬሲ ጻድቀ።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/7.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/8.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/9.mp3)"
#                        """ዚቅ
# እለ ትነብሩ ተንሥኡ፤ ወእለ ታረምሙ አውሥኡ፤ ማርያምሃ በቃለ ስብሐት ጸውኡ፤ ቁሙ ወአጽምዑ ተአምረ ድንግል ከመ ትስምዑ፤ ጸልዩ ቅድመ ስዕላ ለቅድስት ድንግል፤ መርዓተ አብ ወእመ በግዑ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/14.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/15.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/16.mp3)"
#                        """ማኅሌተ ጽጌ
# እንዘ ተሐቅፊዮ ለሕፃንኪ ጽጌ ፀዓዳ ወቀይሕ፤ 
# አመ ቤተ መቅደስ ቦእኪ በዕለተ ተአምር ወንጽሕ፤ 
# ንዒ ርግብየ ትናዝዝኒ እምላህ፤ 
# ወንዒ ሠናይትየ ምስለ ገብርኤል ፍሡሕ፤ 
# ወሚካኤል ከማኪ ርኅሩኅ።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/19.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/20.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/21.mp3)"
#                        """ዘቅ 
# ንዒ ርግብየ ወንዒ ሠናይትየ ፤ እንተ ሐዋርያት ይሴብሑኪ ፤ መላእክት ይትለአኩኪ ፤ ፃዒ እምሊባኖስ ስነ ሕይወት።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/24.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/25.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/26.mp3)"
#                        """ዚቅ (ዓዲ)
# ንዒ ኀቤየ ኦ ድንግል ምስለ ኲሎሙ መላእክት፤ ከመ ታዕርጊ ጸሎተነ ጊዜ መንፈቀ ሌሊት።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/27.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/28.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/29.mp3)"
#                        """ማኅሌተ ጽጌ
# ሰዊተ ሥርናዩ ለታዴዎስ ወለበርተሎሜዎስ ወይኑ፤ 
# እንተ ጸገይኪ አስካለ በዕለተ ተከልኪ እደ የማኑ፤ 
# ማርያም ለጴጥሮስ ጽላሎቱ ወለጳውሎስ ሰበኑ፤ 
# ብኪ ምውታን ሕያዋነ ኮኑ፤ 
# ወሐዋርያት መላእክተ በሰማይ ኮነኑ።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/30.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/31.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/32.mp3)"
#                        """ዚቅ
# ኦ መድኃኒት ለነገሥት፤ ማኅበረ ቅዱሳን የዓውዱኪ፤ ነቢያት የዓኲቱኪ፤ ወሐዋርያት ይሴብሑኪ፤ እስመ ኪያኪ ኀቤ ለታዕካሁ ከመ ትኲኒዮሙ ማኅደረ፤ መላእክት ይኬልሉኪ፤ ጻድቃን ይባርኩኪ፤ አበው ይገንዩ ለኪ፤ እስመ ኪያኪ ኀቤ ለታዕካሁ ከመ ትኲኒዮሙ ማኅደረ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/36.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/37.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/38.mp3)"
#                         """ማኅሌተ ጽጌ
# ክበበ ጌራ ወርቅ ጽሩይ እምዕንቌ ባሕርይ ዘየኀቱ፤ 
# ዘተጽሕፈ ብኪ ትእምርተ ስሙ ወተዝካረ ሞቱ፤ 
# አክሊለ ጽጌ ማርያም ለጊዮርጊስ ቀጸላ መንግሥቱ፤ 
# አንቲ ኲሎ ታሰግዲ ሎቱ፤ 
# ወለኪኒ ይሰግድ ውእቱ።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/39.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/40.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/41.mp3)" 
#                         """ዚቅ
# ውድስት አንቲ በአፈ ነቢያት፤ ወስብሕት በሐዋርያት፤ አክሊለ በረከቱ ለያዕቆብ፤ ወትምክሕተ ቤቱ ለ፳ኤል።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/44.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/45.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/46.mp3)" 
#                         """ማኅሌተ ጽጌ
# ኅብረ ሐመልሚል ቀይሕ ወፀዓድዒድ አርአያ ኮስኮስ ዘብሩር፤ 
# ተአምርኪ ንፁሕ በአምሳለ ወርቅ ግቡር፤ 
# ተፈጸመ ናሁ ማኅሌተ ጽጌ ሥሙር፤ 
# አስምኪ ቦቱ ንግሥተ ሰማያት ወምድር፤ 
# ከመ በሕጽንኪ ያሰምክ ፍቁር።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/48.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/49.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/50.mp3)" 
#                         """ዚቅ
# ሃሌ ሃሌ ሉያ፤ ሃሌ ሉያ፤ ጥቀ አዳም መላትኅኪ ከመ ማዕነቅ፤ ይግበሩ ለኪ ኮስኮሰ ወርቅ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/54.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/55.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/56.mp3)" 
#                         """ሰቆቃወ ድንግል
# ተመየጢ እግዝእትየ ሀገረኪ ናዝሬተ፤ 
# ወኢትጎንድዪ በግብጽ ከመ ዘአልብኪ ቤተ፤ 
# በላዕሌኪ አልቦ እንተ ያመጽእ ሁከተ፤ 
# ለወልድኪ ዘየኃሥሦ ይእዜሰ ሞተ፤ 
# በከመ ነገሮ መልአክ ለዮሴፍ ብሥራተ።\n"""
#                        "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/58.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/59.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/60.mp3)" 
#                        """ዚቅ
# ሃሌ ሉያ፤ ተመየጢ ተመየጢ ሰላመ ሰጣዊት፤ ወንርዓይ ብኪ ሰላመ፤ ምንተኑ ትኔጽሩ በእንተ ሰላመ ሰጣዊት፤ እንተ ትሔውጽ እምርኁቅ፤ ከመ መድብለ ማኅበር ሑረታቲሀ ዘበስን ለወለተ አሚናዳብ።\n"""
#                        "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/63.mp3)\n"
#                        "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/64.mp3)\n"
#                        "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/65.mp3)", inline=False),
#                     #    """ዚቅ
#                     #     ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
#                     #    "- [New Link 1](https://example.com/new1)\n"
#                     #    "- [New Link 2](https://example.com/new2)\n"
#                     #    "- [New Link 3](https://example.com/new3)"
#                     #    """ዚቅ
#                     #     ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
#                     #    "- [New Link 1](https://example.com/new1)\n"
#                     #    "- [New Link 2](https://example.com/new2)\n"
#                     #    "- [New Link 3](https://example.com/new3)" , inline=False),
#             discord.Embed(title="Page 2", description="""This is some content for page 2.
#             Again, you can write a lot of text here.
#             Just keep adding lines and they will appear.""")
#             .add_field(name="Links", value="[Link 1](https://example.com/1)\n[Link 2](https://example.com/2)\n[Link 3](https://example.com/3)", inline=False),
#             # Add more pages as needed
#         ]
#         view = PaginatedView(paginated_content)
#         await interaction.response.edit_message(content='Navigating pages:', embed=paginated_content[0], view=view)
#         return False
#         return await super().interaction_check(interaction)

class PaginatedView(View):
    def __init__(self, embeds):
        super().__init__()
        self.embeds = embeds
        self.current_page = 0
        self.total_pages = len(embeds)
        self.update_buttons()
    
    def update_buttons(self):
        self.children[0].disabled = self.current_page == 0
        self.children[1].disabled = self.current_page == self.total_pages - 1
    
    @discord.ui.button(label='◀', style=discord.ButtonStyle.primary)
    async def previous_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @discord.ui.button(label='▶', style=discord.ButtonStyle.primary)
    async def next_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)


# class SecondSetOfButtons(View):
#     def __init__(self):
#         super().__init__(timeout=60)
#         self.add_buttons()

#     def add_buttons(self):
#         # Add your second set of buttons here
#         for i in range(1, 6):
#             self.add_item(Button(label=f'Second Set Button {i}', custom_id=f'second_set_button_{i}', row=i//5))

#     async def interaction_check(self, interaction: discord.Interaction) -> bool:
#         if interaction.custom_id.startswith('second_set_button_'):
#             # Define your paginated text pages here
#             pages = [
#                 "This is the content of page 1",
#                 "This is the content of page 2",
#                 "This is the content of page 3",
#                 # Add more pages as needed
#             ]
#             view = PaginatedTextView(pages)
#             await interaction.response.edit_message(content=pages[0], view=view)
#             return False  # Return False to stop listening for interactions on this view
#         return await super().interaction_check(interaction)

# class PaginatedTextView(View):
#     def __init__(self, pages):
#         super().__init__(timeout=60)
#         self.pages = pages
#         self.current_page = 0
#         self.update_content()

#     def update_content(self):
#         self.children[1].label = f'Page {self.current_page + 1}/{len(self.pages)}'
#         self.children[1].disabled = False
#         if self.current_page == 0:
#             self.children[0].disabled = True
#         else:
#             self.children[0].disabled = False

#         if self.current_page == len(self.pages) - 1:
#             self.children[2].disabled = True
#         else:
#             self.children[2].disabled = False

#     @discord.ui.button(label='Previous', style=discord.ButtonStyle.red)
#     async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.current_page -= 1
#         self.update_content()
#         await interaction.response.edit_message(content=self.pages[self.current_page], view=self)

#     @discord.ui.button(label='Page 1/x', style=discord.ButtonStyle.grey, disabled=True)
#     async def page_number(self, interaction: discord.Interaction, button: discord.ui.Button):
#         pass  # This button is just for displaying the page number

#     @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
#     async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.current_page += 1
#         self.update_content()
#         await interaction.response.edit_message(content=self.pages[self.current_page], view=self)


bot.run(TOKEN)