"""
Author:      Roy Wu
Description: Symbolic version of spatial RRP manipulator
History:     03/16/2021 - initial version
             
"""
import numpy as np
import numpy.lonalg.norm as norm
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


q1, q2, q3 = symbols('q1, q2, q3')
r1, r2 = symbols('r1, r2')
q1d, q2d, q3d = symbols('q1d, q2d, q3d')

#* sanity check - zero position
# q1=q2=q3=0
q3=4.44
r1= 13
r2=6
q1=np.radians(30)
q2=np.radians(106.7)

# #*---------- ----------
#*    forward kinematics
#*---------- ----------
T01 = hXformSym(0, pi/2, r1, pi/2+q1)
T12 = hXformSym(0, pi/2, 0, pi+q2)
T23 = hXformSym(0, 0, r2+q3, 0)
T03= T01*T12*T23
#T = multi_dot([jt1, jt2, jt3, ht4]).round(3)
pprint(simp(T03))

#*---------- ----------
#*    Find the z axes for Jacobian
#*---------- ----------
#* extract SO(3) from SE(3)
R01 = Matrix([ T01[0:3, 0:3] ])
R12 = Matrix([ T12[0:3, 0:3] ])
R23 = Matrix([ T23[0:3, 0:3] ])

o1 = Matrix([ T01[0:3, 3] ])
o3 = Matrix([ T03[0:3, 3] ])
z = Matrix([ [0], [0], [1]])
zero = Matrix([ [0], [0], [0]])
z1 = R01*z
z2 = R01*R12*z


Jd1 = hatSym(z)*(o3)
Jd2 = hatSym(z1)*(o3-o1)
Jd= Matrix.hstack(Jd1, Jd2, z2) #* horizontal matrix concatenation
Jw= Matrix.hstack(z, z1, zero) #* horizontal matrix concatenation
J= Matrix.vstack(Jd, Jw)
# pprint(simp(J))

# qdot= Matrix([ [q1d], [0], [0]])
qdot= Matrix([ [0], [q2d], [0]])
# qdot= Matrix([ [0], [0], [q3d]])
xdot = J*qdot
pprint(simp(xdot))



