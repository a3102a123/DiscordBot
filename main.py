from bot import *
import json
import os
import asyncio

try:
    TOKEN = os.getenv("DC_TOKEN")
    print(f"get token : {TOKEN}")
    print("Finding the env var of token")
except:
    with open(os.path.join("config.json")) as json_file:
        config = json.load(json_file)
        TOKEN = config["TOKEN"]
    print("Using config file to set up token")

# init the bot
### intents is the authority of the discord 
intents = discord.Intents.default()
intents.message_content = True
client = BotClient(intents=intents)
### run the bot
client.run(TOKEN)
