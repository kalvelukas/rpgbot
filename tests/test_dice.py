"""test the code.RollStandard -module."""
import unittest

from code import functions
from code.functions import dice
from code.functions.dice import RollStandard

class TestRollStandard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.roll1 = RollStandard()
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

    def test_roll_standard(self):
        self.assertEqual((len(self.roll1.roll()) == 1), True)
        self.assertEqual((max(self.roll1.roll()) <= 6), True)
        for numb in self.numblist:
            self.assertEqual((min(self.roll1.roll(numb, 100)) >= 1), True)
            self.assertEqual((max(self.roll1.roll(numb)) <= 6), True)
            self.assertEqual((len(self.roll1.roll(numb)) == numb), True)
            self.assertEqual((len(self.roll1.roll(numb, numb)) == numb), True)
            self.assertEqual((max(self.roll1.roll(numb, numb)) <= numb), True)
            for pips in self.pipslist:
                self.assertEqual((max(self.roll1.roll(numb, pips)) <= pips), True)
                self.assertEqual((len(self.roll1.roll(numb, pips)) == numb), True)
        # for char in self.charlist:
        #     self.assertRaises(TypeError, self.roll1.roll, char)
        #     self.assertRaises(TypeError, self.roll1.roll, char, char)
        #     for pips in self.pipslist:
        #         self.assertRaises(TypeError, self.roll1.roll, char, pips)
        #         self.assertRaises(TypeError, self.roll1.roll, pips, char)
        #     for floa in self.floalist:
        #         self.assertRaises(TypeError, self.roll1.roll, char, floa)
        #         self.assertRaises(TypeError, self.roll1.roll, floa, floa)
        # for nega in self.negalist:
        #     self.assertRaises(ValueError, self.roll1.roll, nega)
        #     self.assertRaises(ValueError, self.roll1.roll, nega, nega)
        #     for pips in self.pipslist:
        #         self.assertRaises(ValueError, self.roll1.roll, nega, pips)
        # for entry in self.frinlist:
        #     self.assertRaises(NotImplementedError, self.roll1.roll, entry)
        #     self.assertRaises(NotImplementedError, self.roll1.roll, entry, entry)

    def test_roll_modified(self):
        pass

    def test_roll_rerolls(self):
        pass