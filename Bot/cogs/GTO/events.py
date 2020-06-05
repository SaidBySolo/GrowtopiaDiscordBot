import discord
from discord.ext import commands
from cogs.ext.page import page

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="이벤트")
    async def _Events(self, ctx):

        year_embed = discord.Embed(
            title="그로우토피아 이벤트 정보입니다.", description="**연례행사**\n\n매년 열리는 이벤트는 매년 1회 발생하며\nHarvest Festival, Mid-Autumn Festival과 같은 휴일을 축하하기위해 개최됩니다.\n연간 이벤트는 1주일 동안 진행되며 WinterFest는 2일 동안 지속됩니다.")
        year_embed.add_field(name="1월", value="Anniversary Week")
        year_embed.add_field(name="1월/2월", value="Lunar New Year")
        year_embed.add_field(name="2월", value="Valentine's Week")
        year_embed.add_field(name="3월", value="St. Patrick's Week")
        year_embed.add_field(name="4월", value="Easter Week")
        year_embed.add_field(name="5월", value="Cinco De Mayo Week")
        year_embed.add_field(name="5월/6월", value="Super Pineapple Party")
        year_embed.add_field(name="6월/7월", value="SummerFest")
        year_embed.add_field(name="8월", value="Player Appreciation Week")
        year_embed.add_field(name="9월/10월", value="Harvest Festival")
        year_embed.add_field(name="10월/11월", value="Halloween")
        year_embed.add_field(name="11월", value="Thanksgiving Week")
        year_embed.add_field(name="12월", value="WinterFest")

        month_embed = discord.Embed(
            title="그로우토피아 이벤트 정보입니다.", description="**월간행사**\n\n월간 이벤트는 한달에 한두번 발생하며 일반적으로 24시간 동안만 지속됩니다.\nLocke The Traveling Salesman는 한달에 두번씩 발생되고,이 이외에는 한달의 한번씩만 발생됩니다.")
        month_embed.add_field(name="The Carnival", value="3일")
        month_embed.add_field(name="Night Of The Comet", value="24시간")
        month_embed.add_field(name="Locke The Traveling Salesman", value="24시간, 월드에 10분")
        month_embed.add_field(name="The Grand Tournament", value="5일")
        month_embed.add_field(name="Surgery Day", value="24시간")
        month_embed.add_field(name="All Howl's Eve", value="24시간")
        month_embed.add_field(name="Geiger Day", value="24시간")
        month_embed.add_field(name="Ghost Day", value="24시간")

        embedlist = [year_embed, month_embed]
        await page(self.bot, ctx, embedlist)


def setup(bot):
    bot.add_cog(Events(bot))
