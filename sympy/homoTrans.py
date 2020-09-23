
import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import sin, cos
from sympy          import symbols



al, be, ga      = symbols("alpha beta gamma")
Rx = Matrix([ [1,0,0], [0, cos(al), -sin(al)], [0, sin(al), cos(al)] ])