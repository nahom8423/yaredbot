# import discord
# from discord.ext import tasks
# import datetime


# intents = discord.Intents.default()
# intents.voice_states = True
# client = discord.Client(intents=intents)

# GUILD_ID = 970490174565928960

# # Define the Ethiopian months and corresponding words
# ethiopian_months = ["ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ"]

# # Define the words for each day of the month
# ethiopian_day_words = {
#     1: ["ልደታ", "ራጉኤል", "ኤልያስ"],
#     2: ["ታዴዎስ ሐዋርያ", "ኢዮብ ጻድቅ"],
#     3: ["በዓታ ማርያም", "ዜና ማርቆስ", "ነአኲቶ ለአብ"],
#     4: ["ዮሐንስ ወልደ ንጐድጓድ"],
#     5: ["ጴጥሮስ ወጳውሎስ", "አቡነ ገብረ መንፈስ ቅዱስ"],
#     6: ["ኢየሱስ", "ቁስቋም", "ቅድስት አርሴማ"],
#     7: ["ሥላሴ", "ፊሊሞን", "አብላንዮስ"],
#     8: ["ማቴዎስ", "ዮልያኖስ", "አባ ኪሮስ"],
#     9: ["ቶማስ ሐዋርያ", "አንድርያስ ሐዋርያ", "አውሳብዮስ", "አርባ ሰማዕታት"],
#     10: ["በዓለ መስቀሉ ለእግዚእነ"],
#     11: ["ሐና ወኢያቄም", "ቅዱስ ፋሲለደስ ሰማዕት", "ቅዱስ ያሬድ"],
#     12: ["ሚካኤል", "ክርስቶስ ሠመራ", "አባ ሳሙኤል"],
#     13: ["እግዚአብሔር አብ", "ቅዱስ ሩፋኤል", "ተዓምረ ባስልዮስ"],
#     14: ["አቡነ አረጋዊ", "አባ ገብረ ክርስቶስ", "ድምጥያኖስ ሰማዕት"],
#     15: ["ቂርቆስና ኢየሉጣ", "ስልፋኮስ"],
#     16: ["ኪዳነ ምሕረት", "ሚካኤል ጳጳስ"],
#     17: ["ቅዱስ እስጢፋኖስ", "ሉቃስ ዘዓምደ ብርሃን", "አባ ግርማ"],
#     18: ["ፊልጶስ ሐዋርያ", "ኤስድሮስ ሰማዕት", "ተክለ አልፋ", "ኤውስጣቴዎስ ሰማዕት"],
#     19: ["ቅዱስ ገብርኤል", "አርቃዲዎስ", "ጎርጎርዮስ ሊቀ ጳጳስ"],
#     20: ["ጽንጸታ ለማርያም", "ነቢዩ ኤልሳ", "ሐጌ ነቢይ", "አባ ሰላማ መተርጉም", "ሕንጸተ አትናቴዮስ ሊቀጳጳስ"],
#     21: ["ማርያም"],
#     22: ["ቅዱስ ዑራኤል", "ደቅስዮስ", "ያዕቆብ ምሥራቃዊ"],
#     23: ["ጊዮርጊስ", "ልጊኖስ", "ሰማዕት"],
#     24: ["አቡነ ተክለ ሃይማኖት"],
#     25: ["መርቆሬዎስ", "አኒፍኖስ"],
#     26: ["ሆሴዕ ነቢይ", "ሳዶቅ ሰማዕት", "ቶምስ ደቀመዝሙር"],
#     27: ["መድኃኔዓለም", "ሕዝቅያስ ነቢይ", "አባ ዮሐንስ"],
#     28: ["አማኑኤል", "ቆስጠንጢስኖስ", "አብርሃም"],
#     29: ["በዓለ ወልድ", "ሳሙኤል ዘወገግ"],
#     30: ["ማርቆስ ወንጌላዊ"],
# }
# # Function to update the voice channels
# async def update_channels():
#     # Get the current date
#     now = datetime.datetime.now()
#     ethiopian_date = (now - datetime.timedelta(days=9)).strftime("መጋቢት %d")  # Subtract 9 days for the 17th

#     # Get the words for the day of the month
#     day_words = ethiopian_day_words.get(now.day, [])

#     # Update the voice channels
#     guild = client.get_guild(GUILD_ID)  # Replace GUILD_ID with your guild ID
#     if guild:
#         for channel_id in [1167180226451746876, 1167180947918168074]:  # Replace with your channel IDs
#             channel = guild.get_channel(channel_id)
#             if channel:
#                 try:
#                     if channel.id == 1167180226451746876:
#                         await channel.edit(name=ethiopian_date)
#                     elif channel.id == 1167180947918168074 and day_words:
#                         await channel.edit(name=" ".join(day_words))
#                 except Exception as e:
#                     print(f"Error updating channel {channel.name}: {e}")


# # Function to convert Gregorian date to Ethiopian date
# def gregorian_to_ethiopian(date_str):
#     gregorian_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
#     ethiopian_year = gregorian_date.year - 8  # Adjust for Ethiopian calendar
#     ethiopian_month = ethiopian_months[gregorian_date.month - 1]  # Month index starts from 0
#     ethiopian_day = gregorian_date.day
#     return f"{ethiopian_month} {ethiopian_day}"

# # Background task to update channels every day
# @tasks.loop(hours=24)
# async def daily_update():
#     await update_channels()

# # Event handler for bot startup
# @client.event
# async def on_ready():
#     print(f"Logged in as {client.user}")

#     # Start the daily update task
#     daily_update.start()


# client.run("OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw")



import discord
from discord.ext import tasks
import datetime

intents = discord.Intents.default()
intents.voice_states = True
client = discord.Client(intents=intents)

GUILD_ID = 970490174565928960

# Define the Ethiopian months and corresponding words
ethiopian_months = ["ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ"]

# Define the words for each day of the month
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
    ethiopian_day = now.day - 6
    if ethiopian_day <= 0:
        # Adjust if the day is in the previous month
        ethiopian_month = ethiopian_months[now.month - 2]
        ethiopian_day += 30  # Assuming Ethiopian months have 30 days

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

