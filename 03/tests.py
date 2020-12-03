import unittest
from main import answer_one, answer_two
from main import Landscape

input_for_testing = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

class AoC03Test(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(7, answer_one(input_for_testing.splitlines()))

    def testCalculationTwo(self):
        answer = answer_two(input_for_testing.splitlines())
        self.assertEqual(336, answer)

    def testParsing(self):
        line = '#...#...#..'

        landscape = Landscape.extract_trees(line)

        expected_list = [True, False, False, False, True, False, False, False, True, False, False]

        self.assertListEqual(expected_list, landscape)


if __name__ == "__main__": 
    unittest.main()