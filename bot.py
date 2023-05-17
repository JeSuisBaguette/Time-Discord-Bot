# Imports
import os
import discord
from dotenv import load_dotenv
from time_API import get_time, convert_time


# Setup
intents = discord.Intents().all()
client = discord.Client(intents=intents)


# To see if the bot has connected properly. 
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


# All responses to commands. 
@client.event
async def on_message(message):
    # Makes sure to not respond if the author is the bot itself. 
    if message.author == client.user:
        return

    # In response to "$hello".
    if (message.content).lower().startswith("$hello"):
        await message.channel.send(
            "Hello! I can help with fetching and converting between time zones. Type '$help' for command specifications."
        )

    # Lists all commands and parameters using "get_help()".
    if (message.content).lower().startswith("$help"):
        await message.channel.send(get_help())

    # Shows current time in specifiec timezone.
    if (message.content).lower().startswith("$time"):
        try:
            command, target = message.content.split("-")
            time = get_time(target.strip())
            await message.channel.send(time)
        except:
            await message.channel.send("Invalid Time zone. Only IANA time zone names are accepted.")

    # Converts the time into the time zone specified from the time zone entered. Increment is a necessary parameter even if none. 
    if (message.content).lower().startswith("$convert"):
        try:
            command, from_zone, target = message.content.split("-")
            if "+" in message.content:
                to_zone, increment = target.split("+")
            else:
                increment = "00:00:00:00"
                to_zone = target
            convert = convert_time(
                from_zone.strip(), to_zone.strip(), increment.strip()
            )
            await message.channel.send(convert)
        except:
            await message.channel.send("Invalid increment range/time zone. Make sure to add leading zeros if applicable/only enter time zones in IANA format.")

def get_help():
    return f'List of bot commands:\
            \n\n"$time-continent/city": Returns the current time of the specified city. Must be in IANA (continent/city) format\
            \n\n"$convert-continent/city-continent/city+DD:HH:MM:SS": Converts time to the second time zone by specified increment (zero if not given).\
            \n\nPlease note that "-", "+", and leading zeros (ex: 00:01:00:00 to incrememnt by one hour) are required exactly as specified.'


# Run
load_dotenv()
client.run(os.getenv("TOKEN"))
