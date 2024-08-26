# import discord
# from discord.ext import commands
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'
# GUILD_ID = '970490174565928960'
# CHANNEL_ID = '970857256251953162'

# # Path to the images directory
# IMAGE_PATH = r"C:\Users\nahom\OneDrive\Documents\gradle-8.2.1-all\images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def misbak(ctx):
#     week_number = datetime.now().isocalendar()[1]  # Week starts from 1
#     image_file_path = os.path.join(IMAGE_PATH, f"week{week_number}.png")  # Assuming PNG format
    
#     if os.path.exists(image_file_path):
#         await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No image available for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)



# import discord
# from discord.ext import commands
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '972131288251240579'
# CHANNEL_ID = '970857256251953162'

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"],
#     # ... add paths for other weeks
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\gradle-8.2.1-all\images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def misbak(ctx):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No images available for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)

# import discord
# from discord.ext import commands
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"],
#     # ... add paths for other weeks
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\gradle-8.2.1-all\images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)


# import discord
# from discord.ext import commands
# from interactions import SlashCommand, SlashContext
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"],
#     # ... add paths for other weeks
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\gradle-8.2.1-all\images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
# slash = SlashCommand(bot, sync_commands=True)  # Initialize SlashCommand support

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# # Traditional command for misbak
# @bot.command()
# async def misbak(ctx):
#     await handle_misbak(ctx)

# # Slash command for misbak
# @slash.slash(name="misbak", description="Send the misbak image and text for the current week.")
# async def _misbak_slash(ctx: SlashContext):
#     await handle_misbak(ctx)

# async def handle_misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel.")
#         return

#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No images available for this week.')

# # Traditional command for setweektext
# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     await handle_setweektext(ctx, week_number, text)

# # Slash command for setweektext
# @slash.subcommand(base="set", name="weektext", description="Set the text for a specific week.", 
#                   options=[
#                       {
#                           "name": "week_number",
#                           "description": "The week number (1-52).",
#                           "type": 4,
#                           "required": True
#                       },
#                       {
#                           "name": "text",
#                           "description": "The text for the week.",
#                           "type": 3,
#                           "required": True
#                       }
#                   ])
# async def _setweektext_slash(ctx: SlashContext, week_number: int, text: str):
#     await handle_setweektext(ctx, week_number, text)

# async def handle_setweektext(ctx, week_number, text):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)




# from interactions import CommandContext, CommandClient
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"],
#     # ... add paths for other weeks
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Path\To\Your\Images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = CommandClient(prefix='?')


# @bot.slash(name="misbak", description="Send the misbak image and text for the current week.")
# async def misbak(ctx):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=image_file_path)
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No images available for this week.')

# @bot.slash(name="setweektext", description="Set the text for a specific week.")
# async def setweektext(ctx, week_number: int, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.start(TOKEN)

# ___________________________________________________________________

# import discord
# from discord.ext import commands
# from discord import Interaction
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"], 
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# # BASE_IMAGE_DIR = "/root/bot/yaredbot/images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# from asyncio import tasks


# def to_ethiopian_date(gregorian_date):
#     # Subtract 8 years to get the Ethiopian year
#     ethiopian_year = gregorian_date.year - 8
    
#     # Offsets for each month
#     month_offsets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 10]
    
#     # Adjust for leap year
#     if gregorian_date.year % 4 == 0:
#         month_offsets[11] = 11
#         month_offsets[12] = 11
    
#     # Determine the Ethiopian month and day
#     if gregorian_date.month == 1 or gregorian_date.month == 2:
#         ethiopian_month = gregorian_date.month + 10
#         ethiopian_day = gregorian_date.day
#     else:
#         ethiopian_month = gregorian_date.month - 2
#         ethiopian_day = gregorian_date.day + month_offsets[gregorian_date.month]
#         if ethiopian_day > 30:
#             ethiopian_day -= 30
#             ethiopian_month += 1

#     return ethiopian_day, ethiopian_month, ethiopian_year

# def arabic_to_geez(num):
#     geez_numerals = ["፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲"]
#     if num < 10:
#         return geez_numerals[num - 1]
#     elif num < 100:
#         tens, remainder = divmod(num, 10)
#         return geez_numerals[tens - 1] + "፲" + (geez_numerals[remainder - 1] if remainder else "")
#     else:
#         return "፻"  # For numbers from 100 to 999, we only handle 100 for simplicity

# ethiopian_months = [
#     "ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜን", "ማስቅረም", "ጥቅምት", "ህዳር", "ጳጉሜ"
# ]

# @tasks.loop(hours=24)
# async def update_channel_name():
#     voice_channel_name = to_ethiopian_date_amharic(datetime.now())
#     guild = discord.utils.get(bot.guilds, id=GUILD_ID)
#     voice_channel = discord.utils.get(guild.voice_channels, name=voice_channel_name)
#     if not voice_channel:  # If the voice channel with the current Ethiopian date doesn't exist
#         voice_channel = discord.utils.get(guild.voice_channels, name="YOUR_CURRENT_VOICE_CHANNEL_NAME")  # Replace with a known voice channel name
#     await voice_channel.edit(name=voice_channel_name)

# above is the workin script




