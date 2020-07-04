# Numerical Solution to Equations Systems
 A Python based code to numerically solve generic equations systems.
 
## Problem description
 
This code solve numerically a system of generic (linear and non-linear) equations using Newton Method

![](https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20f_1%28x_1%2C%20x_2%2C%20...%2C%20x_n%29%20%3D%200%20%5C%5C%20f_2%28x_1%2C%20x_2%2C%20...%2C%20x_n%29%20%3D%200%20%5C%5C%20...%20%5C%5C%20f_n%28x_1%2C%20x_2%2C%20...%2C%20x_n%29%20%3D%200%20%5Cend%7Bmatrix%7D%5Cright.)

## Dependences

- ``` Python 3.8.3 ``` 
- ``` Python Numpy library ```
- ``` Python SymPy library ```

## How to use 
There two main files in this project `non_linear_equations.py` and `non_linear_solver.py`.

From they, you want import `Equation` and `EquationSolver`, respectively. 

### The Equation class
Equation class is a SymPy based class structured to store a set of equations and evaluate this system at a given point. 

1. **Constructor**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Recive a list of SymPy expressions an a tuple containing the set of symbols (in String) that compose the system

2. _Equation_.**str_to_expression**(string_expression_list)

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Recive a list of Strings and parse to SymPy expression
 
 Ex.
 ```python
 from non_linear_equations import Equation
 string_expressions = ["x**2 + y**2 + z**2 - 8",
                       "x**2 + y**2 - z**2",
                        "y**2 - x + z - 3"]
 expr = Equation.str_to_expression( string_expressions )
 ```
 
3. _obj_.**at**(_self_, values)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Evaluate the system in a given point

Ex.
```python
from non_linear_equations import Equation


expr = Equation.str_to_expression( ["x**2 + y**2 + z**2 - 8",
                                    "x**2 + y**2 - z**2",
                                    "y**2 - x + z - 3"])
expr = Equation( expr, ('x', 'y', 'z') )
eval = expr.at( (2,3,4) ) # Respect the given in the constructor
print(eval)
```

## The EquationSolver class

1. **Constructor**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Recive a Equation class

2. obj.**solve**(_self_, initial_values, stop_criterion, max_iterations = 30, stop_criterion_value = 0.01, generate_output_info = False [WIP])
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Solve a determinated Equation System and return the solution vector in Numpy.ndarray type.

This method is the core of the program, it will tries to solve the given sytem with Newton Method.
| Parameter            |                       Meaning | Default value  |
|----------------------|----------------------------------------------------------------------------------------------------------------|---|
| initial_values       | The initial values of method aproximation, should be close enough to the real solution to garantee convergence | - |
| stop_criterion       | Should be _EquationSolver_.max_relative_error or  _EquationSolver_.max_absolute_error                          | - |
| max_iterations       | The max number of steps to tries hit the stop_criterion  before the method returns                             | 30 |
| stop_criterion_value | The values that the stop_criterion needs to get to reach the convergence and return a solution                 | 0.01|

