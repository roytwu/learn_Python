"""
Author:      Roy Wu
Description: homework problem 
"""
import numpy as np
from math import cos, sin

#*---------- ----------
#*    hw11
#*---------- ----------
angle = 20      #* in degrees 
atr = np.pi/180 #* angle to radian
Rz = np.matrix([ [np.cos(angle*atr), -np.sin(angle*atr), 0], 
               [np.sin(angle*atr), np.cos(angle*atr), 0], 
               [0,0,1] ])

#print(Rz) #* R_OB

angleFoo = np.arctan(3.5/2)/atr
#print("angleFoo is ...", angleFoo)

r2_O_length = np.sqrt(2*2+3.5*3.5)
r2_B_length = r2_O_length*np.cos((angleFoo-20)*atr)
#print (r2_B_length)


r2_B = np.matrix([[r2_B_length], [0], [0]])
#print (r2_B)

r2_O = Rz*r2_B
#print ("Result is ...\n", r2_O)


#*---------- ----------
#*    projection problem
#*---------- ----------
p1_O = np.array([[3], [8], [0]])
print(np.shape(p1_O))

# p1_O = np.array([3, 8, 0])
# print(np.shape(p1_O))

psi = 23*np.pi/180.
Rz = np.array([ [cos(psi), -sin(psi), 0], 
                [sin(psi), cos(psi), 0], 
                [0,0,1] ])
print(np.shape(Rz))

p1_B = np.matmul(Rz.transpose(), p1_O)
p2_B = np.array([p1_B[0], [0], [0]])
print(p2_B)
print(np.shape(p2_B))

p2_O = np.matmul(Rz, p2_B)
print('\np2_O is...\n', p2_O)




