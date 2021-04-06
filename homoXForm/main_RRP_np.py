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



# q1=q2=q3=0
r1= 13
r2=6

q1=np.radians(30)
q2=np.radians(-90-16.7)
q3=4.44


# #*---------- ----------
#*    forward kinematics
#*---------- ----------
T01 = hXform(0, np.pi/2, r1, np.pi/2+q1).round(5)
T12 = hXform(0, np.pi/2, 0, np.pi+q2).round(5)
T23 = hXform(0, 0, r2+q3, 0).round(5)
T03 = multi_dot([T01, T12, T23]).round(3)
print("T is...")
pprint(T03)

#*---------- ----------
#*    Find the z axes for Jacobian
#*---------- ----------
#* extract SO(3) from SE(3)
R01 = np.array(T01[0:3, 0:3])
R12 = np.array(T12[0:3, 0:3])
R23 = np.array(T23[0:3, 0:3])


o1 = np.array([[T01[0,3]], [T01[1,3]], [T01[2,3]]])
o3 = np.array([[T03[0,3]], [T03[1,3]], [T03[2,3]]])
print("o3 is...")
pprint(o3)
z = np.array([[0], [0], [1]])
zero = np.array([ [0], [0], [0]])
z1 = np.matmul(R01,z)
z2 = multi_dot([R01, R12, z]).round(2)
print("z is...")
pprint(z2)

Jd1 =np.matmul( hat(z), o3)
Jd2 = np.matmul(hat(z1), o3-o1)
Jd= np.hstack((Jd1, Jd2, z2)) #* horizontal matrix concatenation
Jw= np.hstack((z, z1, zero))  #* horizontal matrix concatenation
J= np.vstack((Jd, Jw))
print("J is...", J)


qdot = np.array([[0], [1], [0]])
X = np.matmul(J, qdot)
print("X is...")
pprint(X)


#*---------- ----------
#*    Bonus
#*---------- ----------
p_C = np.array([[-4], [15], [3], [1]])
T_0C= np.array([ [1,0,0,-5], [0,0,1,8.66], [0,-1,0,25], [0,0,0,1]])
p_0 = multi_dot([T_0C, p_C]).round(5)
print("p0 is...")
pprint(p_0)

