import discord
from typing import Optional
from utils.dice import State
# Create a class called MyView that subclasses discord.ui.View
class DiceView(discord.ui.View):
    def __init__(self, *, timeout: Optional[float] = 180.0):
        super().__init__(timeout=timeout)
        
        self.state_menu = discord.ui.Select(
            # the placeholder text that will be displayed if nothing is selected
            placeholder = "擲骰狀態", 
            # the minimum number of values that must be selected by the users
            min_values = 1, 
            # the maximum number of values that can be selected by the users
            max_values = 1, 
            
            options=[
                discord.SelectOption(label="正常", value=State.Regular.name, default=True),
                discord.SelectOption(label="優勢", value=State.Advantage.name),
                discord.SelectOption(label="劣勢", value=State.Disadvantage.name),
            ]
        )
        # add the default option's value
        # There are some bugs of discord.py. It doesn't add the default value to the values list.
        self.state_menu.values.append(State.Regular.name)
        
        self.check_btn = discord.ui.Button(
            label="Roll!", 
            style=discord.ButtonStyle.primary, 
            emoji="😎"
        )
        
        self.layout()
    
    def layout(self):
        self.add_item(self.state_menu)
        self.add_item(self.check_btn)
    
    # Create a button with the label "😎 Click me!" with color Blurple
    # @discord.ui.button(label="Roll!", style=discord.ButtonStyle.primary, emoji="😎") 
    # async def button_callback(self, interaction, button):
    #     # Send a message when the button is clicked
    #     await interaction.response.send_message("You clicked the button!") 