# import discord
# from discord.ext import commands
# from discord import Interaction
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png"], #"week1_image2.png"],
#     2: ["week2_image1.png"],
#     3: ["week3_image1.png"],
#     4: ["week4_image1.png"],
#     5: ["week5_image1.png"],
#     6: ["week6_image1.png"],
#     7: ["week7_image1.png"],
#     8: ["week8_image1.png"],
#     9: ["week9_image1.png"],
#     10: ["week10_image1.png"],
#     11: ["week11_image1.png"],
#     12: ["week12_image1.png"],
#     13: ["week13_image1.png"],
#     14: ["week14_image1.png"],
#     15: ["week15_image1.png"],
#     16: ["week16_image1.png"],
#     17: ["week17_image1.png"],
#     18: ["week18_image1.png"],
#     19: ["week19_image1.png"],
#     20: ["week20_image1.png"],
#     21: ["week21_image1.png"],
#     22: ["week22_image1.png"],
#     23: ["week23_image1.png"],
#     24: ["week24_image1.png"],
#     25: ["week25_image1.png"],
#     26: ["week26_image1.png"],
#     27: ["week27_image1.png"],
#     28: ["week28_image1.png"],
#     29: ["week29_image1.png"],
#     30: ["week30_image1.png"],
#     31: ["week31_image1.png"],
#     32: ["week32_image1.png"],
#     33: ["week33_image1.png"],
#     34: ["week34_image1.png"],
#     35: ["week35_image1.png"],
#     36: ["week36_image1.png"],
#     37: ["week37_image1.png"],
#     38: ["week38_image1.png"],
#     39: ["week39_image1.png"],
#     40: ["week40_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"],
#     46: ["week46_image1.png"],
#     47: ["week47_image1.png"],
#     48: ["week48_image1.png"],
#     49: ["week49_image1.png"],
#     50: ["week50_image1.png"],
#     51: ["week51_image1.png"],
#     52: ["week52_image1.png"],
# }

# MEZMUR_PATHS = {
#     43: ["week43.txt"],
#     44: ["week44.txt"],
#     45: ["week45.txt"],
#     46: ["week46.txt"],
    
# }


# # Base directory where all images are stored
# #BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
# BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"
# #BASE_MEZMUR_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\mezmurs"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())


# SPECIFIC_CHANNEL_ID = '972131288251240579'  # Channel where bot reacts to new images

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.event
# async def on_message(message):
#     # Ignore messages sent by the bot itself
#     if message.author == bot.user:
#         return

#     # Check if the message is in the specified channel
#     if str(message.channel.id) == SPECIFIC_CHANNEL_ID:
#         # Check if the message has attachments
#         if message.attachments:
#             # Now call the logic you have in your ?misbak command
#             await send_weekly_images(message.channel)

#     # Ensure other bot commands still get processed
#     await bot.process_commands(message)

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     await send_weekly_images(ctx.channel)

# async def send_weekly_images(channel):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await channel.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await channel.send(week_texts[week_number])
#     else:
#         await channel.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# @bot.command()
# async def mezmur(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]

#     if week_number in MEZMUR_PATHS:
#         for mezmur_file in MEZMUR_PATHS[week_number]:
#             file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)
#             if os.path.exists(file_path):
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     content = file.read()
#                     await ctx.send(content)
#             else:
#                 await ctx.send(f'Mezmur file for week {week_number} not found.')
#     else:
#         await ctx.send('No mezmur set for this week.')
#         print(f"Trying to access file at: {file_path}")

        


# bot.run(TOKEN)

# __________________________________________________

# import interactions
# import discord
# from discord.ext import commands
# from interactions import SlashCommand  # Replace with the actual library you choose
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'your_token_here'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063']  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png", "week1_image2.png"],
#     2: ["week2_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"], 
# }

# # Base directory where all images are stored
# BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\gradle-8.2.1-all\images"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
# slash = SlashCommand(bot, sync_commands=True)  # Replace with the actual initialization if it's different

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @slash.slash(name="misbak")  # Slash command decorator
# async def _misbak(ctx):
#     # Your command logic here
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await ctx.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await ctx.send(week_texts[week_number])
#     else:
#         await ctx.send('No ምስባክ set for this week.')

# @slash.slash(
#     name="setweektext",
#     options=[  # Define command options for arguments
#         {
#             "name": "week_number",
#             "description": "The week number",
#             "type": 4,  # Type 4 corresponds to INTEGER
#             "required": True
#         },
#         {
#             "name": "text",
#             "description": "The text to set for the specified week",
#             "type": 3,  # Type 3 corresponds to STRING
#             "required": True
#         }
#     ]
# )
# async def _setweektext(ctx, week_number: int, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# bot.run(TOKEN)


#_________________________________________________________

# import discord
# from datetime import datetime
# import os

# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  
# GUILD_ID = '970490174565928960'
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]
# IMAGE_PATHS = {
#      1: ["week1_image1.png", "week1_image2.png"],
#      2: ["week2_image1.png"],
#      41: ["week41_image1.png", "week41_image2.png"], 
#      42: ["week42_image1.png"], 
#      43: ["week43_image1.png"], 
#      44: ["week44_image1.png"], 
#      45: ["week45_image1.png"], 
#     # ... add paths for other weeks
# }
# BASE_IMAGE_DIR = r"C:\Path\To\Your\Images"
# week_texts = {}

# intents = discord.Intents.default()
# intents.message_content = True

# bot = discord.Bot(intents=intents, slash_commands=True)  # Enabling slash_commands

# @bot.event
# async def on_ready():
#     await bot.wait_until_ready()
#     await bot.change_presence(status=discord.Status.online)
#     print(f'We have logged in as {bot.user}')

# @bot.slash_command(name="misbak", description="Send the misbak image and text for the current week.")
# async def misbak(ctx):
#     # Your misbak handling logic here...
#     pass  # Replace with your actual logic

