from non_linear_equations import Equation
from non_linear_solver import EquationSolver


expr = Equation.str_to_expression( ["x**2 + y**2 + z**2 - 8",
                                    "x**2 + y**2 - z**2",
                                    "y**2 - x + z - 3"])
expr = Equation(expr, ('x', 'y', 'z'))

equation_solver = EquationSolver(expr)

solution = equation_solver.solve( (1.5, 2.1, 3.4),
                                  EquationSolver.max_relative_error,
                                  stop_criterion_value=0.1)

print(solution)