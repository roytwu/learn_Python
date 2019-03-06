"""
File name:   rodrigues.py
Developer:   wur
Description: symbolic computations for Rodrigues formula
"""
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp


import SO3  #* use custom module
eye3 = SO3.eye3


th, phi, psi = symbols("theta phi psi")
x, y, z      = symbols("x y z")
a1, a2, a3   = symbols("a1 a2 a3")


#* ----- Rodrigues Formula -----
a = (a1, a2, a3)
a_hat = SO3.hat(a)

#* both Rod1 and Rod2 are Rodrigues formula in different form 
#* compare them and print out the result
Rod1 = cos(th)*eye3 + (1-cos(th))*(a_hat*a_hat+eye3) + sin(th)*a_hat
Rod2 = eye3 + sin(th)*a_hat + (1-cos(th))*a_hat*a_hat
result = simp(Rod1-Rod2)
#pprint(result)


#* ----- OpenGL glRotate ----- 
glRot1 = SO3.glRotate(th, a)

#* verifies that glRotate is angle-axis rotation
res = simp(glRot1 -Rod2)
#pprint(res)

#* ----- rotation along basic axes -----
xx = (1, 0, 0)
yy = (0, 1, 0)
zz = (0, 0, 1)
glRot_x = SO3.glRotate(th, xx)
rod_x   = SO3.rodrigues(th, xx)
rot_x   = SO3.Rx(th)

pprint(glRot_x)
pprint(rod_x)
pprint(rot_x)








