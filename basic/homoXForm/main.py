"""
Author:      Roy Wu
Description: Symbolic computations for homogeneous transformation
History:     xx/xx/2020 - intial version
             02/11/2021 - revisit
"""
import numpy as np
import sympy as sym
from numpy.linalg   import multi_dot
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import nsimplify as nsimp
from sympy          import sin, cos
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform #* use custom module
from homoTrans import hXformSym #* use custom module
from homoTrans import hatSym #* use custom module
from homoTrans import veeSym #* use custom module


a1, alpha1, d1, th1 = symbols('a_1, alpha_1, d_1, theta_1')
a2, alpha2, d2, th2 = symbols('a_2, alpha_2, d_2, theta_2')
a3, alpha3, d3, th3 = symbols('a_3, alpha_3, d_3, theta_3')

#* sanity check
# a1=a2=a3=1
# th1=th2=th3=0

# a1=a2=a3=5.0
# th1=np.pi/2.0
# th2=th3=0

# #*---------- ----------
# #*    RRR manipulator
# #*---------- ----------
# jt1 = hXform(a1, 0, 0, th1)
# jt2 = hXform(a2, 0, 0, th2)
# jt3 = hXform(a3, 0, 0, th3)
# T = multi_dot([jt1, jt2, jt3]).round(3)
# # pprint(T)



#*---------- ----------
#*    RR manipulator
#*---------- ----------
l1, l2 = symbols('l1, l2')
jt1 = hXformSym(l1, 0, 0, th1)
jt2 = hXformSym(l2, 0, 0, th2)
T = jt1*jt2
pprint(simp(T))




# #*---------- ----------
# #*    HW#6
# #*---------- ----------
# x= Matrix([ [3], [5], [-7]])
# y= Matrix([ [-1], [2], [3]])
# out = hatSym(x)*y
# pprint(out)

