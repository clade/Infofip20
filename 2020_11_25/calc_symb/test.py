from symbolic import *
import math


x = Symbol('x')

assert str(x)=='x'

y = Symbol('y')

assert str(x+y)=='x + y'

expr = x + y

assert expr.evaluate(x=1, y=5)==6

assert evaluate(Sin(x), {'x':1})==math.sin(1)
