import discord

# 
class BotClient(discord.Client):
    
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
    async def on_message(self, message):
        ### restricting the bot replys in certain channels
        if str(message.channel.id) == "1278254656115445801":
            print(f'Testing: Message from {message.author}: {message.content}')