
class Splitter:

    def split (self, diceroll):
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

    # def rollplayer(self, diceroll):
    #     self.diceroll = diceroll
    #     if (("d" in diceroll) and len(diceroll) < 15):
    #         params = self.splitter(diceroll)
    #         if params == self.errormsg:
    #             return self.errormsg
    #         results = self.roller(params)
    #         formatted = self.formatter(results, params)
    #         return formatted
    #     else:
    #         raise ValueError
    
    @staticmethod
    def check_negative(self, dicenumber: int = 1, dicepips: int = 1, modifier: int = 1):
        """take up to three variables, check >= 1"""
        if dicenumber > 0 and dicepips > 0:
            return
        else:
            raise ValueError("Can't roll less than one")

    @staticmethod
    def verify_type_integer(dicenumber, dicepips, modifier: int = 1):
        if isinstance(dicenumber, int) and isinstance(dicepips, int):
            return
        else:
            raise TypeError("Input not of Type Integer")

