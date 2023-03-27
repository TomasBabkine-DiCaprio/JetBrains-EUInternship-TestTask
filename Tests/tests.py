import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import unittest
from script import calculate_study_time

class Test01(unittest.TestCase):

    def test_calculate(self):
        expected = {
            4: [1.3333333333333333, 3, 3], 
            0: [1.4285714285714286, 7, 1], 
            1: [1.4285714285714286, 7, 0], 
            3: [1.5, 4, 0], 
            2: [1.6, 5, 0]
        }

        N = 4
        M = 5
        L = 10
        topics = [[10, 7], [10, 7], [8, 5], [6, 4], [4, 3]]

        print('Test 01: calculate_study_time constructs the right dictionary')
        result = calculate_study_time(N, M, topics)
        self.assertEqual(result, expected)

class Test02(unittest.TestCase):

    def test_calculate(self):
        expected = { 
            0: [1, 1, 1], 
            1: [1, 1, 1], 
            3: [1, 1, 1], 
            2: [1, 1, 1],
            4: [1, 1, 1]
        }

        N = 5
        M = 5
        L = 5
        topics = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

        print('Test 02: calculate_study_time constructs the right dictionary when all topics take the same time to cover')
        result = calculate_study_time(N, M, topics)
        self.assertEqual(result, expected)

class Test03(unittest.TestCase):

    def test_calculate(self):
        expected = { 
            0: [1, 1, 0], 
            1: [1, 1, 0], 
            3: [1, 1, 0], 
            2: [1, 1, 0],
            4: [1, 1, 0]
        }

        N = 0
        M = 5
        L = 1
        topics = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

        print('Test 03: calculate_study_time constructs the right dictionary when N = 0')
        result = calculate_study_time(N, M, topics)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()