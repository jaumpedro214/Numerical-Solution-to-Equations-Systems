from non_linear_equations import Equation
import numpy as np
import numpy.linalg
from sympy import diff

class EquationSolver():

    def __init__(self, equation ):
        self.equation = equation

        self.__jacobian_matrix = np.ndarray( shape=(len(equation), len(equation)), dtype = type(equation) )
        self.__initiate_jacobian_matrix()

    def __initiate_jacobian_matrix(self):

        iter = 0
        for column in self.__jacobian_matrix:
            atual_symbol_diff = self.equation.symbols_set[iter]
            self.__jacobian_matrix[:,iter] = [ diff(expr, atual_symbol_diff ) for expr in self.equation ]
            iter +=1

    def solve(self,
              initial_values,
              stop_criterion,
              max_iterations = 30,
              stop_criterion_value = 0.01,
              generate_output_info = False):

        method_converged = False
        old_values = initial_values

        log_output = []
        if( generate_output_info ):
            log_output.append( np.array( old_values ) )

        for i in range( max_iterations ):
            new_values = self.__next_iter( old_values )

            error_value = stop_criterion(new_values, old_values)

            old_values = new_values

            if( error_value <= stop_criterion_value ):
                method_converged = True
                break

        if( method_converged == False ):
            print( "WARNING: Method did not converge")

        return new_values

    def __next_iter(self, old_values):
        return old_values + self.__evaluate_determinants_vector(old_values)

    def __evaluate_determinants_vector(self, values):
        jacobian_matrix = self.__evaluate_jacobian_at( values )
        equation_value = -1*self.equation.at(values)
        result = np.linalg.solve( jacobian_matrix, equation_value  )

        return result

    def __evaluate_jacobian_at(self, values):
        subs = { symbol:value for(symbol, value) in zip(self.equation.symbols_set, values) }
        result = [ [ float( expr.evalf(subs=subs) ) for expr in row ] for row in self.__jacobian_matrix ]
        return np.array( result )

    @classmethod
    def max_absolute_error(cls, values1, values2 ):
        return np.max( np.abs( values1-values2 ) )

    @staticmethod
    def max_relative_error(values1, values2):
        return np.max(np.abs( (values1 - values2)/values1 ) )

    @property
    def jacobian_matrix(self):
        return self.__jacobian_matrix