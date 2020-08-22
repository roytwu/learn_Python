"""
Author:      Roy Wu
Description: Basic programming for numpy
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy        import linalg
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
print("eigenvalues are...", lamb)
print("eigenvectors are...", v[0])

I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
dumm1 = np.dot(lamb[0], I)
print("dumm1...", dumm1)
output = np.matmul((tata-dumm1), v[:,0])
print('output is...', output)


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