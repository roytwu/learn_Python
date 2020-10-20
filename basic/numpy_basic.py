"""
Author:      Roy Wu
Description: Basic programming for numpy
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy        import linalg
from numpy        import angle
from scipy.linalg import expm, sinm, cosm
from pprint       import pprint 


#*---------- ----------
#*    matrix exponential  
#*---------- ----------
# a = np.arange(15).reshape(3,5) #* 3 rows x 5 columns
a = np.arange(9).reshape(3,3)    #* 3 rows x 3 columns
m1 = np.exp(a) 
ma = expm(a)
# print('Matrix a is...\n', a)
# print('\nElement-wise exponential is ...\n', m1)
# print('\nMatrix exponential is... ')
# pprint(ma)


#*---------- ----------
#*    matrix operation   
#*---------- ----------
toto = np.array([[1, 2], [4, 5]])
totoInv = linalg.inv(toto)
# print("inverse is...", totoInv)

 
output1 = toto.dot(totoInv)          #* AxB=A.dot(B) 
output2 = np.matmul(toto, totoInv)   
# print("output1 is...", output1)
# print("output2 is...", output2)
# print("output is...", totoInv*toto)  #* element-wise multiplication

totoT = toto.transpose()             #* matris transpose
# print("transpose is...", totoT)


tata = np.array([[math.cos(0.5), 0, math.sin(0.5)], [0, 1, 0], [-math.sin(0.5), 0, math.cos(0.5)]])
tataDet = linalg.det(tata)  #* determinant
lamb, v = linalg.eig(tata)
# print("eigenvalues are...", lamb)
# print("eigenvectors are...", v[0])

# I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# dumm1 = np.dot(lamb[0], I)
# print("dumm1...", dumm1)
# output = np.matmul((tata-dumm1), v[:,0])
# print('output is...', output)


#*---------- ----------
#*    Euler's identity  
#*---------- ----------
eu1 = expm(1j*a)
eu2 = np.exp(1j*a)
eu3 = cosm(a) + 1j*sinm(a)
# print(eu1-eu2)
# print(eu1-eu3) #* this shall output zero matrix

#*---------- ----------
#*    triggometric functions 
#*---------- ----------
# x = np.arange(0, 4*np.pi, 0.1) #* start, stop, step
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = y1**2+y2**2  #* power operator

# fig = plt.figure()
# # plt.plot(x,y1, x,y2, x,y3)
# plt.plot(x, y1, label = 'sine')
# plt.plot(x, y2, label = 'cosine')
# plt.xlabel('time')
# plt.ylabel('...')
# plt.title('Trigg functions')
# plt.legend()
# # plt.grid()

# # plt.show()
# plt.savefig('foo.pdf')

#*---------- ----------
#*    linearizing triggometric functions 
#*---------- ----------
x = np.linspace(0, math.pi*2, 50) #* start, stop, step
y = np.cos(x)
y2 = (1-x)*np.sqrt(2)/2
y3 = -1+0*x
fig = plt.figure()
plt.plot(x,y, 'b')
plt.plot(x,y2, 'r')
plt.plot(x,y3, 'c')


#*---------- ----------
#*    polar coordinate
#*---------- ----------
M4 = -5+9j
M2 = -3+9j
M5 = -7+9J
M3 = -4+9j
M1 = -1+9j
mag =abs(M4)*abs(M2)/ (abs(M5)*abs(M3)*abs(M1))
a = angle(M4)+angle(M2) - (angle(M5)+angle(M3)+angle(M1))
print(mag)
print(np.degrees(a))


#* example 2
zero1 = -4+0j
zero2 = -3+0j
pole1 = -2+0j
pole2 = -1+0j
a1 = -2+3j
a2 = -2+(math.sqrt(2)/2)*1j

angle1 =angle(a1-zero1)+angle(a1-zero2) -angle(a1-pole1) -angle(a1-pole2)
print(np.degrees(angle1))

angle2 =angle(a2-zero1)+angle(a2-zero2) -angle(a2-pole1) -angle(a2-pole2)
print(np.degrees(angle2))

mP = abs(a2-pole1)*abs(a2-pole2)
mZ = abs(a2-zero1)*abs(a2-zero2)
K = mP/mZ 
print('K is...', K)

* exercise 8.2
p = -3
pole1 = -2 +3j
pole2 = -2 -3*1j
zero =  -2
ang = angle(p-zero)-angle(p-pole1)-angle(p-pole2)
print('angles is...', np.degrees(ang))

K = abs(p-pole1)*abs(p-pole2)/abs(p-zero) 
print('K is...', K)


