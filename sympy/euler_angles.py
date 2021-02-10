"""
Author:      Roy Wu
Description: symbolic computations for Euler angles
History:     01/17/2019 -- initial verison
             02/09/2021 -- revisit
"""

from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
import numpy as np

al, be, ga      = symbols("alpha beta gamma")
th, phi, psi    = symbols("theta phi psi")
g               = symbols("g")
ax, ay, az      = symbols("ax ay az")

Rx = Matrix([ [1,0,0], [0, cos(al), -sin(al)], [0, sin(al), cos(al)] ])
Ry = Matrix([ [cos(be), 0, sin(be)], [0,1,0], [-sin(be), 0, cos(be)] ])
Rz = Matrix([ [cos(ga), -sin(ga), 0], [sin(ga), cos(ga), 0], [0,0,1] ])

Rxx = Matrix([ [1,0,0], [0, cos(th), -sin(th)], [0, sin(th), cos(th)] ])
Ryy = Matrix([ [cos(phi), 0, sin(phi)], [0,1,0], [-sin(phi), 0, cos(phi)] ])
Rzz = Matrix([ [cos(psi), -sin(psi), 0], [sin(psi), cos(psi), 0], [0,0,1] ])


#*---------- ----------
#*    Euler angle x-y-z
#*---------- ----------
bRg = Rx*Ry*Rz 
print("---------\n")
pprint(bRg)
print("---------\n")
aE = Matrix([ [0], [0], [-g]  ])  #*gravitational acceleration in global frame
a = bRg*aE  #*gravitational accerlation in body fixed frame
pprint(simp(a))

#*result
al = atan2(-ay,az)
be = asin(-ax/g)
 
expr = bRg.subs(ga,0) #evaluate bRg at gamma=0
pprint(expr)


#*---------- ----------
#*    Euler angle z-y-x
#*---------- ----------
bRg2 = Rzz*Ryy*Rxx 
print("---------\n")
pprint(bRg2)
print("---------\n")
#* gravitational accerlation in body fixed frame
#* see _note_CGM for details
a2 = (bRg2).T * aE  
pprint(simp(a2))

#* ywa from magnetometer
Ryx= simp(Ryy*Rxx)
Rbm = Matrix([ [1,0,0], [0, -1, 0], [0, 0, -1] ])
pprint(simp(Ryx*Rbm));



#*---------- ----------
#*    Euler angle z-x-z (procession-nutation-spin)
#*---------- ----------
phi = 35 * np.pi/180
th  = 100 * np.pi/180
psi = 75 * np.pi/180

phi = 90 * np.pi/180
th  = 40 * np.pi/180
psi = 160 * np.pi/180

pre  = Matrix([ [cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0,0,1] ])
nut  = Matrix([ [1,0,0], [0, cos(th), -sin(th)], [0, sin(th), cos(th)] ])
spin = Matrix([ [cos(psi), -sin(psi), 0], [sin(psi), cos(psi), 0], [0,0,1] ])

R_OB = pre*nut*spin    #* sympy multiplication
# R_OB = R_OB.evalf(3)   #* round off 
pprint(simp(R_OB))


ans1 = R_OB.inv()
ans2 = R_OB.transpose()
print(simp(ans1-ans2))

















