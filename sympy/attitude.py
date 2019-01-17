"""
File name:   attitude.py
Date:        Created on Thur Jan 17 2019
Author:      wur
Description: symbolic computations for rotation matrices
"""

from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp

al, be, ga      = symbols("alpha beta gamma")
g               = symbols("g")
ax, ay, az      = symbols("ax ay az")

Rx = Matrix([ [1,0,0], [0, cos(al), -sin(al)], [0, sin(al), cos(al)] ])
Ry = Matrix([ [cos(be), 0, sin(be)], [0,1,0], [-sin(be), 0, cos(be)] ])
Rz = Matrix([ [cos(ga), -sin(ga), 0], [sin(ga), cos(ga), 0], [0,0,1] ])


bRg = Rx*Ry*Rz #Euler angle
aE = Matrix([ [0], [0], [-g]  ])  #gravitational acceleration in global frame
a = bRg*aE  #gravitational accerlation in body fixed frame
pprint(simp(a))

al = atan2(-ay,az)
be = asin(-ax/g)
 
expr = bRg.subs(ga,0) #evaluate bRg at gamma=0
pprint(expr)

