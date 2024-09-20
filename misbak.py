import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import View, Button, Modal, TextInput
import os
import random
import re
import datetime
import pytz  # Import pytz for time zone handling

# Load the bot token securely from environment variables
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Ensure your .env file contains your bot token

# Replace with your actual guild (server) ID as an integer
GUILD_ID = 970490174565928960  # Replace with your guild ID

# Define the bot intents
intents = discord.Intents.default()

# Create the bot class
class MyBot(commands.Bot):
    def __init__(self):
        # Set command_prefix to None since we're using slash commands
        super().__init__(command_prefix=None, intents=intents)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        print("Syncing commands...")
        await self.tree.sync(guild=guild)
        print(f"Slash commands synced to guild {guild.id}.")

# Initialize the bot
bot = MyBot()

# Misbak View with buttons
class MisbakView(discord.ui.View):
    @discord.ui.button(label="ዘሰንበት", style=discord.ButtonStyle.primary)
    async def option1(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Use script directory to build absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, "images", "option1")
        
        # Send a random image from the option1 folder
        images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if images:
            image_file = random.choice(images)
            image_path = os.path.join(folder_path, image_file)
            file = discord.File(image_path)
            await interaction.response.send_message("ዘሰንበት ምስባክ:", file=file)
        else:
            await interaction.response.send_message("No images found in Option 1 folder.", ephemeral=True)

    @discord.ui.button(label="ዛሬ", style=discord.ButtonStyle.primary)
    async def option2(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Use Ethiopia's time zone
        ethiopia_tz = pytz.timezone('Africa/Addis_Ababa')
        now = datetime.datetime.now(ethiopia_tz)
        now_date = now.date()  # Extract the date component

        # Simplified Ethiopian date calculation
        gregorian_year = now.year
        gregorian_month = now.month
        gregorian_day = now.day

        # Determine the Ethiopian year
        if (gregorian_month > 9) or (gregorian_month == 9 and gregorian_day >= 11):
            eth_year = gregorian_year - 7
            new_year = datetime.datetime(gregorian_year, 9, 11, tzinfo=ethiopia_tz).date()
        else:
            eth_year = gregorian_year - 8
            new_year = datetime.datetime(gregorian_year - 1, 9, 11, tzinfo=ethiopia_tz).date()

        # Calculate the number of days since September 11
        delta_days = (now_date - new_year).days

        # Calculate Ethiopian month and day
        eth_month = (delta_days // 30) + 1
        eth_day = (delta_days % 30) + 1

        # Format month and day with leading zeros
        eth_month_str = f"{eth_month:02d}"
        eth_day_str = f"{eth_day:02d}"

        # Construct the image filename
        image_filename = f"{eth_month_str}-{eth_day_str}.png"

        # Use script directory to build absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, "images", "dates")
        image_path = os.path.join(folder_path, image_filename)

        # Debugging statements
        print(f"Current date (Ethiopia time): {now_date}")
        print(f"Ethiopian New Year date: {new_year}")
        print(f"Delta days: {delta_days}")
        print(f"Ethiopian date: {eth_month_str}/{eth_day_str}")
        print(f"Looking for image at: {image_path}")

        if os.path.isfile(image_path):
            file = discord.File(image_path)
            await interaction.response.send_message("ዛሬ ምስባክ:", file=file)
        else:
            await interaction.response.send_message(
                f"No image found for today's date ({eth_month_str}/{eth_day_str}).", ephemeral=True
            )

    @discord.ui.button(label="N/A", style=discord.ButtonStyle.primary)
    async def option3(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Implement logic for tomorrow's date if needed
        await interaction.response.send_message("Option 3 is under development.", ephemeral=True)

    @discord.ui.button(label="Enter Date", style=discord.ButtonStyle.secondary)
    async def enter_date(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Show a modal to enter date
        modal = DateInputModal()
        await interaction.response.send_modal(modal)

# Date Input Modal
class DateInputModal(discord.ui.Modal, title="Enter Date"):
    date_input = discord.ui.TextInput(
        label="Enter date (MM/DD)",
        placeholder="e.g., 01/07",
        required=True,
        max_length=5,
    )

    async def on_submit(self, interaction: discord.Interaction):
        date_input_value = self.date_input.value.strip()
        # Validate date format MM/DD
        if not re.match(r'^\d{2}/\d{2}$', date_input_value):
            await interaction.response.send_message(
                "Invalid date format. Please enter date as MM/DD.", ephemeral=True
            )
            return
        # Replace '/' with '-' to match your filename convention
        image_filename = f"{date_input_value.replace('/', '-')}.png"
        # Use script directory to build absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, "images", "dates")  # Updated to "dates" folder
        image_path = os.path.join(folder_path, image_filename)
        # Debugging statement
        print(f"Looking for image at: {image_path}")
        if os.path.isfile(image_path):
            file = discord.File(image_path)
            try:
                await interaction.response.send_message(
                    f"Here is the image for {date_input_value}:", file=file
                )
            except discord.errors.InteractionResponded:
                await interaction.followup.send(
                    f"Here is the image for {date_input_value}:", file=file
                )
        else:
            try:
                await interaction.response.send_message(
                    f"No image found for {date_input_value}.", ephemeral=True
                )
            except discord.errors.InteractionResponded:
                await interaction.followup.send(
                    f"No image found for {date_input_value}.", ephemeral=True
                )

# Define the slash command using the bot's tree decorator
@bot.tree.command(name="misbak", description="Select an option.")
async def misbak_command(interaction: discord.Interaction):
    print(f"/misbak command invoked by {interaction.user}")
    view = MisbakView()
    await interaction.response.send_message("Select an option:", view=view)

# Run the bot
bot.run(TOKEN)
