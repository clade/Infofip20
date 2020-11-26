import math
import numbers

from .base import Function, Expr

class MathFunction(Function):
    def __init__(self, arg):
        if isinstance(arg, numbers.Number):
            arg = Number(arg)
        assert isinstance(arg, Expr)
        self.arg = arg
        
    def display(self, parent):
        return f'{self.function_name}({self.arg.display(self)})'

    def evaluate(self, **kwd):
        return getattr(math, self.function_name)(self.arg.evaluate(**kwd))
    
    
class Sin(MathFunction):
    function_name = 'sin'

class Cos(MathFunction):
    function_name = 'cos'

