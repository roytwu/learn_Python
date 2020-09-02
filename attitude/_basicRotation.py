"""
Author:   Roy Wu
Description: Symbolic computations to test funcitons of mapping between 
             SO(3) and Redrigues formula
"""
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy.matrices import Transpose
from sympy          import simplify as simp
import numpy as np

import SO3  #* use custom module
eye3 = SO3.eye3

th, phi, psi = symbols("theta phi psi")
x, y, z      = symbols("x y z")
a1, a2, a3   = symbols("a1 a2 a3")


#* testing hat and vee map
a = (a1, a2, a3)
a_hat = SO3.hat(a)
aa = SO3.vee(a_hat)
#pprint(a_hat)
#pprint(aa)
#print('\n')       

#* ----- Rodrigues Formula -----
#* both Rod1 and Rod2 are Rodrigues formula in different form 
#* compare them and print out the result
Rod1 = cos(th)*eye3 + (1-cos(th))*(a_hat*a_hat+eye3) + sin(th)*a_hat
Rod2 = eye3 + sin(th)*a_hat + (1-cos(th))*a_hat*a_hat
result = simp(Rod1-Rod2)
#pprint(result)

#* ----- rotation along basic axes -----
Rz = SO3.Rz(psi) #* 1st rotation; o  -> B'
Ry = SO3.Ry(th)  #* 2nd rotation; B' -> B"
Rx = SO3.Rx(phi) #* 3rd rotation; B" -> B
R_OB = Rz*Ry*Rx  #* Tait-Byran 
#pprint(Rz)
#pprint(Ry)
#pprint(Rx)
#pprint(R_OB)


#* ----- Kinematic singularity -----
xBasis = Matrix([[1], [0], [0]])
yBasis = Matrix([[0], [1], [0]])
zBasis = Matrix([[0], [0], [1]])


Bp_y=Rz*yBasis
Bpp_x = Rz*Ry*xBasis
#pprint(Bpp_x)



combine = Matrix([[0, -sin(psi), cos(psi)*cos(th)], [0, cos(psi), sin(psi)*cos(th)], [1, 0, -sin(th)]])
cInv= combine.inv()

print("\nCombine is...")
pprint(simp(cInv))


















# Bp_y = (Rz)*yBasis
# print("Bp_y is...")
# pprint(Bp_y)

# Bpp_x = Rz*Ry*xBasis
# print("Bpp_x is...")
# pprint(Bpp_x)

# cInv = combine.inv()
# pprint(simp(cInv)) 
