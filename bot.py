import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from discord import Interaction
from datetime import datetime, timedelta
import pytz
import os
import asyncio
from discord.ui import View, Button
from discord import Embed
import math
from discord.ext import tasks
import subprocess
from dotenv import load_dotenv
load_dotenv()  


subprocess.Popen(["python3", "date.py"])

import os
TOKEN = os.getenv('DISCORD_BOT_TOKEN')



# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
GUILD_ID = '970490174565928960'

# Allowed channels for the misbak command
ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063', '970857256251953162']  # Add other channel IDs as needed

# Paths to thhe images for each week
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
    18: ["week18_image1.png, week18_image2.png"],
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
    11: ["week11.txt"],





    43: ["week43.txt"],
    44: ["week44.txt"],
    45: ["week45.txt"],
    46: ["week46.txt"],
    51: ["week51.txt"],
    
}


# Base directory where all images are stored
BASE_IMAGE_DIR = r"C:\Users\nahom\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
# BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"
BASE_MEZMUR_DIR = r"C:\Users\nahom\Documents\yaredbot\mezmurs"

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
    await bot.change_presence(status=discord.Status.online, activity=activity)

    
    # Set the rich presence
    activity = discord.Game(name="ጸናጽል", type=0)  # Type 3 is "Watching" 0=playing 1=streaming 2=listening 3=watching 4=custom(notforbot) 5=competing
    await bot.change_presence(status=discord.Status.online, activity=activity) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    activity = discord.Game(name="ጸናጽል")
    await bot.change_presence(status=discord.Status.online, activity=activity)


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

    # Check if the message is in the specified channel
    if str(message.channel.id) == SPECIFIC_CHANNEL_ID:
        # Check if the message has attachments
        if message.attachments:
            # Now call the logic you have in your ?misbak command
            await send_weekly_images(message.channel)

    # Ensure other bot commands still get processed
    await bot.process_commands(message)

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     await send_weekly_images(ctx.channel)

# async def send_weekly_images(channel):
#     try:
#         week_number = datetime.now().isocalendar()[1]
        
#         if week_number in IMAGE_PATHS:
#             for image_file in IMAGE_PATHS[week_number]:
#                 image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#                 if os.path.exists(image_file_path):
#                     await channel.send(file=discord.File(image_file_path))
#             # ... rest of the code ...
#         else:
#             await channel.send('No ምስባክ set for this week.')
#     except Exception as e:
#         print(f"Error in send_weekly_images: {e}")
#         await channel.send(f"An error occurred: {e}")

@bot.command()
async def misbak(ctx):
    # Check if the command is used in an allowed channel
    if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
        await ctx.send("This command can't be used in this channel. Try #bot-commands or #media")
        return

    # Proceed with sending the weekly images
    await send_weekly_images(ctx.channel)

async def send_weekly_images(channel):
    try:
        # Get the current week number of the year
        week_number = datetime.now().isocalendar()[1]
        
        # Check if there are images set for the current week
        if week_number in IMAGE_PATHS:
            # Send all images for the current week
            for image_file in IMAGE_PATHS[week_number]:
                image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
                if os.path.exists(image_file_path):
                    await channel.send(file=discord.File(image_file_path))
        else:
            await channel.send('No image set for this week.')
    except Exception as e:
        print(f"Error in send_weekly_images: {e}")
        await channel.send(f"An error occurred: {e}")

@bot.command()
async def setweektext(ctx, week_number: int, *, text: str):
    """Set the text for a specific week."""
    if 0 < week_number <= 52:
        week_texts[week_number] = text
        await ctx.send(f'Text set for week {week_number}.')
    else:
        await ctx.send('Invalid week number.')


@bot.command()
async def mezmur(ctx):
    # Check if the command is used in an allowed channel
    if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
        await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
        return

    week_number = datetime.now().isocalendar()[1]

    if week_number in MEZMUR_PATHS:
        for mezmur_file in MEZMUR_PATHS[week_number]:
            file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    await ctx.send(content)
            else:
                await ctx.send(f'Mezmur file for week {week_number} not found.')
    else:
        await ctx.send('No mezmur set for this week.')
        print(f"Trying to access file at: {file_path}")

