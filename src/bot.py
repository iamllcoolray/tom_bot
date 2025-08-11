import os
from typing import Final, List
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot_response import get_bot_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
TEST_GUILD_ID = os.getenv("GUILD_ID")

# Sample autocomplete suggestions
DAN_SUGGESTIONS = [
    "Tell me a joke Tom.",
    "Who are you?",
    "Give me a motivational quote Tom.",
    "What are you?",
    "Explain what you do here."
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    try:
        await bot.sync_commands()
        print("Slash commands synced.")
    except Exception as e:
        print(f"Command sync failed: {e}")


# Autocomplete function
async def message_autocomplete(ctx: discord.AutocompleteContext) -> List[str]:
    return [s for s in DAN_SUGGESTIONS if ctx.value.lower() in s.lower()]

# Slash command using discord.Option with autocomplete
@bot.slash_command(name="tom", description="Ask Tom anything", guild_ids=[TEST_GUILD_ID])
async def dan(
    ctx: discord.ApplicationContext,
    message: str = discord.Option(description="Your message", autocomplete=message_autocomplete)
):
    try:
        print(f"/tom called in {ctx.channel} by {ctx.author} with message: {message}")
        response = get_bot_response(user_message=message)
        await ctx.respond(f"{ctx.author.mention} {response}")
    except Exception as e:
        print(f"Error: {e}")
        await ctx.respond("Something went wrong while processing your message.", ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
