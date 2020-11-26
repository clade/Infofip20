import numbers
import operator

class Expr(object):
    def __repr__(self):
        return self.display(parent=None)
    
    def __str__(self):
        return self.display(parent=None)

    def __mul__(self, other):
        return Prod(self, other)

    def __rmul__(self, other):
        return Prod(other, self)    
    
    def __add__(self, other):
        return Sum(self, other)

    def __radd__(self, other):
        return Sum(other, self)
    
    
    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)

    def evaluate(self, **kwd):
        raise Exception('Cannot evaluate {self.__class__.__name__}'.format(self=self))
        
  
    
class Node(Expr):
    pass

class Leave(Expr):
    pass

class Symbol(Leave):
    def __init__(self, name):
        assert isinstance(name, str), 'name should be a str'
        self.name = name

    def display(self, parent):
        return self.name
    
    def __repr__(self):
        return 'Symbol({})'.format(self.name)
    
    def evaluate(self, **kwd):
        try:
            return kwd[self.name]
        except KeyError:
            raise Exception('Cannot evaluate variable {self.name}'.format(self=self))    
        
class Number(Leave):
    def __init__(self, val):
        self.val = val

    def display(self, parent):
        return str(self.val) 
    
    def __repr__(self):
        return 'Number({})'.format(self.val)    

    def evaluate(self, **kwd):
        return self.val


class Function(Node):
    """ Function with an arbitrary number of arguments """
    pass

class BinaryOperator(Function):
    def __init__(self, arg1, arg2):
        if isinstance(arg1, numbers.Number):
            arg1 = Number(arg1)
        if isinstance(arg2, numbers.Number):
            arg2 = Number(arg2)
        self.arg1 = arg1
        self.arg2 = arg2
        
    def display(self, parent):
        parenthese=True
        if parent is None:# or isinstance(parent, MathFunction): 
            parenthese=False
        if isinstance(parent, BinaryOperator) and self.priority>=parent.priority:
            parenthese=False
        left = self.arg1.display(self)
        right = self.arg2.display(self)
        if parenthese:
            return f"({left} {self.operator_name} {right})"
        else:
            return f"{left} {self.operator_name} {right}" 
    
    def evaluate(self, **kwd):
        left = self.arg1.evaluate(**kwd)
        right = self.arg2.evaluate(**kwd)
        return self.operator_function(left, right)    
        
class Sum(BinaryOperator):
    operator_name = '+'
    operator_function = operator.add
    priority = 1

class Prod(BinaryOperator):
    operator_name = '*'
    operator_function = operator.mul
    priority = 2


class Div(BinaryOperator):
    operator_name = '/'
    operator_function = operator.truediv
    priority = 2

    
class Sub(BinaryOperator):
    operator_name = '-'
    operator_function = operator.sub    
    priority = 0

class UnaryOperator(Function):
    pass

class Neg(UnaryOperator):
    pass