# @bot.slash_command(name="setweektext", description="Set the text for a specific week.")
# async def setweektext(ctx, week_number: int, text: str):
#     # Your setweektext handling logic here...
#     pass  # Replace with your actual logic

# bot.run(TOKEN)

#########################################################################################################################################################################################
# import discord
# from discord.ext import commands
# from discord import FFmpegPCMAudio
# from discord import Interaction
# from datetime import datetime
# import os

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png"], #"week1_image2.png"],
#     2: ["week2_image1.png"],
#     3: ["week3_image1.png"],
#     4: ["week4_image1.png"],
#     5: ["week5_image1.png"],
#     6: ["week6_image1.png"],
#     7: ["week7_image1.png"],
#     8: ["week8_image1.png"],
#     9: ["week9_image1.png"],
#     10: ["week10_image1.png"],
#     11: ["week11_image1.png"],
#     12: ["week12_image1.png"],
#     13: ["week13_image1.png"],
#     14: ["week14_image1.png"],
#     15: ["week15_image1.png"],
#     16: ["week16_image1.png"],
#     17: ["week17_image1.png"],
#     18: ["week18_image1.png"],
#     19: ["week19_image1.png"],
#     20: ["week20_image1.png"],
#     21: ["week21_image1.png"],
#     22: ["week22_image1.png"],
#     23: ["week23_image1.png"],
#     24: ["week24_image1.png"],
#     25: ["week25_image1.png"],
#     26: ["week26_image1.png"],
#     27: ["week27_image1.png"],
#     28: ["week28_image1.png"],
#     29: ["week29_image1.png"],
#     30: ["week30_image1.png"],
#     31: ["week31_image1.png"],
#     32: ["week32_image1.png"],
#     33: ["week33_image1.png"],
#     34: ["week34_image1.png"],
#     35: ["week35_image1.png"],
#     36: ["week36_image1.png"],
#     37: ["week37_image1.png"],
#     38: ["week38_image1.png"],
#     39: ["week39_image1.png"],
#     40: ["week40_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"],
#     46: ["week46_image1.png"],
#     47: ["week47_image1.png"],
#     48: ["week48_image1.png"],
#     49: ["week49_image1.png"],
#     50: ["week50_image1.png"],
#     51: ["week51_image1.png"],
#     52: ["week52_image1.png"],
# }

# MEZMUR_PATHS = {
#     43: ["week43.txt"],
#     44: ["week44.txt"],
#     45: ["week45.txt"],
#     46: ["week46.txt"],
    
# }


# # Base directory where all images are stored
# #BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
# BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"
# #BASE_MEZMUR_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\mezmurs"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())


# SPECIFIC_CHANNEL_ID = '972131288251240579'  # Channel where bot reacts to new images

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# @bot.event
# async def on_message(message):
#     # Ignore messages sent by the bot itself
#     if message.author == bot.user:
#         return

#     # Check if the message is in the specified channel
#     if str(message.channel.id) == SPECIFIC_CHANNEL_ID:
#         # Check if the message has attachments
#         if message.attachments:
#             # Now call the logic you have in your ?misbak command
#             await send_weekly_images(message.channel)

#     # Ensure other bot commands still get processed
#     await bot.process_commands(message)

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     await send_weekly_images(ctx.channel)

# async def send_weekly_images(channel):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await channel.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await channel.send(week_texts[week_number])
#     else:
#         await channel.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# @bot.command()
# async def mezmur(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]

#     if week_number in MEZMUR_PATHS:
#         for mezmur_file in MEZMUR_PATHS[week_number]:
#             file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)
#             if os.path.exists(file_path):
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     content = file.read()
#                     await ctx.send(content)
#             else:
#                 await ctx.send(f'Mezmur file for week {week_number} not found.')
#     else:
#         await ctx.send('No mezmur set for this week.')
#         print(f"Trying to access file at: {file_path}")

# # url vc join
# @bot.command()
# async def join(ctx):
#     """Join the voice channel."""
#     channel = ctx.author.voice.channel
#     await channel.connect()

# @bot.command()
# async def leave(ctx):
#     """Leave the voice channel."""
#     await ctx.voice_client.disconnect()

# @bot.command()
# async def play(ctx, url: str):
#     """Play audio from a direct link."""
#     if not ctx.voice_client:
#         await ctx.author.voice.channel.connect()
#     ctx.voice_client.play(FFmpegPCMAudio(executable="ffmpeg", source=url))

# @bot.command()
# async def stop(ctx):
#     """Stop audio playback."""
#     if ctx.voice_client:
#         ctx.voice_client.stop()    



# READING_MESSAGES = {
#     43: {
#         "d1": "፯ ዝቅ ሮሜ ም. ፯ ቊ. ፩ - ፲፬",
#         "d2": "ጴጥሮስ ፩ ም. ፩ ቊ. ፳፩ - ፍ፡ም፡",
#         "kahin": "ግብ፡ ሐዋ፡ ም. ፳፪ ቊ. ፩ - ፮"
#     },
#     44: {
#         "d1": "Text for week2 reading d1",
#         "d2": "Text for week2 reading d2",
#         "kahin": "Text for week2 reading kahin"
#     },
#     #... Add messages for other weeks as needed
# }


