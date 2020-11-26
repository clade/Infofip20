import unittest

from symbolic import *


class Test(unittest.TestCase):
    def test_str(self):
        x = Symbol('x')
        y = Symbol('y')
        self.assertEqual(str(x), 'x')
        self.assertEqual(str(x+y), 'x + y')
        self.assertEqual(str(Sin(x+y)), 'sin(x + y)')

    def test_evaluate(self):        
        x = Symbol('x')
        y = Symbol('y')
        expr = x + y
        self.assertEqual(expr.evaluate(x=1, y=5), 6)

# python -m unittest test_bis



