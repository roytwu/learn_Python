"""
Author:      Roy Wu
Description: planar polar manipulator 
History:     xx/xx/2020 - intial version
             02/11/2021 - revisit, adding more comments 
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
from homoTrans import hatSym    #* use custom module
from homoTrans import veeSym    #* use custom module

r, th, thDot = symbols('r, theta, omega')
a2, alpha2, d2, th2 = symbols('a_2, alpha_2, d_2, theta_2')
a3, alpha3, d3, th3 = symbols('a_3, alpha_3, d_3, theta_3')

#*---------- ----------
#*    Forward Kinematics
#*---------- ----------
T01 = hXformSym(0, sym.pi/2, 0, (sym.pi)/2+th)
T12 = hXformSym(0, 0, r, 0)
T02 = T01*T12
pprint(T02)

#* extract rotation matrix to find angular velocity
R02 = Matrix([ T02[0:3, 0:3] ]) 
pprint(R02)

R02dot = Matrix([ [cos(th)*thDot, 0, -sin(th)*thDot], [-sin(th)*thDot, 0, cos(th)*thDot], [0, 0, 0]])

hatOmega = R02dot * R02.transpose()
omega = simp(veeSym(hatOmega)) #* angular velocity
pprint(omega)


#*---------- ----------
#*    Demo of hat map and vee map
#*---------- ----------
# vec = Matrix([ [a], [b], [c]])
# out = hatSym(vec)
# pprint(out)

# out2 = veeSym(out)
# pprint(out2)

