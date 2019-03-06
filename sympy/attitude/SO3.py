"""
Developer:   Roy TWu
File Name:   SO3.py
Description: custom modules about attitude representation and transformation
"""

from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp

th, phi, psi = symbols("theta phi psi")
x, y, z      = symbols("x y z")
v1, v2, v3   = symbols("v1 v2 v3")

Rx = Matrix([ [1,0,0], [0, cos(th), -sin(th)], [0, sin(th), cos(th)] ])
Ry = Matrix([ [cos(phi), 0, sin(phi)], [0,1,0], [-sin(phi), 0, cos(phi)] ])
Rz = Matrix([ [cos(psi), -sin(psi), 0], [sin(psi), cos(psi), 0], [0,0,1] ])

eye3 = Matrix([ [1,0,0], [0, 1, 0], [0, 0, 1] ])

hat_v = Matrix([ [0,-v3, v2], [v3, 0, -v1], [-v2, v1, 0] ])

#* hat map
def hat(tup_v):
    v1 = tup_v[0]
    v2 = tup_v[1]
    v3 = tup_v[2]
    hatMap = Matrix([ [0,-v3, v2], [v3, 0, -v1], [-v2, v1, 0] ])   
    return hatMap 