"""
Author:      Roy Wu
Description: multiplication of complex numbers, sympy version
https://docs.sympy.org/latest/modules/functions/elementary.html#sympy.functions.elementary.complexes.Abs
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
#*    polar coordinate
#*---------- ----------
# M4 = -5+9j
# M2 = -3+9j
# M5 = -7+9J
# M3 = -4+9j
# M1 = -1+9j
# mag =abs(M4)*abs(M2)/ (abs(M5)*abs(M3)*abs(M1))
# a = angle(M4)+angle(M2) - (angle(M5)+angle(M3)+angle(M1))
# print(mag)
# print(np.degrees(a).round(3))


a, b, c, d = symbols('a, b, c, d')
a=1
b=2
v1 = a+I*b
v2 = c+I*c

v1m = abs(v1)
v2a = arg(v1)
print(v2a)
