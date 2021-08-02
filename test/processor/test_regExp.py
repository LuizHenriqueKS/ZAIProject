from unittest import TestCase
import unittest

import ZAIProject as ai


class TestRegExp(TestCase):
    def test(self):
        processor = ai.processor.RegExp(r'(\d+)\+(\d+)')
        self.assertEqual(processor.apply('1+2'), ['1', '2'])


if __name__ == '__main__':
    unittest.main()
