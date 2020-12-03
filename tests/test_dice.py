"""test the code.RollStandard -module."""
import unittest

from code import dice
from code.dice import RollStandard

class TestRollStandard(unittest.TestCase):
    def setUp(self):
        roll1 = RollStandard
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
        self.assertEqual((len(roll1.roll()) == 1), True)
        self.assertEqual((max(roll1.roll()) <= 6), True)
        for numb in self.numblist:    
            self.assertEqual((min(roll1.roll(numb, 100)) >= 1), True)
            self.assertEqual((max(roll1.roll(numb)) <= 6), True)
            self.assertEqual((len(RollStandard.roll(numb)) == numb), True)
            self.assertEqual((len(RollStandard.roll(numb, numb)) == numb), True)
            self.assertEqual((max(RollStandard.roll(numb, numb)) <= numb), True)
            for pips in self.pipslist:
                self.assertEqual((max(RollStandard.roll(numb, pips)) <= pips), True)
                self.assertEqual((len(RollStandard.roll(numb, pips)) == numb), True)
        # for char in self.charlist:
        #     self.assertRaises(TypeError, RollStandard.roll, char)
        #     self.assertRaises(TypeError, RollStandard.roll, char, char)
        #     for pips in self.pipslist:
        #         self.assertRaises(TypeError, RollStandard.roll, char, pips)
        #         self.assertRaises(TypeError, RollStandard.roll, pips, char)
        #     for floa in self.floalist:
        #         self.assertRaises(TypeError, RollStandard.roll, char, floa)
        #         self.assertRaises(TypeError, RollStandard.roll, floa, floa)
        # for nega in self.negalist:
        #     self.assertRaises(ValueError, RollStandard.roll, nega)
        #     self.assertRaises(ValueError, RollStandard.roll, nega, nega)
        #     for pips in self.pipslist:
        #         self.assertRaises(ValueError, RollStandard.roll, nega, pips)
        # for entry in self.frinlist:
        #     self.assertRaises(NotImplementedError, RollStandard.roll, entry)
        #     self.assertRaises(NotImplementedError, RollStandard.roll, entry, entry)

    def test_modify(self):
        pass

    def test_reroll(self):
        pass