import datetime
import importlib
import random

import discord

import functions.dice



class RpgBot(discord.Client):
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
        if message.content.startswith("/bothelp"):
            await message.author.send("__**Hello**__,\nI'm your friendly Channel Bot.\n\nYou typed /bothelp for help. May I help you?\n\nIf You need help, look at my one functionality below.\n\n\n-> for some dicerolling, type */roll [amount]d[pips]s[number needed]*, for example /roll 5d6s4", delete_after=30)
            return
        ### DICEROLL
        if message.content.startswith("/roll "):
            # rollcommand = message.content.split(" ")[1]
            # diceroll = rollcommand.lower()

            # diceroller = funclib.roll()
            # result = diceroller.rollplayer(diceroll)
            # roller = code.dice

            # await message.channel.send(str(result))
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

if __name__ == "__main__":
    def main():
        print("has to be run by discord client")
        

client = RpgBot()
token = str(input())
client.run(token)