"""
Author:      Roy Wu
Description: Symbolic computations for homogeneous transformation
History:     03/16/2021 - initial version
             
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
from homoTrans import hat    #* use custom module
from homoTrans import vee    #* use custom module



q1=q2=q3=0
r1= 13
r2=6

q1=0.3
q2=0.3

# #*---------- ----------
#*    forward kinematics
#*---------- ----------
T01 = hXform(0, np.pi/2, r1, np.pi/2+q1)
T12 = hXform(0, np.pi/2, 0, np.pi+q2)
T23 = hXform(0, 0, r2+q3, 0)
T03 = multi_dot([T01, T12, T23]).round(2)
pprint(T03)

#*---------- ----------
#*    Find the z axes for Jacobian
#*---------- ----------
#* extract SO(3) from SE(3)
R01 = np.array(T01[0:3, 0:3]).round(2)
R12 = np.array(T12[0:3, 0:3]).round(2)
R23 = np.array(T23[0:3, 0:3]).round(2)


o1 = np.array([[T01[0,3]], [T01[1,3]], [T01[2,3]]])
o3 = np.array([[T03[0,3]], [T03[1,3]], [T03[2,3]]])
z = np.array([[0], [0], [1]])
zero = np.array([ [0], [0], [0]])
z1 = np.matmul(R01,z)
z2 = multi_dot([R01, R12, z]).round(2)
# pprint(z2)

Jd1 =np.matmul( hat(z), o3)
Jd2 = np.matmul(hat(z1), o3-o1)
Jd= np.hstack((Jd1, Jd2, z2)) #* horizontal matrix concatenation
Jw= np.hstack((z, z1, zero)) #* horizontal matrix concatenation
J= np.vstack((Jd, Jw))
print(J)