# url vc join
@bot.command()
async def join(ctx):
    """Join the voice channel."""
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    """Leave the voice channel."""
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, url: str):
    """Play audio from a direct link."""
    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()
    ctx.voice_client.play(FFmpegPCMAudio(executable="ffmpeg", source=url))

@bot.command()
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
@bot.command(name="nextbeal")
async def next_beal(ctx):
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
            await ctx.send(f"{next_mahlet['date']} in {channel.mention}. {next_mahlet['description']}")
        else:
            await ctx.send("The specified channel for the next beal was not found.")
    else:
        await ctx.send("There are no upcoming beals.")

############################################################################

# DATE UPDATER

# def gregorian_to_ethiopian(gregorian_date):
#     # Ethiopian New Year in Gregorian calendar
#     if gregorian_date.month < 9 or (gregorian_date.month == 9 and gregorian_date.day < 11):
#         # If before Ethiopian New Year in Gregorian calendar
#         ethiopian_year = gregorian_date.year - 8
#     else:
#         # If after Ethiopian New Year in Gregorian calendar
#         ethiopian_year = gregorian_date.year - 7

#     # New year's day in Ethiopian calendar
#     new_year_day = datetime(ethiopian_year - 1, 9, 11)
#     if (ethiopian_year - 1) % 4 == 3:  # Ethiopian leap year correction
#         new_year_day = datetime(ethiopian_year - 1, 9, 12)

#     # Calculate the difference
#     days_difference = (gregorian_date - new_year_day).days

#     # Ethiopian month and day
#     ethiopian_month = (days_difference // 30) + 1
#     ethiopian_day = (days_difference % 30) + 1

#     return ethiopian_year, ethiopian_month, ethiopian_day

# # Test with the current date
# current_date = datetime.now()
# eth_year, eth_month, eth_day = gregorian_to_ethiopian(current_date)
# eth_year, eth_month, eth_day


# def gregorian_to_julian_day_number(year, month, day):
#     a = (14 - month) // 12
#     y = year + 4800 - a
#     m = month + 12 * a - 3
#     jdn = day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045
#     return jdn

# def julian_day_number_to_ethiopian(jdn):
#     JDN_OFFSET = 1723856
#     jdn -= JDN_OFFSET
#     year = (jdn * 4 + 3) // 1461
#     jdn -= (year * 365) + (year // 4)
#     month = min((jdn * 13 + 502) // 365, 13)
#     jdn -= (month - 1) * 30
#     day = jdn + 1
#     return year, month, day

# # Current Gregorian date
# now = datetime.now()
# gregorian_year, gregorian_month, gregorian_day = now.year, now.month, now.day

# # Conversion
# jdn = gregorian_to_julian_day_number(gregorian_year, gregorian_month, gregorian_day)
# ethiopian_year, ethiopian_month, ethiopian_day = julian_day_number_to_ethiopian(jdn)

# print(f"Ethiopian Date: {ethiopian_year}-{ethiopian_month:02d}-{ethiopian_day:02d}")

# # Update the Ethiopian date channel every 24 hours
# @tasks.loop(hours=24)
# async def update_ethiopian_date_channel():
#     now = datetime.now()
#     gregorian_year, gregorian_month, gregorian_day = now.year, now.month, now.day
#     jdn = gregorian_to_julian_day_number(gregorian_year, gregorian_month, gregorian_day)
#     ethiopian_year, ethiopian_month, ethiopian_day = julian_day_number_to_ethiopian(jdn)
#     ethiopian_date_str = f"{ethiopian_year}-{ethiopian_month:02d}-{ethiopian_day:02d}"
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)  
#     if date_channel:
#         await date_channel.edit(name=f"Ethiopian Date: {ethiopian_date_str}")
#     else:
#         print("Date channel not found or ID incorrect")

# @update_ethiopian_date_channel.before_loop
# async def before_update_ethiopian_date_channel():
#     await bot.wait_until_ready()

# update_ethiopian_date_channel.start()



