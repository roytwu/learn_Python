"""
File name:   quat.py
Developer:   wur
Description: Quaterinion operations
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


rot_x   = SO3.Rx(th)  #*creating rotation matrix
pprint(rot_x)

#* map SO(3) to S(3)
quat_x = SO3.SO3ToUnitQuat(rot_x)
print(quat_x)

result = SO3.unitQuatToSO3(quat_x)
pprint(simp(result))