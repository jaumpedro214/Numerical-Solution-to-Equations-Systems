from sympy import *
import numpy as np

class Equation():

    def __init__(self, expressions, symbols):
        self.equation_expressions = expressions
        self.__symbols_set = symbols
        self.__equation_size = 0

        self.__init_equation_size()

    def __str__(self):
        str_result = "Equation "
        for expr in self.equation_expressions:
            str_result+="\n"+expr.__str__()+" = 0"

        return str_result

    def __getitem__(self, item):
        return self.equation_expressions[item]

    def __len__(self):
        return self.__equation_size

    @property
    def symbols_set(self):
        return self.__symbols_set

    def __init_equation_size(self):
        if( len( self.equation_expressions ) != len( self.__symbols_set ) ):
            print( "WARNING: Equation size and number of Symbols much match" )

        self.__equation_size = len( self.__symbols_set )

    def at(self, values):

        subs = { symbol:value for(symbol, value) in zip(self.__symbols_set, values) }
        result = [ float(expr.evalf(subs=subs)) for expr in self.equation_expressions ]
        result = np.array(result)

        return result

    @staticmethod
    def str_to_expression(str_list_expression):
        return [parse_expr(expr) for expr in str_list_expression]