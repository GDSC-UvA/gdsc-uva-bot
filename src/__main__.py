import discord
import logging
import os

from utils import render_templates as render


TOKEN = os.environ.get("GDSC_DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("Discord Bot token is not defined in environment variable 'GDSC_DISCORD_TOKEN'!")

logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

@bot.event
async def on_message(message: discord.Message):
    if message.author != bot.user:
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

@bot.slash_command()
async def test(ctx, arg: str):
    print(arg)
    await ctx.send("Recieved command!")

bot.run(TOKEN)