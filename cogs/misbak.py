import discord
from discord.ext import commands
from datetime import datetime
import os

class WeeklyEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Use a raw string or replace \ with /
        self.BASE_IMAGE_DIR = r"C:\Users\nahom\Documents\yaredbot\images"
        self.IMAGE_PATHS = {
            # Define your weekly image paths here
        }
        self.ALLOWED_CHANNEL_IDS = ["970857256251953162"]  # Correct as needed

    @discord.app_commands.command(name="misbak", description="Send weekly images")
    async def misbak(self, interaction: discord.Interaction):
        if str(interaction.channel.id) not in self.ALLOWED_CHANNEL_IDS:
            await interaction.response.send_message("This command can't be used in this channel.", ephemeral=True)
            return

        week_number = datetime.now().isocalendar()[1]

        if week_number in self.IMAGE_PATHS:
            for image_name in self.IMAGE_PATHS[week_number]:
                file_path = os.path.join(self.BASE_IMAGE_DIR, image_name)
                if os.path.exists(file_path):
                    await interaction.response.send_message(file=discord.File(file_path))
                else:
                    await interaction.response.send_message("Image not found.", ephemeral=True)
        else:
            await interaction.response.send_message("No images set for this week.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(WeeklyEvents(bot))
