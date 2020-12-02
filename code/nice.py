#nice.py
"""take resultlist, desired diceroll, format string for output"""
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