# @bot.command(name='nibabd1')
# async def readingd1(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d1': 'Reading message for this week is not available.'})['d1'])
#     image_path = f"readings/deacon1/week{week_number}_readingd1.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabd2')
# async def readingd2(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d2': 'Reading message for this week is not available.'})['d2'])
#     image_path = f"readings/deacon2/week{week_number}_readingd2.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabkahin')
# async def readingkahin(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'kahin': 'Reading message for this week is not available.'})['kahin'])
#     image_path = f"readings/kahin/week{week_number}_readingkahin.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='wengel')
# async def wengel(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     image_path = f"readings/wengel/week{week_number}_wengel.png"
#     if os.path.exists(image_path):
#         await ctx.send(file=discord.File(image_path))
#     else:
#         await ctx.send(f"Wengel image for week {week_number} not found.")

# bot.run(TOKEN)


##########################################################################################################################################

# import discord
# from discord.ext import commands, tasks
# from discord import FFmpegPCMAudio
# from discord import Interaction
# from datetime import datetime
# from datetime import datetime, timedelta
# import pytz
# import os
# import asyncio
# from discord.ui import View, Button
# from discord import Embed
# import math

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png"], #"week1_image2.png"],
#     2: ["week2_image1.png"],
#     3: ["week3_image1.png"],
#     4: ["week4_image1.png"],
#     5: ["week5_image1.png"],
#     6: ["week6_image1.png"],
#     7: ["week7_image1.png"],
#     8: ["week8_image1.png"],
#     9: ["week9_image1.png"],
#     10: ["week10_image1.png"],
#     11: ["week11_image1.png"],
#     12: ["week12_image1.png"],
#     13: ["week13_image1.png"],
#     14: ["week14_image1.png"],
#     15: ["week15_image1.png"],
#     16: ["week16_image1.png"],
#     17: ["week17_image1.png"],
#     18: ["week18_image1.png"],
#     19: ["week19_image1.png"],
#     20: ["week20_image1.png"],
#     21: ["week21_image1.png"],
#     22: ["week22_image1.png"],
#     23: ["week23_image1.png"],
#     24: ["week24_image1.png"],
#     25: ["week25_image1.png"],
#     26: ["week26_image1.png"],
#     27: ["week27_image1.png"],
#     28: ["week28_image1.png"],
#     29: ["week29_image1.png"],
#     30: ["week30_image1.png"],
#     31: ["week31_image1.png"],
#     32: ["week32_image1.png"],
#     33: ["week33_image1.png"],
#     34: ["week34_image1.png"],
#     35: ["week35_image1.png"],
#     36: ["week36_image1.png"],
#     37: ["week37_image1.png"],
#     38: ["week38_image1.png"],
#     39: ["week39_image1.png"],
#     40: ["week40_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"],
#     46: ["week46_image1.png"],
#     47: ["week47_image1.png"],
#     48: ["week48_image1.png"],
#     49: ["week49_image1.png"],
#     50: ["week50_image1.png"],
#     51: ["week51_image1.png"],
#     52: ["week52_image1.png"],
# }

# MEZMUR_PATHS = {
#     43: ["week43.txt"],
#     44: ["week44.txt"],
#     45: ["week45.txt"],
#     46: ["week46.txt"],
    
# }


# # Base directory where all images are stored
# #BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
# BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"
# #BASE_MEZMUR_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\mezmurs"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())


# SPECIFIC_CHANNEL_ID = '972131288251240579'  # Channel where bot reacts to new images

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# # rich presence
# @bot.event
# async def on_ready():
#     print(f'We have logged in as {bot.user}')
    
#     # Set the rich presence
#     activity = discord.Game(name="ጸናጽል", type=0)  # Type 3 is "Watching" 0=playing 1=streaming 2=listening 3=watching 4=custom(notforbot) 5=competing
#     await bot.change_presence(status=discord.Status.online, activity=activity) 

# @bot.event
# async def on_ready():
#     print(f'We have logged in as {bot.user}')
    
#     # Set the rich presence with an image
#     activity = discord.Activity(name="ጸናጽል", type=discord.ActivityType.playing, large_image="tsenatsil_silver")
#     await bot.change_presence(activity=activity)
# # end of rich presence

# @bot.event
# async def on_message(message):
#     # Ignore messages sent by the bot itself
#     if message.author == bot.user:
#         return

#     # Check if the message is in the specified channel
#     if str(message.channel.id) == SPECIFIC_CHANNEL_ID:
#         # Check if the message has attachments
#         if message.attachments:
#             # Now call the logic you have in your ?misbak command
#             await send_weekly_images(message.channel)

#     # Ensure other bot commands still get processed
#     await bot.process_commands(message)

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     await send_weekly_images(ctx.channel)

# async def send_weekly_images(channel):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await channel.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await channel.send(week_texts[week_number])
#     else:
#         await channel.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# @bot.command()
# async def mezmur(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]

#     if week_number in MEZMUR_PATHS:
#         for mezmur_file in MEZMUR_PATHS[week_number]:
#             file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)
#             if os.path.exists(file_path):
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     content = file.read()
#                     await ctx.send(content)
#             else:
#                 await ctx.send(f'Mezmur file for week {week_number} not found.')
#     else:
#         await ctx.send('No mezmur set for this week.')
#         print(f"Trying to access file at: {file_path}")

# # url vc join
# @bot.command()
# async def join(ctx):
#     """Join the voice channel."""
#     channel = ctx.author.voice.channel
#     await channel.connect()

# @bot.command()
# async def leave(ctx):
#     """Leave the voice channel."""
#     await ctx.voice_client.disconnect()

# @bot.command()
# async def play(ctx, url: str):
#     """Play audio from a direct link."""
#     if not ctx.voice_client:
#         await ctx.author.voice.channel.connect()
#     ctx.voice_client.play(FFmpegPCMAudio(executable="ffmpeg", source=url))

