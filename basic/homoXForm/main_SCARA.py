"""
Author:      Roy Wu
Description: Symbolic computations for homogeneous transformation
History:     02/25/2021 - initial version
             
"""
import numpy as np
import sympy as sym
from numpy.linalg   import multi_dot
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import nsimplify as nsimp
from sympy          import sin, cos, pi
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform #* use custom module
from homoTrans import hXformSym #* use custom module
from homoTrans import hatSym #* use custom module
from homoTrans import veeSym #* use custom module


th1, th2, th3, th4 = symbols('theta_1, theta_2, theta3, theta_4')
l0, l1, l2 = symbols('l0, l1, l2')


#* sanity check - zero position
th1=th2=th3=th4=0


#* testing prismatic joint
th4=2
# th2=th3=0

# #*---------- ----------
#*    forward kinematics
#*---------- ----------
jt1 = hXformSym(0, 0, l0, th1)
jt2 = hXformSym(l1, 0, 0, th2+pi/2)
jt3 = hXformSym(l2, 0, 0, th3)
jt4 = hXformSym(0, 0, -th4, 0)
T= jt1*jt2*jt3*jt4
#T = multi_dot([jt1, jt2, jt3, ht4]).round(3)
pprint(simp(T))






