"""
File name:   main_quat.py
Developer:   wur
Description: Symbolic computations to test funcitons of mapping between 
             SO(3) and S(3) 
"""
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp

th, phi, psi = symbols("theta phi psi")

#* use custom module
import SO3  

xx = (1, 0, 0)
yy = (0, 1, 0)
zz = (0, 0, 1)


rot   = SO3.Rx(th)  #*creating rotation matrix
pprint(rot)

#* map SO(3) to S(3)
quat = SO3.SO3ToUnitQuat(rot)
print(quat)

rot_2 = SO3.unitQuatToSO3(quat)
pprint(simp(rot_2))