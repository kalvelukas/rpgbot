"""Overwritten discord.Client Class"""
import datetime
# import importlib
# import random
import sys

import discord

from functions.dice import roll as rollbot

class RpgBot(discord.Client):
    """Lukas' discord client"""
#### BOT ReadyMsg plus Logfile datetime entry ###
    async def on_ready(self):
        """post a log entry to logfile when logging in"""
        file_object = open("logfile.txt", "a")
        datetime_object = datetime.datetime.now()
        file_object.write(str(datetime_object) + " Bot logged in on Server\n")
        print(str(datetime_object) + " I'm there!!! BeepBoop!")
        return
#### BOT ACTIONS ON MSG in channels
    async def on_message(self, message):
        """when a message is posted in a chat, do..."""
        print(str(message.author) + " " + str(message.content))
## FUNTIONALITIES FOR EVERYONE
        ### BOTHELP
        if message.content.startswith("Hey!"):
            await message.author.send("__**Hello**__,\nI'm your friendly Channel Bot.")
            return
        ### DICEROLL "delete.after = 30"
        if message.content.startswith("/roll "):
            rollcommand = message.content.split(" ")[1]
            diceroll = rollbot(int(rollcommand))
            await message.channel.send(str(diceroll))
            return

## ADMINISTRATION
        #### MODULE RELOAD ###
        # if (message.content.startswith("/refresh")):
        #     f = open("logfile.txt", "a")
        #     datetime_object = datetime.datetime.now()
        #     print(datetime_object)
        #     f.write(str(datetime_object) + " MODULE RELOAD\n")
        #     print("reloaded modules")
        #     importlib.reload(code.dice)
            # return
        #### BOTKILL ###
        if message.content.startswith("/gosleep"):
            file_object = open("logfile.txt", "a")
            datetime_object = datetime.datetime.now()
            print(datetime_object)
            file_object.write(str(datetime_object) + " BOTKILL\n")
            print("bot ended")
            sys.exit()

client = RpgBot()
TOKEN = input()
client.run(TOKEN)
