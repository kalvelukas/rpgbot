"""test the code.dice -module."""
import unittest

from code import dice

class TestRoll(unittest.TestCase):
    def setUp(self):
        self.numblist = list(range(1, 100, 5))
        self.pipslist = list(range(1, 10001, 100))
        self.frinlist = list(range(101, 10001, 100))
        self.modilist = list(range(1, 10))
        self.negalist = list(range(-104, 0, 5))
        self.floalist = [0.1, 12.1, 0.92851, 97872.742, 0.05]
        self.charlist = ["a","z", "b", "eface", "<@@////"]
        pass 

    def tearDown(self):
        pass

    def test_roll(self):
        self.assertEqual((len(dice.roll()) == 1), True)
        self.assertEqual((max(dice.roll()) <= 6), True)
        for numb in self.numblist:    
            self.assertEqual((min(dice.roll(numb, 100)) >= 1), True)
            self.assertEqual((max(dice.roll(numb)) <= 6), True)
            self.assertEqual((len(dice.roll(numb)) == numb), True)
            self.assertEqual((len(dice.roll(numb, numb)) == numb), True)
            self.assertEqual((max(dice.roll(numb, numb)) <= numb), True)
            for pips in self.pipslist:
                self.assertEqual((max(dice.roll(numb, pips)) <= pips), True)
                self.assertEqual((len(dice.roll(numb, pips)) == numb), True)
        # for char in self.charlist:
        #     self.assertRaises(TypeError, dice.roll, char)
        #     self.assertRaises(TypeError, dice.roll, char, char)
        #     for pips in self.pipslist:
        #         self.assertRaises(TypeError, dice.roll, char, pips)
        #         self.assertRaises(TypeError, dice.roll, pips, char)
        #     for floa in self.floalist:
        #         self.assertRaises(TypeError, dice.roll, char, floa)
        #         self.assertRaises(TypeError, dice.roll, floa, floa)
        # for nega in self.negalist:
        #     self.assertRaises(ValueError, dice.roll, nega)
        #     self.assertRaises(ValueError, dice.roll, nega, nega)
        #     for pips in self.pipslist:
        #         self.assertRaises(ValueError, dice.roll, nega, pips)
        # for entry in self.frinlist:
        #     self.assertRaises(NotImplementedError, dice.roll, entry)
        #     self.assertRaises(NotImplementedError, dice.roll, entry, entry)

    def test_modify(self):
        pass

    def test_reroll(self):
        pass