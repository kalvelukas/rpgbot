import random

#INITIALISING
   # Create standard values
def __init__(self):
    self.diceamount = 1
    self.dicepips = 6
    self.errormsg = "ERROR, please type again."
#INTERFACE METHODS
   #
    #PLAYER INPUT/OUTPUT

def rollplayer(self, diceroll):
    self.diceroll = diceroll
    if (("d" in diceroll) and len(diceroll) < 15):
        params = self.splitter(diceroll)
        if params == self.errormsg:
            return self.errormsg
        results = self.roller(params)
        formatted = self.formatter(results, params)
        return formatted
    else:
        return self.errormsg

    #NPC INPUT/OUTPUT
def rollnpc(self, diceamount, dicepips):
        pass

#INFORMATION TRANSITION AS LIST
def splitter(self, diceroll):
        self.diceroll = diceroll
        diceamount = self.diceroll.split("d")[0]
        splithelp = str(self.diceroll.split("d")[1])

        if ("s" in splithelp):
            dicepips = splithelp.split("s")[0]
            desire = self.diceroll.split("s")[1]
        else:
            dicepips = self.diceroll.split("d")[1]

        if diceamount.isnumeric() and dicepips.isnumeric() and (int(diceamount) < 101):
            rollparams = list(())
            rollparams.append(int(diceamount))
            rollparams.append(int(dicepips))
            if desire.isnumeric():
                rollparams.append(int(desire))
            else:
                rollparams.append(int(dicepips))
            return rollparams
        else:
            return self.errormsg

def roller(self, parameters):
        self.parameters = parameters
        diceamount = int(parameters[0])
        dicepips = int(parameters[1])
        resultlist = list(())
        if (diceamount > 0):
            i = 0
            while (i < diceamount):
                i += 1
                result = random.randint(1, dicepips)
                resultlist.append(result)
            return resultlist
        else:
            return

#TEXT FORMATTER
def formatter(self, results, parameters= [1, 6, 6]):
        self.dicepips = parameters[1]
        self.desire = parameters[2]
        self.result = results
        chatstringresult = "You have rolled! Wonderful!\n\n\n"
        print(str(self.desire))
        for entry in self.result:
            if entry == 1:
                chatstringresult = chatstringresult + "__**" + str(entry) + "**__     Crit. Failure\n"

            if entry < self.desire and entry != 1:
                chatstringresult = chatstringresult + "*" + str(entry) + "*     Failure\n"

            if entry == self.dicepips:
                chatstringresult = chatstringresult + "__**" + str(entry) + "**__     Crit. Success\n"

            if ((self.desire > 1) and (entry >= self.desire) and (entry < self.dicepips)):
                chatstringresult = chatstringresult + "__" + str(entry) + "__     Success\n"
        return chatstringresult
