import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import logging
from dotenv import load_dotenv
load_dotenv()  # This method will load variables from `.env`

# Setup logging to see the debug output
logging.basicConfig(level=logging.INFO)

# Define the bot intents
intents = discord.Intents.default()
intents.message_content = True

# Define the bot
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Register the slash command
        self.tree.add_command(mahlet_command)
        logging.info("Syncing commands...")
        await self.tree.sync()  # Sync commands with Discord

# Initialize the bot
bot = MyBot()

# Define the Ethiopian months starting from "መስከረም"
ethiopian_months = ["መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ", "ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ"]

# Define the paginated embed view
class PaginatedEmbedView(View):
    def __init__(self, embeds, timeout=180):
        super().__init__(timeout=timeout)
        self.embeds = embeds
        self.current_page = 0
        self.total_pages = len(embeds)
        self.update_buttons()

    def update_buttons(self):
        # Clear existing buttons
        self.clear_items()

        # Navigation buttons
        if self.current_page > 0:
            previous_button = Button(label="Previous", style=discord.ButtonStyle.primary)
            previous_button.callback = self.previous_page  # Assign callback
            self.add_item(previous_button)
        
        if self.current_page < self.total_pages - 1:
            next_button = Button(label="Next", style=discord.ButtonStyle.primary)
            next_button.callback = self.next_page  # Assign callback
            self.add_item(next_button)

    async def previous_page(self, interaction: discord.Interaction):
        self.current_page -= 1
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    async def next_page(self, interaction: discord.Interaction):
        self.current_page += 1
        self.update_buttons()
        await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

# Define the second set of buttons view
class SecondButtonsView(View):
    def __init__(self, button_labels, month_number):
        super().__init__(timeout=180)
        self.month_number = month_number  # Save the month number
        
        # Add buttons with specific labels passed in
        for i, label in enumerate(button_labels):
            button = Button(label=label, style=discord.ButtonStyle.secondary)
            button.callback = lambda inter, i=i: self.second_button_callback(inter, i)
            self.add_item(button)

    async def second_button_callback(self, interaction: discord.Interaction, button_number: int):
        # Create custom embeds for each button in the second set
        embeds = []

        # Example content for each second button, based on month and button_number
        if self.month_number == 1 and button_number == 0:  # መስከረም, First Button
            embeds = [
                discord.Embed(title="Page 1", description="Details for ዓውድ ዓመት Page 1"),
                discord.Embed(title="Page 2", description="Details for ዓውድ ዓመት Page 2"),
            ]
        elif self.month_number == 1 and button_number == 1:  # መስከረም, Second Button
            embeds = [
                discord.Embed(title="Page 1", description="Details for ምትረተ ርእሱ ቅዱስ ዮሐንስ መጥምቅ"),
            ]
        elif self.month_number == 2 and button_number == 0:  # ጥቅምት, First Button
            embeds = [
                discord.Embed(title="Page 1", description="Details for አቡነ ገበረ መንፈስ ቅዱስ"),
            ]
        # Add more conditions for other buttons and months as needed

        # Default content if no specific pages are defined
        if not embeds:
            embeds = [
                discord.Embed(title="Page 1", description="Default content for this button."),
            ]

        # Create the paginated embed view
        paginated_view = PaginatedEmbedView(embeds)

        # Edit the message to show the first page of the paginated embeds
        await interaction.response.edit_message(embed=embeds[0], content=None, view=paginated_view)

# Define the first set of buttons view
class InitialButtonsView(View):
    def __init__(self):
        super().__init__(timeout=180)  # Adjust the timeout as needed

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

# Define the slash command
@app_commands.command(name="mahlet", description="Starts the button interaction.")
async def mahlet_command(interaction: discord.Interaction):
    logging.info(f"{interaction.user} used /mahlet")
    
    view = InitialButtonsView()
    for i, month in enumerate(ethiopian_months):
        button = Button(label=month, style=discord.ButtonStyle.primary)
        button.callback = lambda inter, i=i: button_callback(inter, i+1)  # Assign callback, +1 to match month number
        view.add_item(button)

    view.message = await interaction.response.send_message("Choose a month:", view=view, ephemeral=False)

# Callback function for button interactions
async def button_callback(interaction: discord.Interaction, button_number: int):
    # Define specific labels for the second set of buttons based on the first button clicked
    if button_number == 1:  # መስከረም
        second_set_labels = ["ዓውድ ዓመት", "ምትረተ ርእሱ ቅዱስ ዮሐንስ መጥምቅ", "ፋሲለድሰ", "መስቀል", "አስተርእዮተ መስቀል", "ብዙኃን ማርያም"]
    elif button_number == 2:  # ጥቅምት
        second_set_labels = ["አቡነ ገበረ መንፈስ ቅዱስ", "አቡነ አረጋዊ", "መድኃኔዓለም"]
    elif button_number == 3:  # ኅዳር
        second_set_labels = ["ቁስቋም", "ቅዳሴ ቤት ለጊዮርጊስ", "አርባዕቱ እንስሳ", "ቅድስት ሐና", "ቅዱስ ሚካኤል", "አዕላፍ", "ጽዮን", "ካህናተ ሰማይ", "መርቆሬዎስ"]
    elif button_number == 4:  # ታኅሣሥ
        second_set_labels = ["በዓታ ለማርያም", "ዘስብከት", "ቅድስት አርሴማ", "ሳሙኤል", "ዘብርሃን", "ሩፋኤል", "ቅዱስ ገብርኤል", "ደቅስዮስ", "ተክለ ሃይማኖት", "አማኑኤል", "ዘልደት"]
    elif button_number == 5:  # ጥር
        second_set_labels = ["አባ ሊባኖስ", "ዮሐንስ ወልደ ነጐድጓድ", "ግዝረት", "ሥሌሴ", "ጥምቀት", "ቃና ዘገሊላ", "እግዚአብሔር አብ", "ቂርቆስ", "ጊዮርጊስ", "አስተርእዮ ማርያም", "ዑረኤል"]
    elif button_number == 6:  # የካቲት
        second_set_labels = ["ልደተ ስምዖን", "ኪዳነ ምሕረት"]
    elif button_number == 7:  # መጋቢት
        second_set_labels = ["ገብረ መንፈስ ቅዱስ", "መስቀል", "መድኃኔዓለም", "በዓለ አግዚአብሔር"]
    elif button_number == 8:  # ሚያዝያ
        second_set_labels = ["ጊዮርጊስ", "ማርቆስ"]
    elif button_number == 9:  # ግንቦት
        second_set_labels = ["ልደታ", "ቅዱስ ያሬድ", "ደብረ ምጥማቅ"]
    elif button_number == 10:  # ሰኔ
        second_set_labels = ["ሚካኤል", "ሕንፀተ ቤታ ለማርያም"]
    elif button_number == 11:  # ሐምሌ
        second_set_labels = ["ጴጥሮስ ውጳውሎስ", "ሥላሴ", "ቂርቆስ ውቅዱስ ገብርኤል"]
    elif button_number == 12:  # ነሐሴ
        second_set_labels = ["ደብረ ታቦር", "ኪዳነ ምሕረት", "ተክለ ሃይማኖት"]
    elif button_number == 13:  # ጳጉሜ
        second_set_labels = ["ሩፋኤል"]
    else:
        second_set_labels = [f"Option {i}" for i in range(1, 7)]  # Default labels

    # Show the second set of buttons based on the first button clicked
    view = SecondButtonsView(second_set_labels, button_number)  # Pass month_number
    await interaction.response.edit_message(content="Now choose one of the following:", view=view)
# Run the bot


# bot.run('OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw')  # Replace with your actual bot token
import os
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot.run(TOKEN)  # Replace with your actual bot token