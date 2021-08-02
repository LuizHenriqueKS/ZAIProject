import unittest
from ZAIProject.utility import getMinValue


class TestGetMinValue(unittest.TestCase):
    def test(self):
        matrix = [[1, 2], [3, 4]]
        expected = 1
        result = getMinValue(matrix)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
