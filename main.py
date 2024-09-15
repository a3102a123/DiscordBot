from bot import *
import json
import os
import asyncio
from gpt import *

def init():
    try:
        with open(os.path.join("config.json")) as json_file:
            config = json.load(json_file)
        print("Using config file to set up token")
    except:
        config = dict()
        config["DC_TOKEN"] = os.getenv("DC_TOKEN")
        config["GOOGLE_TOKEN"] = os.getenv("GOOGLE_TOKEN")
        print("Using the env var to set up token")
    return config

if __name__ == "__main__":
    cfg = init()
    # init google gemini
    gpt = Gemini(cfg["GOOGLE_TOKEN"])

    # init the bot
    intents = discord.Intents.default()
    intents.message_content = True
    client = BotClient(gpt=gpt,command_prefix = '/',intents=intents)
    ### run the bot
    client.run(cfg["DC_TOKEN"])
