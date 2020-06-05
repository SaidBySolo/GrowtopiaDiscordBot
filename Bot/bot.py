import discord
from discord.ext import commands
import json
import os

token = "Token paste here"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="&")

def load_cogs(bot):
    extensions = ['jishaku',
                  'cogs.GTO.events']

    failed = []

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"{e.__class__.__name__}: {str(e)}")
            failed.append(extension)

    if failed:
        print(f"\n{' '.join(failed)}ë¥?ë¡œë“œ?˜ëŠ”???¤íŒ¨?ˆìŠµ?ˆë‹¤.\n")
    return failed
    

if __name__ == '__main__':
    bot = Bot()
    bot.remove_command('help')
    load_cogs(bot)
    bot.run(token)