from bot import *
import json
import os
import asyncio

with open(os.path.join("config.json")) as json_file:
    config = json.load(json_file)
print(config)

# init the bot
### intents is the authority of the discord 
intents = discord.Intents.default()
intents.message_content = True
client = BotClient(intents=intents)
### run the bot
client.run(config["TOKEN"])
