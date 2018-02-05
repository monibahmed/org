import unittest
import doctest


def function(A, B):
    ''' Return the Summatation of two numbers
    >> > function(3, 4)
    7
    >> > function(10, 2)
    12
    '''

    return A + B


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(function(3, 4), 7)


def test_answer():
    assert function(3, 4) == 7
