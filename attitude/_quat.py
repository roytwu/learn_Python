"""
File name:   _quat.py
Developer:   wur
Description: Symbolic computations to test funcitons of mapping between 
             SO(3) and S(3) 
"""

from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy          import zeros
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp

th, phi, psi = symbols("theta phi psi")

#* use custom module
import SO3  
import S3

#* round tiny doubles to zero
def roundTinyDoubleToZero(Matx):
    out = zeros(3)
    for i in range(3):
        for j in range(3):
            if abs(Matx[i,j]) < 0.0000001:
                out[i,j] = 0.0
            else:
                out[i,j] = Matx[i,j]
    return out        

#* ----- Main program starts here -----
xx = (1, 0, 0)
yy = (0, 1, 0)
zz = (0, 0, 1)

#* creating random rotation matrix
rotA = SO3.Rx(1.0)* SO3.Ry(1.0) 
rotB = SO3.Rz(1.0)
pprint(rotA)

#* map SO(3) to S(3)
quatA = SO3.SO3ToUnitQuat(rotA)
quatB = SO3.SO3ToUnitQuat(rotB)
print(quatA)

rotA2 = SO3.unitQuatToSO3(quatA)
pprint(simp(rotA2))


#* ----- testing quaternion multiplication -----
rotC = rotA*rotB                        #* multiplication of SO(3)
quatC = S3.multiplication(quatA, quatB) #* multiplication of S(3)
rotCC = SO3.unitQuatToSO3(quatC)

print('\nShall obtain identity matrix... \n')
result = rotCC* rotC.T 
result = roundTinyDoubleToZero(result)
pprint(result)
