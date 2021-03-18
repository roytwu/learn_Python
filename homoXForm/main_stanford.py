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
from sympy          import nsimplify as nsimp #* numerical simplification
from sympy          import sin, cos
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform #* use custom module
from homoTrans import hXformSym #* use custom module
from homoTrans import hatSym #* use custom module
from homoTrans import veeSym #* use custom module


d2, d3, d6    = symbols('d_2, d_3, d_6')
th1, th2, th3 = symbols('theta_1, theta_2, theta_3')
th4, th5, th6 = symbols('theta_4, theta_5, theta_6')


#*---------- ----------
#*    Robot specs
#*---------- ----------
# d2 =5
# d6 =10


#*---------- ----------
#*    Joint vairables
#*---------- ----------

#* zero position
# th1=th2=d3=th4=th5=th6=0

# #* test case 1
# th2 = -np.pi/2
# th5 = np.pi/2
# d3=7


#*---------- ----------
#*    forward K
#*---------- ----------
#* numpy version
# T01 = hXform(0, -np.pi/2, 0, th1)
# T12 = hXform(0, np.pi/2, d2, th2)
# T23 = hXform(0, 0, d3, 0)
# T34 = hXform(0, -np.pi/2, 0, th4)
# T45 = hXform(0, np.pi/2, 0, th5)
# T56 = hXform(0, 0, d6, th6)
# T = multi_dot([T01, T12, T23, T34, T45, T56]).round(3)
# pprint(T)

#* sympy version
T01 = hXformSym(0, -np.pi/2, 0, th1)
T12 = hXformSym(0, np.pi/2, d2, th2)
T23 = hXformSym(0, 0, d3, 0)
T34 = hXformSym(0, -np.pi/2, 0, th4)
T45 = hXformSym(0, np.pi/2, 0, th5)
T56 = hXformSym(0, 0, d6, th6)
T = T01*T12*T23*T34*T45*T56
pprint(T)




#*---------- ----------
#*    Find the z axes for Jacobian
#*---------- ----------
#* extract SO(3) from SE(3)
R01 = Matrix([ T01[0:3, 0:3] ])
R12 = Matrix([ T12[0:3, 0:3] ])
R23 = Matrix([ T23[0:3, 0:3] ])
R34 = Matrix([ T34[0:3, 0:3] ])
R45 = Matrix([ T45[0:3, 0:3] ])


z= Matrix([ [0], [0], [1]])
z1 = R01*z #* z1 as seen from {0}
#display(z1)
# pprint(nsimp(z1, tolerance=0.1))

z2 = R01*R12*z #* z2 as seen from {0}
#display(z2)
# pprint(nsimp(z2, tolerance=0.1))

z3 = R01*R12*R23*z #* z3 as seen from {0}
#display(z3)
# pprint(nsimp(z3, tolerance=0.1))

z4 = R01*R12*R23*R34*z #* z4 as seen from {0}
#display(z4)
# pprint(nsimp(z4, tolerance=0.1))

z5 = R01*R12*R23*R34*R45*z #* z5 as seen from {0}
#display(z5)
pprint(nsimp(z5, tolerance=0.1))





