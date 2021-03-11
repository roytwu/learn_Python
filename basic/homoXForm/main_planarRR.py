"""
Author:      Roy Wu
Description: planar RR manipulator 
History:     xx/xx/2020 - intial version
             03/11/2021 - updating with custom library 
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy        import linalg
from scipy.linalg import expm, sinm, cosm
# from math import sin, cos, acos, atan, atan2, sqrt
from math import radians, degrees

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
from homoTrans import hatSym    #* use custom module
from homoTrans import veeSym    #* use custom module



#*---------- ----------
#*    Forward Kinematics
#*---------- ----------
l1, l2   = symbols('l_1, l_2')
th1, th2 = symbols('theta_1, theta_2')

T01 = hXformSym(l1, 0, 0, th1)
T12 = hXformSym(l2, 0, 0, th2)
T02 = T01*T12
pprint(simp(T02))


#*---------- ----------
#*    Jacobian
#*---------- ----------
z = Matrix([ [0], [0], [1]])  #* z0
z2 = z1 = z
o0 = Matrix([ [0], [0], [0]]) 
o1 = Matrix([ [l1*cos(th1)], [l1*sin(th1)], [0]]) 
o2 = Matrix([ [l1*cos(th1)+l2*cos(th1+th2)], [l1*sin(th1)+l2*sin(th1+th2)], [0]]) 

Jd1 = hatSym(z)*(o2-o0)
Jd2 = hatSym(z1)*(o2-o1)

Jd= Matrix.hstack(Jd1, Jd2) #* horizontal matrix concatenation
Jw= Matrix.hstack(z, z1) #* horizontal matrix concatenation
J= Matrix.vstack(Jd, Jw)
pprint(simp(J))





