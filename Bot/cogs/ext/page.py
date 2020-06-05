import discord
import asyncio

async def pererror(msg):
    try:
        await msg.clear_reactions()
    except Exception:
        pass
    else:
        await msg.add_reaction(emoji="❎")
        await msg.add_reaction(emoji="◀")
        await msg.add_reaction(emoji="▶")

async def page(bot, ctx, embedlist:list):

    num = 0
    total = len(embedlist)

    msg = await ctx.send(embed=embedlist[num])
    await msg.add_reaction(emoji="❎")
    await msg.add_reaction("◀")
    await msg.add_reaction("▶")

    def check(reaction: discord.Reaction, user: discord.User):
        return (user.id == ctx.author.id) and (reaction.emoji in ['▶', '◀', '❎'])

    while True:
        try:
            reaction, user = await bot.wait_for(event="reaction_add", check=check, timeout=80.0)
            if user.id != ctx.author.id or reaction.message.id != msg.id:
                continue

        except asyncio.TimeoutError:
            await msg.edit(embed=discord.Embed(title="요청이 만료되었어요."))
            await msg.clear_reactions()
            return

        else:
            if reaction.emoji == "❎":
                await msg.delete()
                return

            elif reaction.emoji == "▶":

                num = num
                total = total
                
                num += 1

                if num > total - 1:
                    num = 0

                await msg.edit(embed=embedlist[num])
                await pererror(msg)
        
            elif reaction.emoji == "◀":

                num = num
                total = total

                num -= 1
                if num < 0:
                    num = total - 1

                await msg.edit(embed=embedlist[num])
                await pererror(msg)