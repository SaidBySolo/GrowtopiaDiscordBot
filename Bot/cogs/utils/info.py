import discord
from discord.ext import commands

class GTOevents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="봇정보")
    async def _info(self, ctx):
        pass

def setup(bot):
    bot.add_cog(GTOevents(bot))