# @tasks.loop(hours=24)
# async def update_ethiopian_date_channel():
#     # Adjust for the specific timezone and subtract the necessary days to align with the Ethiopian calendar
#     now = datetime.datetime.now(pytz.timezone('America/New_York')) - datetime.timedelta(days=11)
#     eth_year, eth_month, eth_day = gregorian_to_ethiopian(now)
#     ethiopian_date_str = f"{eth_year}-{eth_month:02d}-{eth_day:02d}"
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)  
#     if date_channel:
#         await date_channel.edit(name=f"Ethiopian Date: {ethiopian_date_str}")
#     else:
#         print("Date channel not found or ID incorrect")

# @update_ethiopian_date_channel.before_loop
# async def before_update_ethiopian_date_channel():
#     await bot.wait_until_ready()

# @bot.event
# async def on_ready():
#     print('Bot is ready.')
#     update_voice_channels.start()  # Start the loop here, ensuring the bot's event loop is running


# @tasks.loop(hours=24)
# async def update_voice_channels():
#     now = datetime.now(pytz.timezone('Africa/Addis_Ababa'))
#     jdn = gregorian_to_julian_day_number(now.year, now.month, now.day)
#     eth_year, eth_month, eth_day = julian_day_number_to_ethiopian(jdn)

#     # Construct the new channel name based on the Ethiopian date
#     date_channel_name = f"Ethiopian Date: {eth_year}-{eth_month:02d}-{eth_day:02d}"
    
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)
#     if date_channel:
#         await date_channel.edit(name=date_channel_name)
#     else:
#         print("Date channel not found or ID incorrect")

# # Start the loop
# update_voice_channels.start()

# Voice channel IDs
DATE_CHANNEL_ID = 1167180226451746876  # Replace with the actual channel ID
DAY_NAME_CHANNEL_ID = 1167180947918168074  # Replace with the actual channel ID








       

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






