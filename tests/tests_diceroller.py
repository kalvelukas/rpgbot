import unittest

import sample
from sample.functions import diceroller
from sample.functions.diceroller import diceroller

class TestRoll(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return

    @classmethod
    def tearDownClass(cls):
        return

    def setUp(self):
        self.diceroll = ""    

    def tearDown(self):
        pass

    def test_roll(self):
        result = diceroller()
        self.assertEqual(result == 1, "true")

    def test_splitter(self):
        pass



if __name__ == "__main__":
    unittest.main()