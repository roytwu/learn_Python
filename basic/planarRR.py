"""
Author:      Roy Wu
Description: planar RR manipulator 
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy        import linalg
from scipy.linalg import expm, sinm, cosm
from math import sin, cos, acos, atan, atan2
from math import radians, degrees
 

#*---------- ----------
#*    forwardK 
#*---------- ----------
l1=3     #* link 1
l2=1     #* link 2
th1=60   #* joint variable 1 in degrees
th2=-150  #* joint variable 2 in degrees
th1 = radians(th1) #* convert degree to radians
th2 = radians(th2)
x = l1*cos(th1) +l2*cos(th1+th2)
y = l1*sin(th1) +l2*sin(th1+th2)
x=round(x, 5)
y=round(y, 5)
print('posiiton is...', x, y)

#*---------- ----------
#*    invK - arc-cosine 
#*---------- ----------
cosN = x**2+y**2-l1**2-l2**2
cosD = 2*l1*l2 
d = cosN/cosD
t2 = acos(d)
t2 = degrees(t2)
t2 = round(t2, 5)
print('(invK, acos) theta2 is...', t2)

#*---------- ----------
#*    invK arc-tangent, half angle formula
#*---------- ----------
dum1 = (1-d)/(1+d)
dum1 = math.sqrt(dum1)
toto = degrees(atan(dum1)*2)
print('\n(invK, half-angle atan) theta2 is...', toto)


#*---------- ----------
#*    invK arc-tangent (method2)
#*---------- ----------
ntor = math.sqrt(1-d**2)
dtor = d 
toto = degrees(atan(ntor/dtor))
print('(invK, atan) theta2 is...', toto)



#*---------- ----------
#*    invK atan2
#*---------- ----------
tata = degrees(atan2(ntor, dtor))
print('(invK, atan2) theta2 is...', tata)


