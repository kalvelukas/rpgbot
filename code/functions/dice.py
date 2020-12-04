#dice.py
"""take parameters and return a list of random numbers.
"""
import random

from code.functions.slice import Splitter


class RollSuper():
    """superclass
    """
    def roll(self, dicenumber: int = 1, dicepips: int = 6, limit=10000) -> list:
        """Take 2 integers return as many as first integer random integers
        (max value <= second integer) as list.
        """
        self.dicenumber = dicenumber
        self.dicepips = dicepips
        Splitter.verify_type_integer(self.dicenumber, self.dicepips)
        Splitter.check_negative(self.dicenumber, self.dicepips)
        if self.dicenumber > 0 and self.dicepips > 0:
            resultlist = list(())
            i = 0
            while (i < dicenumber):
                i += 1
                result = random.randint(1, dicepips)
                resultlist.append(result)
            return resultlist
        elif dicenumber > 10000:
            raise NotImplementedError("Too much to work with for now")

    def modify(self):
        """Apply a modifier on the diceroll, ex. + or -."""
        pass
    def reroll(self):
        """allow for rerolls of certain failed throws"""
        pass

class RollStandard(RollSuper):
    """roll (multiple) dice
    """
    def __init__(self):
        self.dicenumber = 1
        self.dicepips = 6
    pass

class RollRerolls(RollSuper):
    """ roll rerolls on certain dice
    """

class RollModified(RollSuper):
    """roll modified dice
    """


def rollnpc(self, diceamount, dicepips):
        pass


if __name__ == "__main__":
    roll = RollStandard()
    result = roll.roll(20, 20)
    print(str(result))