import unittest
from ZAIProject.utility import getShape


class TestGetShape(unittest.TestCase):
    def test(self):
        sample = [[1, 2], [3, 4], [5, 6]]
        shape = getShape(sample)
        self.assertEqual(shape, [3, 2])


if __name__ == '__main__':
    unittest.main()
