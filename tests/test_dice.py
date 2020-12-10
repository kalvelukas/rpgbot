"""test the code.functions.dice -module."""
import unittest

from code.functions.dice import roll as roll_test
from code.functions.dice import check_numeric as check_numeric_test

class TestDice(unittest.TestCase):
    """TestClass for """
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
        """test the roll"""
        self.assertEqual((len(roll_test()) == 1), True)
        self.assertEqual((max(roll_test()) <= 6), True)
        self.assertEqual((len(roll_test(30, 20))) == 30, True)
        self.assertEqual((len(roll_test(15,30))) == 20, False)

    def test_value_check(self):
        """Test type checker"""
        self.assertRaises(TypeError, check_numeric_test, "a", "aawc")
        self.assertRaises(TypeError, check_numeric_test, "ad", "awdd")

    def test_roll_modified(self):
        """test roll modifier"""

    def test_roll_rerolls(self):
        """test reroller"""
