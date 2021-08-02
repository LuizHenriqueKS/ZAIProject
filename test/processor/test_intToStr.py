from unittest import TestCase
import unittest

import ZAIProject as ai


class TestIntToStr(TestCase):
    def test(self):
        processor = ai.processor.IntToStr()
        self.assertEqual(processor.apply(10, None), '10')


if __name__ == '__main__':
    unittest.main()
