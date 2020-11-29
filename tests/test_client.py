import unittest
import shadowlib

class TestClient(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        return

    @classmethod
    def tearDownClass(cls):
        return

    def setUp(self):
        self.diceroll = str("40d6s5")
        pass

    def tearDown(self):
        pass

    def test_roll(self):
        self.assertTrue(len(shadowlib.funclib.roll.rollplayer(self, self.diceroll)) > 50)
        pass

    def test_splitter(self):
        pass



if __name__ == "__main__":
    unittest.main()