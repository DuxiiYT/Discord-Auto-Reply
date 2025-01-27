import discord
import asyncio

keywords = ["buy", "rate", "black"]

intents = discord.Intents.all()
intents.messages = True

client = discord.Client(intents=intents, self_bot=True)

TOKEN = ""

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if isinstance(message.channel, discord.DMChannel):
        if any(keyword in message.content.lower() for keyword in keywords):
            await message.channel.send("black: 500$")
try:
    client.run(TOKEN, bot=False)
except discord.errors.LoginFailure:
    print("Wrong token")
    exit()
