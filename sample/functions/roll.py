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
        raise ValueError

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
            raise ValueError