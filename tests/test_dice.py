"""test the code.RollStandard -module."""
import unittest

import code.functions.dice

class TestDice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_roll(self):
        self.assertEqual((len(code.functions.dice.roll()) == 1), True)
        self.assertEqual((max(code.functions.dice.roll()) <= 6), True)
        self.assertEqual((len(code.functions.dice.roll(30, 20))) == 30, True)
        self.assertEqual((len(code.functions.dice.roll(15,30))) == 20, False)
        
    def test_value_check(self):
        self.assertRaises(TypeError, code.functions.dice.check_numeric, "a", "aawc")
        self.assertRaises(TypeError, code.functions.dice.check_numeric, "ad", "awdd")
        
    def test_roll_modified(self):
        pass
    
    def test_roll_rerolls(self):
        pass