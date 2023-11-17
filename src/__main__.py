import discord
import logging
from discord.ext import commands
import os
import pprint

from utils import render_templates as render


TOKEN = os.environ.get("GDSC_DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("Discord Bot token is not defined in environment variable 'GDSC_DISCORD_TOKEN'!")

logger = logging.getLogger(__name__)

# TODO Just use discord.Bot
class GDSCUvAClient(discord.Client):
    
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
        
    async def on_message(self, message: discord.Message):
        if message.author != self.user:
            try:
                channel = await message.author.create_dm()
                await channel.send(render.verification_message(message.author.name))
            except discord.errors.HTTPException as err:
                if err.code == 50007:
                    # Discord Bot is not able to send a DM to user.
                    # Most likely because the user 
                    logger.warning(f"Could not send user '{message.author}' a verification message.")
                else:
                    raise err

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$>", intents=intents)

@bot.command(name="test", help="Please just enter something as a string.")
async def test(ctx, args: str):
    print(args)

bot.run(TOKEN)

# client = GDSCUvAClient(intents=intents)
# client.run(TOKEN)