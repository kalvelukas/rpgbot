#dice.py
"""take parameters and return a list of random numbers.
"""
# stlib
import random
import re

def limit_inputstring(inputstring: str):
    inputstring = inputstring[:20]
    if "m" and "r" and "s" in inputstring:
        return inputstring
    elif ("m" and "s") or ("m" and "s") or ("s" and "r") in inputstring:
        return inputstring[:16]
    elif "m" or "s" or "r" in inputstring:
        return inputstring[:12]
    elif "d" in inputstring:
        return inputstring[:8]
    else:
        return "1d6"

def check_inputstring(inputstring):
    # return inputstring
    pass

def split_inputstring(inputstring):
    """Split String Input"""
    # splithelp = str(inputstring.split("d")[1])
    # if ("s" in splithelp):
    #     dicepips = splithelp.split("s")[0]
    #     desire = diceroll.split("s")[1]
    # else:
    #     dicepips = diceroll.split("d")[1]
    pass

def check_numeric(diceamount, dicepips):
    if diceamount.isnumeric() and dicepips.isnumeric():
        rollparams = list(())
        rollparams.append(int(diceamount))
        rollparams.append(int(dicepips))
        return rollparams
    else:
        raise TypeError

def check_roll_value(dicenumber, dicepips):
    """Check if roll value is between 1 and 99."""
    if dicenumber > 0 and dicepips > 0:
        return
    else:
        raise ValueError("Can't roll less than one")

def verify_type_integer(dicenumber, dicepips, modifier: int = 1):
    if isinstance(dicenumber, int) and isinstance(dicepips, int):
        return
    else:
        raise TypeError("Input not of Type Integer")


def roll(dicenumber: int = 1, dicepips: int = 6, limit=150) -> list:
    """Take 2 integers return as many as first integer random integers
    (max value <= second integer) as list.
    """
    resultlist = list(())
    i = 0
    while (i < dicenumber):
        i += 1
        result = random.randint(1, dicepips)
        resultlist.append(result)
    return resultlist

def modify():
    """Apply a modifier on the diceroll, ex. + or -"""
    pass

def reroll():
    """allow for rerolls of certain failed throws"""
    pass

def rollnpc(diceamount, dicepips):
    """Rolls of a NPC."""
    pass


# def rollplayer(diceroll):
#     if (("d" in diceroll) and len(diceroll) < 15):
#         params = splitter(diceroll)
#         if params == .errormsg:
#             return .errormsg
#         results = .roller(params)
#         formatted = .formatter(results, params)
#         return formatted
#     else:
#         raise ValueError

if __name__ == "__main__":
    print(limit_inputstring("awdpawdkpaowkdpodawdokapwkdpoawdkawpodkawpodkwapwadawdwadwa"))
    print(check_inputstring("651964151698512168484"))