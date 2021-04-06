"""
Author:      Roy Wu
Description: Symbolic computations of mapping between SO(3) and S(3) 
History:     10/xx/2020 - initial version
             04/06/2021 - ambibuity 
             (difficulty of using tuple shall be fixed in the future)
"""

import math
import numpy as np
from numpy.linalg   import norm
from sympy          import symbols
from sympy          import sin, cos, tan, cot
from sympy          import asin, acos, atan, atan2
from sympy          import zeros
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import nsimplify as nsimp

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


#*---------- ----------
#*    creating random rotation matrices
#*---------- ----------
rotA = SO3.Rx(1.0)* SO3.Ry(1.0) 
rotB = SO3.Rx(math.pi/6.0)
print('rototation matrix is...')
pprint(nsimp(rotB, tolerance=0.1))


#*---------- ----------
#*    Map SO(3) to S^3
#*---------- ----------
quatA = SO3.SO3ToUnitQuat(rotA)
quatB = SO3.SO3ToUnitQuat(rotB)
print('\nquaternion is...')
print(quatB)


#*---------- ----------
#*    Map S^3 to SO(3)
#*---------- ----------
# quatBn = (-quatB[0], -quatB[1], -quatB[2], -quatB[3]) #* ambiguity
rotB2 = SO3.unitQuatToSO3(quatB)
print('\nConverting S^3 back to SO(3)...')
pprint(simp(rotB2))




#*---------- ----------
#*    quaternion multiplication
#*---------- ----------
rotC = rotA*rotB                        #* multiplication of SO(3)
quatC = S3.multiplication(quatA, quatB) #* multiplication of S(3)
rotCC = SO3.unitQuatToSO3(quatC)

print('\n\nShall obtain identity matrix... \n')
result = rotCC* rotC.T 
out = nsimp(result, tolerance=0.001, rational=True)
pprint(out)
