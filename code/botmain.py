import datetime
import importlib
import random

import discord

from code.functions import dice as dice

class RpgBot(discord.Client):
    """Lukas' discord client"""
#### BOT ReadyMsg plus Logfile datetime entry ###
    async def on_ready(self):
        f = open("logfile.txt", "a")
        datetime_object = datetime.datetime.now()
        f.write(str(datetime_object) + " Bot logged in on Server\n")
        print(str(datetime_object) + " I'm there!!! BeepBoop!")
        return
#### BOT ACTIONS ON MSG in channels
    async def on_message(self, message):
        print(str(message.author) + " " + str(message.content))
## FUNTIONALITIES FOR EVERYONE
        ### BOTHELP
        if message.content.startswith("Hey!"):
            await message.author.send("__**Hello**__,\nI'm your friendly Channel Bot.")
            return
        ### DICEROLL "delete.after = 30"
        if message.content.startswith("/roll "):
            rollcommand = message.content.split(" ")[1]
            diceroll = dice.roll(rollcommand)
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
        if (message.content.startswith("/gosleep")):
            f = open("logfile.txt", "a")
            datetime_object = datetime.datetime.now()
            print(datetime_object)
            f.write(str(datetime_object) + " BOTKILL\n")
            print("bot ended")
            exit()

client = RpgBot()
token = str(input())
client.run(token)