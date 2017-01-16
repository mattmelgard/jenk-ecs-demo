from unittest import TestCase
import unittest
from main import main


class TestMain(TestCase):
    def test_main(self):
        output = main()
        self.assertEqual(output, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
