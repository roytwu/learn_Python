"""
Author:      Roy Wu
Description: Stanford manipulator
History:     02/16/2021 - intial version
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


# a1, alpha1, d1, th1 = symbols('a_1, alpha_1, d_1, theta_1')
# a2, alpha2, d2, th2 = symbols('a_2, alpha_2, d_2, theta_2')
# a3, alpha3, d3, th3 = symbols('a_3, alpha_3, d_3, theta_3')
# th4, th5, th6, d6 = symbols('theta_4, theta_5, theta_6, d_6')


#*---------- ----------
#*    Robot specs
#*---------- ----------
d2 =5
d6 =5


#*---------- ----------
#*    Joint vairables
#*---------- ----------
th1=th2=d3=th4=th5=th6=0


#*---------- ----------
#*    forward K
#*---------- ----------
jt1 = hXform(0, -np.pi/2, 0, th1)
jt2 = hXform(0, np.pi/2, d2, th2)
jt3 = hXform(0, 0, d3, 0)
jt4 = hXform(0, -np.pi/2, 0, th4)
jt5 = hXform(0, np.pi/2, 0, th5)
jt6 = hXform(0, 0, d6, th6)
T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6]).round(3)
pprint(T)