# @bot.command()
# async def stop(ctx):
#     """Stop audio playback."""
#     if ctx.voice_client:
#         ctx.voice_client.stop()    


# # NEXT MAHLET (BEAL) COMMAND
# mahlets = [
#     {"date": "2023-11-05", "channel_id": 974280014390501376, "description": "ማኅሌተ ጽጌ"},
#     {"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
#     # Add more mahlets as needed
# ]

# # ... (your existing bot code) ...

# # Updated Command: ?nextbeal (previously ?nextmahlet)
# @bot.command(name="nextbeal")
# async def next_beal(ctx):
#     # Get the current date and time
#     now = datetime.now(pytz.UTC)
    
#     # Find the next mahlet (beal)
#     next_mahlet = None
#     for mahlet in mahlets:
#         mahlet_date = datetime.strptime(mahlet["date"], "%Y-%m-%d").replace(tzinfo=pytz.UTC)
#         if mahlet_date > now:
#             next_mahlet = mahlet
#             break
    
#     # If a next mahlet (beal) is found, send a message with a link to the specified channel
#     if next_mahlet:
#         channel = bot.get_channel(next_mahlet["channel_id"])
#         if channel:
#             await ctx.send(f"{next_mahlet['date']} in {channel.mention}. {next_mahlet['description']}")
#         else:
#             await ctx.send("The specified channel for the next beal was not found.")
#     else:
#         await ctx.send("There are no upcoming beals.")

# ############################################################################

# # DATE UPDATER
# # Voice channel IDs
# DATE_CHANNEL_ID = 1167180226451746876  # Replace with the actual channel ID
# DAY_NAME_CHANNEL_ID = 1167180947918168074  # Replace with the actual channel ID

# # Ethiopian month names
# ethiopian_months = ["የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሳስ", "ጥር"]

# # Names for each day
# day_names = [
#     "ልደታ ፤ ራጉኤል ፤ ኤልያስ", "ታዴዎስ ሐዋርያ ፤ ኢዮብ ጻድቅ", "በዓታ ማርያም ፤ ዜና ማርቆስ ፤ ነአኲቶ ለአብ",
#     "ዮሐንስ ወልደ ንጐድጓድ", "ጴጥሮስ ወጳውሎስ ፤ አቡነ ገብረ መንፈስ ቅዱስ", "ኢየሱስ ፤ ቁስቋም ፤ ቅድስት አርሴማ",
#     "ሥላሴ ፤ ፊሊሞን ፤ አብላንዮስ", "ማቴዎስ ፤ ዮልያኖስ ፤ አባ ኪሮስ", "ቶማስ ሐዋርያ ፤ አንድርያስ ሐዋርያ ፤ አውሳብዮስ ፤ አርባ ሰማዕታት",
#     "በዓለ መስቀሉ ለእግዚእነ", "ሐና ወኢያቄም ፤ ቅዱስ ፋሲለደስ ሰማዕት ፤ ቅዱስ ያሬድ", "ሚካኤል ፤ ክርስቶስ ሠመራ ፤ አባ ሳሙኤል",
#     "እግዚአብሔር አብ ፤ ቅዱስ ሩፋኤል ፤ ተዓምረ ባስልዮስ", "አቡነ አረጋዊ ፤ አባ ገብረ ክርስቶስ ፤ ድምጥያኖስ ሰማዕት", "ቂርቆስና ኢየሉጣ ፤ ስልፋኮስ", "ኪዳነ ምሕረት ፤ ሚካኤል ጳጳስ",
#     "ቅዱስ እስጢፋኖስ ፤ ሉቃስ ዘዓምደ ብርሃን ፤ አባ ግርማ", "ፊልጶስ ሐዋርያ ፤ ኤስድሮስ ሰማዕት ፤ ተክለ አልፋ ኤውስጣቴዎስ ሰማዕት", "ቅዱስ ገብርኤል ፤ አርቃዲዎስ ፤ ጎርጎርዮስ ሊቀ ጳጳስ",
# ]

# @tasks.loop(hours=24)
# async def update_voice_channels():
#     # Get the current date and time in EST and adjust for Ethiopian calendar
#     now = datetime.now(pytz.timezone('America/New_York')) - timedelta(days=11)
    
#     # Construct the new channel names
#     date_channel_name = f"{ethiopian_months[now.month-1]} {now.day}"
#     day_channel_name = day_names[now.day-1]
    
#     # Get the channels and update their names
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)
#     day_name_channel = bot.get_channel(DAY_NAME_CHANNEL_ID)

#     if date_channel:
#         await date_channel.edit(name=date_channel_name)
#     else:
#         print("Date channel not found")

#     if day_name_channel:
#         await day_name_channel.edit(name=day_channel_name)
#     else:
#         print("Day name channel not found")

# @update_voice_channels.before_loop
# async def before_update_voice_channels():
#     await bot.wait_until_ready()
#     print("Bot is ready. Starting to update voice channels.")

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')
#     print('Bot is ready. Starting to update voice channels.')
#     update_voice_channels.start()
# ###############################################################################


