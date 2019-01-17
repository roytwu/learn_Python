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
al, be, ga      = symbols("alpha beta gamma")

Rx = Matrix([ [1,0,0], [0, cos(al), -sin(al)], [0, sin(al), cos(al)] ])
Ry = Matrix([ [cos(be), 0, sin(be)], [0,1,0], [-sin(be), 0, cos(be)] ])
Rz = Matrix([ [cos(ga), -sin(ga), 0], [sin(ga), cos(ga), 0], [0,0,1] ])
#pprint(Rx)

#* use simplify() to get simplest form of an expression
pprint(simplify(Rx*Rx.T))

bRg = Rx*Rz*Ry
#pprint(bRg)


