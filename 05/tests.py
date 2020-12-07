import unittest
from main import answer_one, answer_two
from main import Boarding_Pass

class BoardingPassTest(unittest.TestCase):

    def testFromString(self):
        bp = Boarding_Pass.from_string('FBFBBFFRLR')
        pass

    def testCalculationTwo(self):
        pass

if __name__ == "__main__": 
    unittest.main()