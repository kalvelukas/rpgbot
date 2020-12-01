"""test the sample.functions.dice -module."""
import unittest
from code import dice

class TestRoll(unittest.TestCase):
    def setUp(self):
        pass 
    def tearDown(self):
        pass
    def test_roll(self):
        """Arg1 is number of dice, Arg2 is pips on the dice, default is 1d6"""
        self.assertEqual((len(dice.roll(50)) == 50), True)
        self.assertEqual((len(dice.roll(20, 40)) == 20), True)
        self.assertEqual((len(dice.roll(100, 100)) == 100), True)
        self.assertEqual((len(dice.roll()) == 1), True)
        self.assertEqual((len(dice.roll()) == 1), True)

        self.assertEqual((max(dice.roll(100)) <= 6), True)
        self.assertEqual((max(dice.roll(1, 10)) <= 10), True)
        self.assertEqual((max(dice.roll(100, 10)) <= 10), True)
        self.assertEqual((max(dice.roll(100, 1000)) <= 1000), True)
        self.assertEqual((max(dice.roll(100, 100000)) <= 100000), True)
        self.assertEqual((max(dice.roll(100, 20)) <= 20), True)

        self.assertEqual((min(dice.roll(100, 100)) >= 1), True)

        with self.assertRaises(TypeError):
            #throw error on string and float input
            dice.roll("a", "a")
            dice.roll("a", 10)
            dice.roll("a")
            dice.roll(9.9, 1.5)

        with self.assertRaises(ValueError):
            # negatives and zeroes
            dice.roll(10, 0)
            dice.roll(-1, -1)
        
        with self.assertRaises(NotImplementedError):
            #if more than 100 dice are rolled
            dice.roll(101)
            dice.roll(20000)
            #FIXME Test passes for the following. Why?
            dice.roll(1,101)
            dice.roll(1, 1)
            dice.roll()

"""TODO input/output test for the diceroller module
- arguments: none OR diceamount and dicepips

- testcases:
  --default: no args given, return 1 result 1=<r<=6
  --positive fringe: diceamount 100/101/150000, dicepips 100/101/200/201/150000
    -->throw value error on greater 100
  --negative fringe: diceamount -6/-1/0, dicepips -6/-1/0 -> throw error
"""
