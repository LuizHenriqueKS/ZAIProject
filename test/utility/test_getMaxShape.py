import unittest
from ZAIProject.utility import getMaxShape


class TestGetMaxShape(unittest.TestCase):
    def test(self):
        shape1 = [1, 2]
        shape2 = [3, 4]
        maxShape = getMaxShape(shape1, shape2)
        self.assertEqual(maxShape, shape2)


if __name__ == '__main__':
    unittest.main()
