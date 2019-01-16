"""
File name:   rottion.py
Date:        Created on Wed Jan 16 16:36:31 2019
Author:      wur
Description: symbolic computations for rattion matrices
"""
#import mpmath
import sympy as sym
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy.printing import pprint
from sympy.matrices import Matrix

psi, phi, theta = symbols("psi phi theta")
theta = sin(psi)+1
pprint(theta)



I = Matrix([ [cos(psi),0,0],[0,1,0], [0,0,1] ])
pprint(I)

