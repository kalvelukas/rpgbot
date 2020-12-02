#dice.py
"""take parameters and return a list of random numbers.
"""
import random

def roll (dicenumber: int = 1, dicepips: int = 6, limit=100) -> list:
    """Take 2 integers return as many as first integer random integers
       (max value <= second integer) as list.
       """
    if isinstance(dicenumber, int) and isinstance(dicepips, int):
        if dicenumber <= 100:
            if (dicepips > 0 and dicenumber > 0):
                resultlist = list(())
                i = 0
                while (i < dicenumber):
                    i += 1
                    result = random.randint(1, dicepips)
                    resultlist.append(result)
                return resultlist
            elif (dicenumber == 0 or dicepips == 0):
                raise ValueError("Can't roll Zeros")
            else:
                raise ValueError("Can't roll negatives")
        else:
            raise NotImplementedError("Too much to display for now")
    else:
        raise TypeError

def modify ():
    """Apply a modifier on the diceroll, ex. + or -."""
    pass

def reroll ():
    """allow for rerolls of certain failed throws"""
    pass

# if __name__ == "__main__":
#     result = roll(int(input()), int(input()))
#     print(str(result))