# READING_MESSAGES = {
#     43: {
#         "d1": "፯ ዝቅ ሮሜ ም. ፯ ቊ. ፩ - ፲፬",
#         "d2": "ጴጥሮስ ፩ ም. ፩ ቊ. ፳፩ - ፍ፡ም፡",
#         "kahin": "ግብ፡ ሐዋ፡ ም. ፳፪ ቊ. ፩ - ፮",
#         "wengel": "",
#     },
#     44: {
#         "d1": "፲፪ ዘቅ `ሮሜ ም. ፲፩ ቍ. ፲፫ - ፪፭`",
#         "d2": "'ራእይ ዮሐንስ ም. ፲፪ ቍ. ፲፫ - ፍ፡ም፡'",
#         "kahin": "'ሐዋርያት ሥራ ም. ፲፩ ቍ. ፩ - ፲፪'",
#         "wengel": "'ማቴዎስ ም. ፳፩ ቍ. ፴፫ - ፍ፡ም፡'"
#     },
#     #... Add messages for other weeks as needed
# }






# @bot.command(name='nibabd1')
# async def readingd1(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d1': 'Reading message for this week is not available.'})['d1'])
#     image_path = f"readings/deacon1/week{week_number}_readingd1.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabd2')
# async def readingd2(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d2': 'Reading message for this week is not available.'})['d2'])
#     image_path = f"readings/deacon2/week{week_number}_readingd2.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabkahin')
# async def readingkahin(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'kahin': 'Reading message for this week is not available.'})['kahin'])
#     image_path = f"readings/kahin/week{week_number}_readingkahin.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='wengel')
# async def wengel(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'wengel': 'ወንጌል for this week is not available.'})['ወንጌል'])
#     image_path = f"readings/wengel/week{week_number}_wengel.png"
#     if os.path.exists(image_path):
#         await ctx.send(file=discord.File(image_path))
#     else:
#         await ctx.send(f"Wengel image for week {week_number} not found.")



# ################


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







# bot.run(TOKEN)


# import discord
# from discord.ext import commands, tasks
# from discord import FFmpegPCMAudio
# from discord import Interaction
# from datetime import datetime
# from datetime import datetime, timedelta
# import pytz
# import os
# import asyncio
# from discord.ext import tasks, commands
# from discord.ui import View, Button
# from discord import Embed
# import math

# # Use environment variables or a config file to store these values securely
# TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'  # Always keep this secret!
# GUILD_ID = '970490174565928960'

# # Allowed channels for the misbak command
# ALLOWED_CHANNEL_IDS = ['972131288251240579', '972135810562412544', '970490175354450063',]  # Add other channel IDs as needed

# # Paths to the images for each week
# # Each week can have multiple images
# IMAGE_PATHS = {
#     1: ["week1_image1.png"], #"week1_image2.png"],
#     2: ["week2_image1.png"],
#     3: ["week3_image1.png"],
#     4: ["week4_image1.png"],
#     5: ["week5_image1.png"],
#     6: ["week6_image1.png"],
#     7: ["week7_image1.png"],
#     8: ["week8_image1.png"],
#     9: ["week9_image1.png"],
#     10: ["week10_image1.png"],
#     11: ["week11_image1.png"],
#     12: ["week12_image1.png"],
#     13: ["week13_image1.png"],
#     14: ["week14_image1.png"],
#     15: ["week15_image1.png"],
#     16: ["week16_image1.png"],
#     17: ["week17_image1.png"],
#     18: ["week18_image1.png"],
#     19: ["week19_image1.png"],
#     20: ["week20_image1.png"],
#     21: ["week21_image1.png"],
#     22: ["week22_image1.png"],
#     23: ["week23_image1.png"],
#     24: ["week24_image1.png"],
#     25: ["week25_image1.png"],
#     26: ["week26_image1.png"],
#     27: ["week27_image1.png"],
#     28: ["week28_image1.png"],
#     29: ["week29_image1.png"],
#     30: ["week30_image1.png"],
#     31: ["week31_image1.png"],
#     32: ["week32_image1.png"],
#     33: ["week33_image1.png"],
#     34: ["week34_image1.png"],
#     35: ["week35_image1.png"],
#     36: ["week36_image1.png"],
#     37: ["week37_image1.png"],
#     38: ["week38_image1.png"],
#     39: ["week39_image1.png"],
#     40: ["week40_image1.png"],
#     41: ["week41_image1.png", "week41_image2.png"], 
#     42: ["week42_image1.png"], 
#     43: ["week43_image1.png"], 
#     44: ["week44_image1.png"], 
#     45: ["week45_image1.png"],
#     46: ["week46_image1.png"],
#     47: ["week47_image1.png"],
#     48: ["week48_image1.png"],
#     49: ["week49_image1.png"],
#     50: ["week50_image1.png"],
#     51: ["week51_image1.png"],
#     52: ["week52_image1.png"],
# }

# MEZMUR_PATHS = {
#     43: ["week43.txt"],
#     44: ["week44.txt"],
#     45: ["week45.txt"],
#     46: ["week46.txt"],
    
# }


# # Base directory where all images are stored
# #BASE_IMAGE_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\images"
# BASE_IMAGE_DIR = "/root/bot/yaredbot/images"
# BASE_MEZMUR_DIR = "/root/bot/yaredbot/mezmurs"
# #BASE_MEZMUR_DIR = r"C:\Users\nahom\OneDrive\Documents\yaredbot\mezmurs"

# # Dictionary to store text for each week
# week_texts = {}

# bot = commands.Bot(command_prefix="?", intents= discord.Intents.all())


# SPECIFIC_CHANNEL_ID = '972131288251240579'  # Channel where bot reacts to new images

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

# # rich presence
# @bot.event
# async def on_ready():
#     print(f'We have logged in as {bot.user}')
    
