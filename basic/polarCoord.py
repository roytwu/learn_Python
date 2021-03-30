"""
Author:      Roy Wu
Description: multiplication of complex numbers, numpy version

"""
import math
import matplotlib.pyplot as plt
import numpy             as np
import sympy             as sym
from numpy        import linalg
from numpy        import angle
from scipy.linalg import expm, sinm, cosm
from pprint       import pprint 
from sympy          import Abs, arg, I
from sympy          import nsimplify as nsimp
from sympy          import simplify as simp
from sympy          import sin, cos, pi
from sympy          import symbols


#*---------- ----------
#*    Express a complex number in terms of magnitude and angle
#*    (polar coordinate)
#*---------- ----------
def magAng(complexNum):
    mag = abs(complexNum)         #* magnitude of the complex number
    ang = angle(complexNum, True) #* angle in degrees
    
    mag = round(mag, 3)
    ang = round(ang, 3)
    
    out = [mag, ang]
    return out
    
#*---------- ----------
#*    main program
#*---------- ----------
v1 = -5+9j
v2 = -1+9j

v1_m = magAng(v1)[0]
v1_a = magAng(v1)[1]
v2_m = magAng(v2)[0]
v2_a = magAng(v2)[1]

#*---------- ----------
#*    apporach 1
#*---------- ----------
v3 = v1*v2
ans1 = magAng(v3)
print('ans1 is...', ans1)
 

#*---------- ----------
#*    apporach 2
#*---------- ----------
v3_m = v1_m*v2_m  #*scale 
v3_a = v1_a+v2_a  #*rotation
print ('ans2 is...', v3_m, v3_a)


