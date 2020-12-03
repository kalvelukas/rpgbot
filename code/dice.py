#dice.py
"""take parameters and return a list of random numbers.
"""
import random

class RollSuper():
    """superclass
    """
    def check_negative(self, dicenumber: int = 1, dicepips: int = 1, modifier: int = 1):
        """take up to three variables, check >= 1"""
        if dicenumber > 0 and dicepips > 0:
            return
        else:
            raise ValueError("Can't roll less than one")
        pass
    def verify_type_integer(self, dicenumber, dicepips, modifier: int = 1):
        if isinstance(dicenumber, int) and isinstance(dicepips, int):
            return
        else:
            raise TypeError("Input not of Type Integer")
    def roll(self, dicenumber: int = 1, dicepips: int = 6, limit=10000) -> list:
        """Take 2 integers return as many as first integer random integers
        (max value <= second integer) as list.
        """
        self.dicenumber = dicenumber
        self.dicepips = dicepips
        self.verify_type_integer(self.dicenumber, self.dicepips)
        self.check_negative(self.dicenumber, self.dicepips)
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

if __name__ == "__main__":
    roll = RollStandard()
    result = roll.roll(20, 20)
    print(str(result))