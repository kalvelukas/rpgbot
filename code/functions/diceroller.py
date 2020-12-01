import random

def rolling (dicenumber: int = 1, dicepips: int = 6) -> list:
    resultlist = list(())
    if (dicenumber > 0 and dicepips > 0):
        i = 0
        while (i < dicenumber):
            i += 1
            result = random.randint(1, dicepips)
            resultlist.append(result)
        return resultlist
    else:
        raise ValueError