@bot.command(name='nibabd1')
async def readingd1(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.send(READING_MESSAGES.get(week_number, {'d1': 'Reading message for this week is not available.'})['d1'])
    image_path = f"readings/deacon1/week{week_number}_readingd1.png"
    await ctx.send(file=discord.File(image_path))

@bot.command(name='nibabd2')
async def readingd2(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.send(READING_MESSAGES.get(week_number, {'d2': 'Reading message for this week is not available.'})['d2'])
    image_path = f"readings/deacon2/week{week_number}_readingd2.png"
    await ctx.send(file=discord.File(image_path))

@bot.command(name='nibabkahin')
async def readingkahin(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.send(READING_MESSAGES.get(week_number, {'kahin': 'Reading message for this week is not available.'})['kahin'])
    image_path = f"readings/kahin/week{week_number}_readingkahin.png"
    await ctx.send(file=discord.File(image_path))

@bot.command(name='wengel')
async def wengel(ctx):
    week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
    await ctx.send(READING_MESSAGES.get(week_number, {'wengel': 'ወንጌል for this week is not available.'})['ወንጌል'])
    image_path = f"readings/wengel/week{week_number}_wengel.png"
    if os.path.exists(image_path):
        await ctx.send(file=discord.File(image_path))
    else:
        await ctx.send(f"Wengel image for week {week_number} not found.")



########################################################################################################## in progress

class PaginatedView(discord.ui.View):
    def __init__(self, embeds_dict):
        super().__init__()
        self.embeds_dict = embeds_dict
        self.current_embeds = self.embeds_dict['wazema']
        self.current_page = 0

    def update_buttons(self):
        self.children[0].disabled = self.current_page == 0
        self.children[1].disabled = self.current_page >= len(self.current_embeds) - 1

    @discord.ui.button(label='◀', style=discord.ButtonStyle.primary)
    async def previous_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.current_embeds[self.current_page], view=self)
            self.update_buttons()

    @discord.ui.button(label='▶', style=discord.ButtonStyle.primary)
    async def next_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page < len(self.current_embeds) - 1:
            self.current_page += 1
            await interaction.response.edit_message(embed=self.current_embeds[self.current_page], view=self)
            self.update_buttons()
        else:
            await interaction.response.edit_message(content="No more pages available.", view=None)

    async def wazema_page(self, interaction: discord.Interaction):
        self.current_embeds = self.embeds_dict['wazema']
        self.current_page = 0
        await self.update_message(interaction)

    async def mahlet_page(self, interaction: discord.Interaction):
        self.current_embeds = self.embeds_dict['mahlet']
        self.current_page = 0
        await self.update_message(interaction)

    async def update_message(self, interaction: discord.Interaction):
        embed = self.current_embeds[self.current_page]
        await interaction.response.edit_message(embed=embed, view=self)
        self.update_buttons()



        def update_buttons(self):
            self.children[0].disabled = self.current_page == 0
            self.children[1].disabled = self.current_page == self.total_pages - 1
@bot.command(name='mahletzema')
async def mahletzema_command(ctx):
    initial_buttons = [
        Button(label='መስከረም', custom_id='meskerem'),
        Button(label='ጥቅምት', custom_id='tikimt'),
        Button(label='ኅዳር', custom_id='hidar'),
        Button(label='ታኅሣሥ', custom_id='tahsas'),
        Button(label='ጥር', custom_id='tir'),
        Button(label='የካቲት', custom_id='yekatit'),
        Button(label='መጋቢት', custom_id='megabit'),
        Button(label='ሚያዚያ', custom_id='miyazia'),
        Button(label='ግንቦት', custom_id='ginbot'),
        Button(label='ሰኔ', custom_id='sene'),
        Button(label='ሐምሌ', custom_id='hamle'),
        Button(label='ነሐሴ', custom_id='nehase'),
        Button(label='ጳጉሜ', custom_id='pagume'),
    ]
    view = InitialButtonsView(initial_buttons)
    await ctx.send('Choose a button:', view=view)
    
class InitialButtonsView(View):
    def __init__(self, buttons):
        super().__init__(timeout=60)
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.data['custom_id'] == 'meskerem':
            second_set_buttons = [
                Button(label='፩ ልደታ', custom_id='lidata'),
                Button(label='፲ወ፩ ቅዱስ ያሬድ', custom_id='yohanneskidusyired'),
                Button(label='፳ወ፩ ደብረ ምጥማቅ', custom_id='debremitmaq'),
            ]
        elif interaction.data['custom_id'] == 'tikimt':
            second_set_buttons = [
                Button(label='Button for Tikimt 1', custom_id='tikimt1'),
                Button(label='Button for Tikimt 2', custom_id='tikimt2'),
                Button(label='Button for Tikimt 3', custom_id='tikimt3'),
            ]
        # Add more conditions for other months and their respective second set of buttons
        else:
            return await super().interaction_check(interaction)
        
        view = SecondSetButtonsView(second_set_buttons)
        await interaction.response.edit_message(content='Choose a button from the second set:', view=view)
        return False

class SecondSetButtonsView(View):
    def __init__(self, buttons):
        super().__init__(timeout=60)
        for button in buttons:
            self.add_item(button)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.data['custom_id'].startswith('lidata'):
            embeds_dict = {
                'wazema': [
                    discord.Embed(
                        title="Wazema Page 1",
                        description="This is the content of Wazema page 1 for Lidata."
                    ),
                    discord.Embed(
                        title="Wazema Page 2",
                        description="This is the content of Wazema page 2 for Lidata."
                    ),
                ],
                'mahlet': [
                    discord.Embed(
                        title="Mahlet Page 1",
                        description="This is the content of Mahlet page 1 for Lidata."
                    ),
                    discord.Embed(
                        title="Mahlet Page 2",
                        description="This is the content of Mahlet page 2 for Lidata."
                    ),
                ]
            }
        elif interaction.data['custom_id'].startswith('yohanneskidusyired'):
            embeds_dict = {
                'wazema': [
                    discord.Embed(
                        title="Wazema Page 1",
                        description="This is the content of Wazema page 1 for Yohannes Kidus Yired."
                    ),
                    discord.Embed(
                        title="Wazema Page 2",
                        description="This is the content of Wazema page 2 for Yohannes Kidus Yired."
                    ),
                ],
                'mahlet': [
                    discord.Embed(
                        title="Mahlet Page 1",
                        description="This is the content of Mahlet page 1 for Yohannes Kidus Yired."
                    ),
                    discord.Embed(
                        title="Mahlet Page 2",
                        description="This is the content of Mahlet page 2 for Yohannes Kidus Yired."
                    ),
                ]
            }
        # Add more conditions for other buttons and their respective embeds
        else:
            return await super().interaction_check(interaction)
        
        view = PaginatedView(embeds_dict)
        await interaction.response.edit_message(content='Navigating pages:', embed=embeds_dict['wazema'][0], view=view)
        return False

# class PaginatedView(View):
#     def __init__(self, embeds):
#         super().__init__()
#         self.embeds = embeds
#         self.current_page = 0
#         self.total_pages = len(embeds)
#         self.update_buttons()
    
#     def update_buttons(self):
#         self.children[0].disabled = self.current_page == 0
#         self.children[1].disabled = self.current_page == self.total_pages - 1
    
#     @discord.ui.button(label='◀', style=discord.ButtonStyle.primary)
#     async def previous_button_callback(self, button, interaction):
#         if self.current_page > 0:
#             self.current_page -= 1
#             self.update_buttons()
#             await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

#     @discord.ui.button(label='▶', style=discord.ButtonStyle.primary)
#     async def next_button_callback(self, button, interaction):
#         if self.current_page < self.total_pages - 1:
#             self.current_page += 1
#             self.update_buttons()
#             await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

# @bot.command(name='commands')
# async def commandpage(ctx):
#     # Define your command pages here
#     command_pages = [
#         # discord.Embed(title="Commands Page 1", description="List of commands"),
#         # discord.Embed(title="Commands Page 2", description="List of commands"), #examples
# discord.Embed(title="Commands List", description="""
# **ዘሰንበት**
# `?misbak`
# `?mezmur`

# **በዓላት**
# `?nextbeal`

# **Music Controls - `a work in progress`**
# `?join`
# `?play`
# `?stop`
# `?leave`

# **ዘሰንበት ንባብ**
# `?nibabd1`
# `?nibabd2`
# `?nibabkahin`
# `?wengel`

# **Utilities**
# `?help`
# `?commands`
# `?setweektext`
#     """),
#     discord.Embed(title="Commands List 2", description="More coming soon...."),
#     ]
    
#     view = PaginatedView(command_pages)
#     await ctx.send(embed=command_pages[0], view=view)


# mahlet_recordings = {
#     "ማኅሌተ ጽጌ": {
#         "description": "አመ፳ወ፭ ለጥቅ ዘሣብዓይ ( ፯ ) ዓመት - ኃምሳይ ( ፭ ) ሰንበት",
#         "recordings": [
#             {"title": "ለወልድኪ ሕፃን", "url": "https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/5%20-%20ame%2025%20letikemt%20zesabeaye%20hamesaye%20amet/49.mp3"},
#             # ... more recordings
#         ],
#         "transcript": """ለወልድኪ ሕፃን ዘስሙ ናዝራዊ ናዝራዊ ሕፃን/፪/
#                         እምግብፅ እምግብፅ ይፄውዖ አቡሁ ራማዊ አቡሁ/፪/"""
#     },
#     # ... more mahlet recordings
# }


# @bot.command(name='mahletzema')
# async def mahletzema_command(ctx):
#     view = PaginatedButtons()
#     await ctx.send('Choose a button:', view=view)
    
# class PaginatedButtons(View):
#     def __init__(self):
#         super().__init__(timeout=60)
#         self.add_buttons(page=1)

#     def add_buttons(self, page):
#         self.clear_items()
#         button_names = [
#             "ማኅሌተ ጽጌ", "ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ", 
#         ]
#         for i, name in enumerate(button_names, start=1):
#             self.add_item(Button(label=name, custom_id=f'button_{i}', row=(i-1)//5))

#     @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
#     async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
#         # Update to the next set of buttons or pages
#         self.add_buttons(page=2)
#         await interaction.response.edit_message(view=self)

#     @discord.ui.button(label='Previous', style=discord.ButtonStyle.red)
#     async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
#         # Update to the previous set of buttons or pages
#         self.add_buttons(page=1)
#         await interaction.response.edit_message(view=self)

#     async def interaction_check(self, interaction: discord.Interaction) -> bool:
#         if interaction.custom_id.startswith('button_'):
#             # When a button from the first set is clicked, show the second set of buttons
#             view = SecondSetOfButtons()
#             await interaction.response.edit_message(content='Choose a button from the second set:', view=view)
#             return False  # Return False to stop listening for interactions on this view
#         return await super().interaction_check(interaction)


# class SecondSetOfButtons(View):
#     def __init__(self):
#         super().__init__(timeout=60)
#         self.add_buttons()

#     def add_buttons(self):
#         second_set_button_names = [
#             "6th ማኅሌተ ጽጌ", "Second Button 2", "Second Button 3", 
#             "Second Button 4", "Second Button 5"
#         ]
#         for i, name in enumerate(second_set_button_names, start=1):
#             self.add_item(Button(label=name, custom_id=f'second_set_button_{i}', row=(i-1)//5))

#     async def interaction_check(self, interaction: discord.Interaction) -> bool:
#         if interaction.custom_id.startswith('second_set_button_'):
#                         paginated_content = read_and_parse_text_file('sibketmahlet.txt')
#                         view = PaginatedView(paginated_content)
#                         await interaction.response.edit_message(content='Navigating pages:', embed=paginated_content[0], view=view)
#                         return False
#         return await super().interaction_check(interaction)
    
# def read_and_parse_text_file(file_path):
#     absolute_path = 'C:\Users\nahom\Documents\yaredbot\mahletzema\sibket\sibketmahlet.txt'  # Replace with the actual path to your file
#     with open(absolute_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#     pages = content.split('---')  # Assuming '---' is your delimiter
#     embeds = [discord.Embed(description=page) for page in pages]
#     return embeds



paginated_content = [
    discord.Embed(
        title="Some Title",
        description="This is a valid description"  # Make sure this is a non-empty string
        
    ),
    # Other embeds...
]


        # Define your paginated content here using triple-quoted strings
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
        # view = PaginatedView(paginated_content)
        # await interaction.response.edit_message(content='Navigating pages:', embed=paginated_content[0], view=view)
        # return False
        # return await super().interaction_check(interaction)


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

# import ethiopian_date as ed

# @bot.command(name='ethiopiandate')
# async def ethiopian_date_command(ctx):
#     now = datetime.now()
#     ethiopian_date = ed.to_ethiopian(now.year, now.month, now.day)
#     await ctx.send(f"Current Ethiopian Date: {ethiopian_date[0]}-{ethiopian_date[1]:02d}-{ethiopian_date[2]:02d}")

# async def update_date_channel(bot):
#     now = datetime.now()
#     ethiopian_date = ed.to_ethiopian(now.year, now.month, now.day)
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)
    
#     if date_channel:
#         new_name = f"Date: {ethiopian_date[0]}-{ethiopian_date[1]:02d}-{ethiopian_date[2]:02d}"
#         await date_channel.edit(name=new_name)


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




import discord
from discord.ext import tasks
import datetime

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)

