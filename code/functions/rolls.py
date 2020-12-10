"""Class collection for Rolls
"""

class RollSuper():
    """Parent for different types of rolls"""
    def __init__(self):
        self.dicenumber = 1
        self.dicepips = 6

class RollStandard(RollSuper):
    """roll (multiple) dice, inherit from RollSuper
    """

class RollRerolls(RollSuper):
    """ roll rerolls on certain dice
    """

class RollModified(RollSuper):
    """roll modified dice
    """

class RollMonster(RollSuper):
    """rolling fiends
    """

class RollNpc(RollSuper):
    """rolling NPCs
    """
