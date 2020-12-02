"""test the sample.functions.dice -module."""
import unittest
from code import dice

class TestRoll(unittest.TestCase):
    def setUp(self):
        notimplist = [101, 102, 103, 104, 1000, 10000, 1000000]
        valerrlist = [-6, -1, 0, ]
        typerrlist = ['a', '<df43rt', '3q4t34t09er', 0.4, 1.9, 10.123]
        pass 
    def tearDown(self):
        pass
    def test_roll_len(self):
        """Arg1 is number of dice, Arg2 is pips on the dice, default is 1d6"""
    #TODO iterate list of good/bad values, get right values.
        goodlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        for entry in goodlist:    
            self.assertEqual((len(dice.roll(entry)) == entry), True)
        for entry in goodlist:
            self.assertEqual((len(dice.roll(entry, entry)) == entry), True)
        self.assertEqual((len(dice.roll()) == 1), True)
        
            # self.assertEqual((len(dice.roll(20, 40)) == 20), True)
            # self.assertEqual((len(dice.roll(100, 100)) == 100), True)
            # self.assertEqual((len(dice.roll(1)) == 1), True)
            # self.assertEqual((len(dice.roll(1, 90000)) == 1), True)
            # self.assertEqual((len(dice.roll(1,30)) == 1), True)

    def test_roll_max(self):
        self.assertEqual((max(dice.roll()) <= 6), True)
        self.assertEqual((max(dice.roll(100)) <= 6), True)
        self.assertEqual((max(dice.roll(1, 10)) <= 10), True)
        self.assertEqual((max(dice.roll(100, 10)) <= 10), True)
        self.assertEqual((max(dice.roll(100, 1000)) <= 1000), True)
        self.assertEqual((max(dice.roll(100, 100000)) <= 100000), True)
        self.assertEqual((max(dice.roll(100, 20)) <= 20), True)

    def test_roll_min(self):
        self.assertEqual((min(dice.roll(100, 100)) >= 1), True)

    def test_roll_err(self):
    #throw error on string and float input
        with self.assertRaises(TypeError):
            dice.roll("a", "a")
        with self.assertRaises(TypeError):
            dice.roll("a", 10)
        with self.assertRaises(TypeError):
            dice.roll("a")
        with self.assertRaises(TypeError):
            dice.roll("a", 10.568)
        with self.assertRaises(TypeError):
            dice.roll(9.9, 1.5)
    # negatives and zeroes
        with self.assertRaises(ValueError):
            dice.roll(10, 0)
        with self.assertRaises(ValueError):
            dice.roll(-1, -1)
        with self.assertRaises(ValueError):
            dice.roll(-6, 1)
    #if more than 100 dice are rolled
        with self.assertRaises(NotImplementedError):
            dice.roll(101)
        with self.assertRaises(NotImplementedError):
            dice.roll(20000)
        with self.assertRaises(NotImplementedError):
            dice.roll(101,101)
        with self.assertRaises(NotImplementedError):
            dice.roll(102)
        with self.assertRaises(NotImplementedError):
            dice.roll(150000)