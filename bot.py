from typing import Any, Coroutine
import discord
from discord.ext import commands
from gpt import *
from utils.loader import load_folder

#
class MyHelp(commands.HelpCommand):
    def __init__(self, **options: Any) -> None:
        super().__init__(**options)
        
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog, commands in mapping.items():
           command_signatures = [self.get_command_signature(c) for c in commands]
           print(command_signatures)
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)
        
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command), color=discord.Color.random())
        if command.help:
            embed.description = command.help
        if alias := command.aliases:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

# 
class BotClient(commands.Bot):
    def __init__(self, ch_id, gpt: Gemini, **kwargs) -> None:
        super().__init__(**kwargs)
        self.gpt = gpt
        self.CHANNEL_ID = int(ch_id)
    
    async def setup_hook(self) -> None:
        self.info_dict = load_folder("docs")
        self.remove_command("help")
        self.help_command = MyHelp()
        await self.bind()
        return await super().setup_hook()
    
    async def bind(self):
        await self.add_cog(BasicCommand(self))
        await self.add_cog(GPTCommand(self))
    
    async def on_ready(self):
        print('Logged in as')
        print(f"Bot name : {self.user.name}")
        print(f"Bot ID : {self.user.id}")
        print('------')
        print(self.all_commands)
        
    def create_channel(self):
        discord.guild    
    
    async def on_message(self, message: discord.Message) -> None:
        if message.channel.id != self.CHANNEL_ID:
            # return when message appears in other channels
            return
        return await super().on_message(message)
    # async def on_message(self, message):
    #     ### restricting the bot replys in certain channels
    #     if message.author == self.user:
    #         return
    #     if str(message.channel.id) == "1278254656115445801":
    #         print(f'Info: Message from {message.author}: {message.content}')
    #         resp = self.gpt.send(message.content)
    #         await message.channel.send(resp.text)

def is_channel():
    async def check_channel(ctx):
        return ctx.channel.id == 1278254656115445801
    return commands.check(check_channel)
    
#
class BasicCommand(commands.Cog):
    def __init__(self, bot: BotClient) -> None:
        super().__init__()
        self.bot = bot
    
    @commands.command(help="The announcement and basic information of this bot.")
    async def info(self, ctx):
        await ctx.send(self.bot.info_dict["info"])
    @commands.command(help="Testing the RTT(round trip time) of the server")
    async def ping(self, ctx):
        rtt = self.bot.latency * 1000
        await ctx.send(f"Ping : {rtt:.2f}ms")
       
        
    # @commands.command()
    # async def help(self, ctx):
    #     await ctx.send("type text here")

#
class GPTCommand(commands.Cog):
    def __init__(self, bot: BotClient) -> None:
        super().__init__()
        self.bot = bot
    
    @commands.command(help="Sending the message to Gemini and get the response.")
    async def send(self, ctx, *content):
        # checking for empty content
        if not content:
            await ctx.send("You should give some message before the /send command\nUsage : /send typing some word here.")
            return
        msg = " ".join(content)
        print(f'Info: Message from {ctx.message.author}: {msg}')
        resp = self.bot.gpt.send(msg)
        await ctx.send(resp.text)