#     # Set the rich presence
#     activity = discord.Game(name="ጸናጽል", type=0)  # Type 3 is "Watching" 0=playing 1=streaming 2=listening 3=watching 4=custom(notforbot) 5=competing
#     await bot.change_presence(status=discord.Status.online, activity=activity) 

# @bot.event
# async def on_ready():
#     print(f'We have logged in as {bot.user}')
    
#     # Set the rich presence with an image
#     activity = discord.Activity(name="ጸናጽል", type=discord.ActivityType.playing, large_image="tsenatsil_silver")
#     await bot.change_presence(activity=activity)
# # end of rich presence

# @bot.event
# async def on_message(message):
#     # Ignore messages sent by the bot itself
#     if message.author == bot.user:
#         return

#     # Check if the message is in the specified channel
#     if str(message.channel.id) == SPECIFIC_CHANNEL_ID:
#         # Check if the message has attachments
#         if message.attachments:
#             # Now call the logic you have in your ?misbak command
#             await send_weekly_images(message.channel)

#     # Ensure other bot commands still get processed
#     await bot.process_commands(message)

# @bot.command()
# async def misbak(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     await send_weekly_images(ctx.channel)

# async def send_weekly_images(channel):
#     week_number = datetime.now().isocalendar()[1]
    
#     if week_number in IMAGE_PATHS:
#         for image_file in IMAGE_PATHS[week_number]:
#             image_file_path = os.path.join(BASE_IMAGE_DIR, image_file)
#             if os.path.exists(image_file_path):
#                 await channel.send(file=discord.File(image_file_path))
        
#         # Send the text for this week if it exists
#         if week_number in week_texts:
#             await channel.send(week_texts[week_number])
#     else:
#         await channel.send('No ምስባክ set for this week.')

# @bot.command()
# async def setweektext(ctx, week_number: int, *, text: str):
#     """Set the text for a specific week."""
#     if 0 < week_number <= 52:  # Assuming 52 weeks in a year
#         week_texts[week_number] = text
#         await ctx.send(f'Text set for week {week_number}.')
#     else:
#         await ctx.send('Invalid week number.')

# @bot.command()
# async def mezmur(ctx):
#     # Check if the command is used in an allowed channel
#     if str(ctx.channel.id) not in ALLOWED_CHANNEL_IDS:
#         await ctx.send("This command can't be used in this channel. Try #bot-commands or #ሚዲያ-media")
#         return

#     week_number = datetime.now().isocalendar()[1]

#     if week_number in MEZMUR_PATHS:
#         for mezmur_file in MEZMUR_PATHS[week_number]:
#             file_path = os.path.join(BASE_MEZMUR_DIR, mezmur_file)
#             if os.path.exists(file_path):
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     content = file.read()
#                     await ctx.send(content)
#             else:
#                 await ctx.send(f'Mezmur file for week {week_number} not found.')
#     else:
#         await ctx.send('No mezmur set for this week.')
#         print(f"Trying to access file at: {file_path}")

# # url vc join
# @bot.command()
# async def join(ctx):
#     """Join the voice channel."""
#     channel = ctx.author.voice.channel
#     await channel.connect()

# @bot.command()
# async def leave(ctx):
#     """Leave the voice channel."""
#     await ctx.voice_client.disconnect()

# @bot.command()
# async def play(ctx, url: str):
#     """Play audio from a direct link."""
#     if not ctx.voice_client:
#         await ctx.author.voice.channel.connect()
#     ctx.voice_client.play(FFmpegPCMAudio(executable="ffmpeg", source=url))

# @bot.command()
# async def stop(ctx):
#     """Stop audio playback."""
#     if ctx.voice_client:
#         ctx.voice_client.stop()    


# # NEXT MAHLET (BEAL) COMMAND
# mahlets = [
#     {"date": "2023-11-05", "channel_id": 974280014390501376, "description": "ማኅሌተ ጽጌ"},
#     {"date": "2023-11-07", "channel_id": 974331886535077908, "description": "ጥቅምት መድኃኒዓለም"},
#     # Add more mahlets as needed
# ]

# # ... (your existing bot code) ...

# # Updated Command: ?nextbeal (previously ?nextmahlet)
# @bot.command(name="nextbeal")
# async def next_beal(ctx):
#     # Get the current date and time
#     now = datetime.now(pytz.UTC)
    
#     # Find the next mahlet (beal)
#     next_mahlet = None
#     for mahlet in mahlets:
#         mahlet_date = datetime.strptime(mahlet["date"], "%Y-%m-%d").replace(tzinfo=pytz.UTC)
#         if mahlet_date > now:
#             next_mahlet = mahlet
#             break
    
#     # If a next mahlet (beal) is found, send a message with a link to the specified channel
#     if next_mahlet:
#         channel = bot.get_channel(next_mahlet["channel_id"])
#         if channel:
#             await ctx.send(f"{next_mahlet['date']} in {channel.mention}. {next_mahlet['description']}")
#         else:
#             await ctx.send("The specified channel for the next beal was not found.")
#     else:
#         await ctx.send("There are no upcoming beals.")

# ############################################################################

# # DATE UPDATER
# # Voice channel IDs
# DATE_CHANNEL_ID = 1167180226451746876  # Replace with the actual channel ID
# DAY_NAME_CHANNEL_ID = 1167180947918168074  # Replace with the actual channel ID

# # Ethiopian month names
# ethiopian_months = ["የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሳስ", "ጥር"]

