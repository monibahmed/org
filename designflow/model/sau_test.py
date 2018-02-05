from sau import *

import unittest


class SauTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sau(1, 2, 3), 5)

    def test_sub(self):
        self.assertEqual(sau(2, 2, 3), -1)


if __name__ == '__main__':
    unittest.main()
