"""
Author:      Roy Wu
Description: planar polar manipulator 
"""

import numpy as np
import sympy as sym
from numpy.linalg   import multi_dot
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import sin, cos
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform    #* use custom module
from homoTrans import hXformSym #* use custom module


r, th = symbols('r, theta')
a2, alpha2, d2, th2 = symbols('a_2, alpha_2, d_2, theta_2')
a3, alpha3, d3, th3 = symbols('a_3, alpha_3, d_3, theta_3')

#*---------- ----------
#*    polar manipulator
#*---------- ----------
jt1 = hXformSym(0, sym.pi/2, 0, (sym.pi)/2+th)
jt2 = hXformSym(0, 0, r, 0)
T = jt1*jt2
# # T = multi_dot([jt1, jt2]).round(3)
pprint(T)