# # Names for each day
# day_names = [
#     "ልደታ ፤ ራጉኤል ፤ ኤልያስ", "ታዴዎስ ሐዋርያ ፤ ኢዮብ ጻድቅ", "በዓታ ማርያም ፤ ዜና ማርቆስ ፤ ነአኲቶ ለአብ",
#     "ዮሐንስ ወልደ ንጐድጓድ", "ጴጥሮስ ወጳውሎስ ፤ አቡነ ገብረ መንፈስ ቅዱስ", "ኢየሱስ ፤ ቁስቋም ፤ ቅድስት አርሴማ",
#     "ሥላሴ ፤ ፊሊሞን ፤ አብላንዮስ", "ማቴዎስ ፤ ዮልያኖስ ፤ አባ ኪሮስ", "ቶማስ ሐዋርያ ፤ አንድርያስ ሐዋርያ ፤ አውሳብዮስ ፤ አርባ ሰማዕታት",
#     "በዓለ መስቀሉ ለእግዚእነ", "ሐና ወኢያቄም ፤ ቅዱስ ፋሲለደስ ሰማዕት ፤ ቅዱስ ያሬድ", "ሚካኤል ፤ ክርስቶስ ሠመራ ፤ አባ ሳሙኤል",
#     "እግዚአብሔር አብ ፤ ቅዱስ ሩፋኤል ፤ ተዓምረ ባስልዮስ", "አቡነ አረጋዊ ፤ አባ ገብረ ክርስቶስ ፤ ድምጥያኖስ ሰማዕት", "ቂርቆስና ኢየሉጣ ፤ ስልፋኮስ", "ኪዳነ ምሕረት ፤ ሚካኤል ጳጳስ",
#     "ቅዱስ እስጢፋኖስ ፤ ሉቃስ ዘዓምደ ብርሃን ፤ አባ ግርማ", "ፊልጶስ ሐዋርያ ፤ ኤስድሮስ ሰማዕት ፤ ተክለ አልፋ ኤውስጣቴዎስ ሰማዕት", "ቅዱስ ገብርኤል ፤ አርቃዲዎስ ፤ ጎርጎርዮስ ሊቀ ጳጳስ",
# ]

# @tasks.loop(hours=24)
# async def update_voice_channels():
#     # Get the current date and time in EST and adjust for Ethiopian calendar
#     now = datetime.now(pytz.timezone('America/New_York')) - timedelta(days=11)
    
#     # Construct the new channel names
#     date_channel_name = f"{ethiopian_months[now.month-1]} {now.day}"
#     day_channel_name = day_names[now.weekday()]
    
#     # Get the channels and update their names
#     date_channel = bot.get_channel(DATE_CHANNEL_ID)
#     day_name_channel = bot.get_channel(DAY_NAME_CHANNEL_ID)

#     if date_channel:
#         await date_channel.edit(name=date_channel_name)
#     else:
#         print("Date channel not found")

#     if day_name_channel:
#         await day_name_channel.edit(name=day_channel_name)
#     else:
#         print("Day name channel not found")

# @update_voice_channels.before_loop
# async def before_update_voice_channels():
#     await bot.wait_until_ready()
#     print("Bot is ready. Starting to update voice channels.")

# async def main():
#     update_voice_channels.start()
#     await bot.start(TOKEN)

# if __name__ == "__main__":
#     asyncio.run(main())


# update_voice_channels.start()
# ###############################################################################


# READING_MESSAGES = {
#     43: {
#         "d1": "፯ ዝቅ ሮሜ ም. ፯ ቊ. ፩ - ፲፬",
#         "d2": "ጴጥሮስ ፩ ም. ፩ ቊ. ፳፩ - ፍ፡ም፡",
#         "kahin": "ግብ፡ ሐዋ፡ ም. ፳፪ ቊ. ፩ - ፮",
#         "wengel": "",
#     },
#     44: {
#         "d1": "፲፪ ዘቅ `ሮሜ ም. ፲፩ ቍ. ፲፫ - ፪፭`",
#         "d2": "'ራእይ ዮሐንስ ም. ፲፪ ቍ. ፲፫ - ፍ፡ም፡'",
#         "kahin": "'ሐዋርያት ሥራ ም. ፲፩ ቍ. ፩ - ፲፪'",
#         "wengel": "'ማቴዎስ ም. ፳፩ ቍ. ፴፫ - ፍ፡ም፡'"
#     },
#     #... Add messages for other weeks as needed
# }






# @bot.command(name='nibabd1')
# async def readingd1(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d1': 'Reading message for this week is not available.'})['d1'])
#     image_path = f"readings/deacon1/week{week_number}_readingd1.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabd2')
# async def readingd2(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'d2': 'Reading message for this week is not available.'})['d2'])
#     image_path = f"readings/deacon2/week{week_number}_readingd2.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='nibabkahin')
# async def readingkahin(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'kahin': 'Reading message for this week is not available.'})['kahin'])
#     image_path = f"readings/kahin/week{week_number}_readingkahin.png"
#     await ctx.send(file=discord.File(image_path))

# @bot.command(name='wengel')
# async def wengel(ctx):
#     week_number = (datetime.now().isocalendar()[1] - 1) % 52 + 1
#     await ctx.send(READING_MESSAGES.get(week_number, {'wengel': 'ወንጌል for this week is not available.'})['ወንጌል'])
#     image_path = f"readings/wengel/week{week_number}_wengel.png"
#     if os.path.exists(image_path):
#         await ctx.send(file=discord.File(image_path))
#     else:
#         await ctx.send(f"Wengel image for week {week_number} not found.")



# ################


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







# bot.run(TOKEN)