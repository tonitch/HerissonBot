import discord
import asyncio
import configparser
import os.path
import shutil
import pathlib

#Init Config File
Config = configparser.ConfigParser()
configfile = os.path.exists("./config.ini")
if configfile:
    print("config.ini Founded... loading")
else:
    shutil.copyfile("./data/Example_config.ini", "./config.ini")
    print("Example_config.ini copied to config.ini, please enter the bot key to run the bot")
Config.read("config.ini")
bot_key = Config.get("Bot", "key")
default_botprefix = Config.get("Bot", "Command_Prefix")

#Init Discord Bot
Client = discord.Client()

@Client.event
async def on_ready():
    print("Démarage du bot: HerissonBot")
    print("bot ID: " + Client.user.iD)
    print("bot Name: " + Client.user.name)


#Run Bot
Client.run(bot_key)