GUILD_ID = 970490174565928960


ethiopian_months = ["ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ"]


ethiopian_day_words = {
    1: ["ልደታ", "ራጉኤል", "ኤልያስ"],
    2: ["ታዴዎስ ሐዋርያ", "ኢዮብ ጻድቅ"],
    3: ["በዓታ ማርያም", "ዜና ማርቆስ", "ነአኲቶ ለአብ"],
    4: ["ዮሐንስ ወልደ ንጐድጓድ"],
    5: ["ጴጥሮስ ወጳውሎስ", "አቡነ ገብረ መንፈስ ቅዱስ"],
    6: ["ኢየሱስ", "ቁስቋም", "ቅድስት አርሴማ"],
    7: ["ሥላሴ", "ፊሊሞን", "አብላንዮስ"],
    8: ["ማቴዎስ", "ዮልያኖስ", "አባ ኪሮስ"],
    9: ["ቶማስ ሐዋርያ", "አንድርያስ ሐዋርያ", "አውሳብዮስ", "አርባ ሰማዕታት"],
    10: ["በዓለ መስቀሉ ለእግዚእነ"],
    11: ["ሐና ወኢያቄም", "ቅዱስ ፋሲለደስ ሰማዕት", "ቅዱስ ያሬድ"],
    12: ["ሚካኤል", "ክርስቶስ ሠመራ", "አባ ሳሙኤል"],
    13: ["እግዚአብሔር አብ", "ቅዱስ ሩፋኤል", "ተዓምረ ባስልዮስ"],
    14: ["አቡነ አረጋዊ", "አባ ገብረ ክርስቶስ", "ድምጥያኖስ ሰማዕት"],
    15: ["ቂርቆስና ኢየሉጣ", "ስልፋኮስ"],
    16: ["ኪዳነ ምሕረት", "ሚካኤል ጳጳስ"],
    17: ["ቅዱስ እስጢፋኖስ", "ሉቃስ ዘዓምደ ብርሃን", "አባ ግርማ"],
    18: ["ፊልጶስ ሐዋርያ", "ኤስድሮስ ሰማዕት", "ተክለ አልፋ", "ኤውስጣቴዎስ ሰማዕት"],
    19: ["ቅዱስ ገብርኤል", "አርቃዲዎስ", "ጎርጎርዮስ ሊቀ ጳጳስ"],
    20: ["ጽንጸታ ለማርያም", "ነቢዩ ኤልሳ", "ሐጌ ነቢይ", "አባ ሰላማ መተርጉም", "ሕንጸተ አትናቴዮስ ሊቀጳጳስ"],
    21: ["ማርያም"],
    22: ["ቅዱስ ዑራኤል", "ደቅስዮስ", "ያዕቆብ ምሥራቃዊ"],
    23: ["ጊዮርጊስ", "ለጊኖስ", "ሰማዕት"],
    24: ["አቡነ ተክለ ሃይማኖት"],
    25: ["መርቆሬዎስ", "አኒፍኖስ"],
    26: ["ሆሴዕ ነቢይ", "ሳዶቅ ሰማዕት", "ቶምስ ደቀመዝሙር"],
    27: ["መድኃኔዓለም", "ሕዝቅያስ ነቢይ", "አባ ዮሐንስ"],
    28: ["አማኑኤል", "ቆስጠንጢስኖስ", "አብርሃም"],
    29: ["በዓለ ወልድ", "ሳሙኤል ዘወገግ"],
    30: ["ማርቆስ ወንጌላዊ"],
}
# Function to update the voice channels
async def update_channels():
    # Get the current date
    now = datetime.datetime.now()
    ethiopian_month = ethiopian_months[now.month - 1]
    
    # Calculate the Ethiopian day by subtracting 9 days
    ethiopian_day = now.day - 5
    if ethiopian_day <= 0:
        # Adjust if the day is in the previous month
        ethiopian_month = ethiopian_months[now.month - 2]
        ethiopian_day += 30  # Assuming Ethiopian months have 30 days which they do besides the 13th month

    # Update the voice channels
    guild = client.get_guild(GUILD_ID)
    if guild:
        for channel_id in [1167180226451746876, 1167180947918168074]:
            channel = guild.get_channel(channel_id)
            if channel:
                try:
                    if channel.id == 1167180226451746876:
                        await channel.edit(name=f"{ethiopian_month} {ethiopian_day}")
                    elif channel.id == 1167180947918168074 and ethiopian_day in ethiopian_day_words:
                        await channel.edit(name=" ".join(ethiopian_day_words[ethiopian_day]))
                except Exception as e:
                    print(f"Error updating channel {channel.name}: {e}")

# Background task to update channels every day
@tasks.loop(hours=24)
async def daily_update():
    await update_channels()

# Event handler for bot startup
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Start the daily update task
    daily_update.start()



client.run("OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw")