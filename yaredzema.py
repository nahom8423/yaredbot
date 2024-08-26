import discord
from discord.ext import commands
from discord.ui import View, Button
import discord
from discord.ext import commands


TOKEN = 'OTcxMjEwMTIzMjQ4ODAzODcy.Gnr9xr.Zmdb_qreJJFWUUxDWqHW5BPkaF--G333MSq-vw'

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

bot = commands.Bot(command_prefix='!')

@bot.command(name='commands')
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
    await ctx.send(embed=command_pages[0], view=view)


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


@bot.command(name='mahletzema')
async def mahletzema_command(ctx):
    view = PaginatedButtons()
    await ctx.send('Choose a button:', view=view)
    
class PaginatedButtons(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_buttons(page=1)

    def add_buttons(self, page):
        self.clear_items()
        button_names = [
            "ማኅሌተ ጽጌ", "ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ", "መስከረም", "ጥቅምት", "ኅዳር", "ታኅሣሥ", 
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
        if interaction.custom_id.startswith('second_set_button_'):
                        paginated_content = read_and_parse_text_file('sibketmahlet.txt')
                        view = PaginatedView(paginated_content)
                        await interaction.response.edit_message(content='Navigating pages:', embed=paginated_content[0], view=view)
                        return False
        return await super().interaction_check(interaction)
    
def read_and_parse_text_file(file_path):
    absolute_path = r'mahletzema\sibket\sibketmahlet.txt'  # Replace with the actual path to your file
    with open(absolute_path, 'r', encoding='utf-8') as file:
        content = file.read()
    pages = content.split('---')  # Assuming '---' is your delimiter
    embeds = [discord.Embed(description=page) for page in pages]
    return embeds

paginated_content = [
    discord.Embed(
        title="Some Title",
        description="This is a valid description"  # Make sure this is a non-empty string
    )
]


@bot.command(name='mahletzema')


            paginated_content = [
            discord.Embed(title="አመ፪ ለኅዳር ዘሣብዓይ ( ፯ ) ዓመት - ሣድሳይ ( ፮ ) ሰንበት", description="""መልክአ ሥላሴ
ሰላም ለአፉክሙ ዘማዕጾሁ ሰላም፤
                           ጽጌያቲሁ ሥላሴ ለተዋህዶ ገዳም፤ መንገለ አሐዱ አምላክ ንዋየ መጻኢት ዓለም፤ ወልጡ አምልኮትየ በጸጋክሙ ፍጹም፤ 
                          እምአምልኮ ጣኦት ግሉፍ አሐዱ ድርኅም።
            """)
            .add_field(name="Links", value="- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/1.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/2.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/2%20-%20ame%204%20letikemt%20sabeay%20kaleaye%20senbet/3.mp3)"
                        """ዚቅ
                        ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/1.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/2.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/3.mp3)"
                       """ዚቅ (ዓዲ)
አሠርገወ ገዳማተ ስን ፤ በመንክር ኪን አርአያሁ ዘገብረ ፤ ሰሎሞን ጥቀ ኢለብሰ በኲሉ ክብሩ ፤ ከመ እሎን ጽጌያት ፤ ኢቀደምት ወኢደኃርት ፤ አራዛተ ሠርጕ ነሢኦሙ ፤ ኢክህሉ ከመ ክርስቶስ መዊዓ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/4.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/5.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/6.mp3)"
                       """ማኅሌተ ጽጌ
ኢየኃፍር ቀዊመ ቅድመ ስዕልኪ ወርኃ ጽጌረዳ አመ ኃልቀ፤ 
ዘኢየኃልቅ ስብሐተ እንዘ እሴብሐኪ ጥቀ፤ 
ተአምርኪ ማርያም ከመ አጠየቀ፤ 
ጸውዖ ስምኪ ያነሥእ ዘወድቀ፤ 
ኃጥአኒ ይሬሲ ጻድቀ።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/7.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/8.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/9.mp3)"
                       """ዚቅ
እለ ትነብሩ ተንሥኡ፤ ወእለ ታረምሙ አውሥኡ፤ ማርያምሃ በቃለ ስብሐት ጸውኡ፤ ቁሙ ወአጽምዑ ተአምረ ድንግል ከመ ትስምዑ፤ ጸልዩ ቅድመ ስዕላ ለቅድስት ድንግል፤ መርዓተ አብ ወእመ በግዑ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/14.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/15.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/16.mp3)"
                       """ማኅሌተ ጽጌ
እንዘ ተሐቅፊዮ ለሕፃንኪ ጽጌ ፀዓዳ ወቀይሕ፤ 
አመ ቤተ መቅደስ ቦእኪ በዕለተ ተአምር ወንጽሕ፤ 
ንዒ ርግብየ ትናዝዝኒ እምላህ፤ 
ወንዒ ሠናይትየ ምስለ ገብርኤል ፍሡሕ፤ 
ወሚካኤል ከማኪ ርኅሩኅ።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/19.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/20.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/21.mp3)"
                       """ዘቅ 
ንዒ ርግብየ ወንዒ ሠናይትየ ፤ እንተ ሐዋርያት ይሴብሑኪ ፤ መላእክት ይትለአኩኪ ፤ ፃዒ እምሊባኖስ ስነ ሕይወት።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/24.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/25.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/26.mp3)"
                       """ዚቅ (ዓዲ)
ንዒ ኀቤየ ኦ ድንግል ምስለ ኲሎሙ መላእክት፤ ከመ ታዕርጊ ጸሎተነ ጊዜ መንፈቀ ሌሊት።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/27.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/28.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/29.mp3)"
                       """ማኅሌተ ጽጌ
ሰዊተ ሥርናዩ ለታዴዎስ ወለበርተሎሜዎስ ወይኑ፤ 
እንተ ጸገይኪ አስካለ በዕለተ ተከልኪ እደ የማኑ፤ 
ማርያም ለጴጥሮስ ጽላሎቱ ወለጳውሎስ ሰበኑ፤ 
ብኪ ምውታን ሕያዋነ ኮኑ፤ 
ወሐዋርያት መላእክተ በሰማይ ኮነኑ።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/30.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/31.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/32.mp3)"
                       """ዚቅ
ኦ መድኃኒት ለነገሥት፤ ማኅበረ ቅዱሳን የዓውዱኪ፤ ነቢያት የዓኲቱኪ፤ ወሐዋርያት ይሴብሑኪ፤ እስመ ኪያኪ ኀቤ ለታዕካሁ ከመ ትኲኒዮሙ ማኅደረ፤ መላእክት ይኬልሉኪ፤ ጻድቃን ይባርኩኪ፤ አበው ይገንዩ ለኪ፤ እስመ ኪያኪ ኀቤ ለታዕካሁ ከመ ትኲኒዮሙ ማኅደረ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/36.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/37.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/38.mp3)"
                        """ማኅሌተ ጽጌ
ክበበ ጌራ ወርቅ ጽሩይ እምዕንቌ ባሕርይ ዘየኀቱ፤ 
ዘተጽሕፈ ብኪ ትእምርተ ስሙ ወተዝካረ ሞቱ፤ 
አክሊለ ጽጌ ማርያም ለጊዮርጊስ ቀጸላ መንግሥቱ፤ 
አንቲ ኲሎ ታሰግዲ ሎቱ፤ 
ወለኪኒ ይሰግድ ውእቱ።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/39.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/40.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/41.mp3)" 
                        """ዚቅ
ውድስት አንቲ በአፈ ነቢያት፤ ወስብሕት በሐዋርያት፤ አክሊለ በረከቱ ለያዕቆብ፤ ወትምክሕተ ቤቱ ለ፳ኤል።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/44.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/45.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/46.mp3)" 
                        """ማኅሌተ ጽጌ
ኅብረ ሐመልሚል ቀይሕ ወፀዓድዒድ አርአያ ኮስኮስ ዘብሩር፤ 
ተአምርኪ ንፁሕ በአምሳለ ወርቅ ግቡር፤ 
ተፈጸመ ናሁ ማኅሌተ ጽጌ ሥሙር፤ 
አስምኪ ቦቱ ንግሥተ ሰማያት ወምድር፤ 
ከመ በሕጽንኪ ያሰምክ ፍቁር።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/48.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/49.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/50.mp3)" 
                        """ዚቅ
ሃሌ ሃሌ ሉያ፤ ሃሌ ሉያ፤ ጥቀ አዳም መላትኅኪ ከመ ማዕነቅ፤ ይግበሩ ለኪ ኮስኮሰ ወርቅ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/54.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/55.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/56.mp3)" 
                        """ሰቆቃወ ድንግል
ተመየጢ እግዝእትየ ሀገረኪ ናዝሬተ፤ 
ወኢትጎንድዪ በግብጽ ከመ ዘአልብኪ ቤተ፤ 
በላዕሌኪ አልቦ እንተ ያመጽእ ሁከተ፤ 
ለወልድኪ ዘየኃሥሦ ይእዜሰ ሞተ፤ 
በከመ ነገሮ መልአክ ለዮሴፍ ብሥራተ።\n"""
                       "- [መልክእ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/58.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/59.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/60.mp3)" 
                       """ዚቅ
ሃሌ ሉያ፤ ተመየጢ ተመየጢ ሰላመ ሰጣዊት፤ ወንርዓይ ብኪ ሰላመ፤ ምንተኑ ትኔጽሩ በእንተ ሰላመ ሰጣዊት፤ እንተ ትሔውጽ እምርኁቅ፤ ከመ መድብለ ማኅበር ሑረታቲሀ ዘበስን ለወለተ አሚናዳብ።\n"""
                       "- [ቂም ዜማ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/63.mp3)\n"
                       "- [ጸናጽል](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/64.mp3)\n"
                       "- [መረግድ](https://www.ethiopianorthodox.org/churchmusic/zema%20timehert%20bet/3%20mahelete%20Tsige%20aqauquam/7%20aquaquam%20zetsiege%20zesabeay%20amet/6%20-%20ame%202%20lehidar%20zesabeaye%20sadesaye%20senbet/65.mp3)", inline=False),
                    #    """ዚቅ
                    #     ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
                    #    "- [New Link 1](https://example.com/new1)\n"
                    #    "- [New Link 2](https://example.com/new2)\n"
                    #    "- [New Link 3](https://example.com/new3)"
                    #    """ዚቅ
                    #     ሃሌ ሉያ፤ ለክርስቶስ ይደሉ ስብሐት፤ ለዘአብጽሐነ እስከ ዛቲ ሰዓት፤ እግዚአ ለሰንበት፤ አኮቴተ ነዓርግ ለመንግሥትከ፤ ምድረ በጽጌ አሠርጎከ።\n"""
                    #    "- [New Link 1](https://example.com/new1)\n"
                    #    "- [New Link 2](https://example.com/new2)\n"
                    #    "- [New Link 3](https://example.com/new3)" , inline=False),
            discord.Embed(title="Page 2", description="""This is some content for page 2.
            Again, you can write a lot of text here.
            Just keep adding lines and they will appear.""")
            .add_field(name="Links", value="[Link 1](https://example.com/1)\n[Link 2](https://example.com/2)\n[Link 3](https://example.com/3)", inline=False),
            # Add more pages as needed
        ]
view = PaginatedView(paginated_content)
async def interaction_check(self, interaction: discord.Interaction) -> bool:
    return False


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

bot = commands.Bot(command_prefix='!')

@bot.command(name='commands')
async def commandpage(ctx):
    command_pages = [
        discord.Embed(title="Commands List", description="..."),  # Fill in your command details
        discord.Embed(title="Commands List 2", description="...")
    ]
    view = PaginatedView(command_pages)
    await ctx.send(embed=command_pages[0], view=view)

class PaginatedButtons(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_buttons()

    def add_buttons(self):
        button_names = ["Button 1", "Button 2"]  # Add your button labels
        for i, name in enumerate(button_names, start=1):
            self.add_item(Button(label=name, custom_id=f'button_{i}'))

    @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Implement your page-switching logic
        pass

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.red)
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Implement your page-switching logic
        pass

client = discord.Client()
client.run(TOKEN)