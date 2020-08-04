"""
Author:      Roy Wu
Description: Basic programming for numpy
"""
import numpy as np
from scipy.linalg import expm, sinm, cosm
from pprint import pprint 

# a = np.arange(15).reshape(3,5) #* 3 rows x 5 columns
a = np.arange(9).reshape(3,3) #* 3 rows x 5 columns
m1 = np.exp(a) 
ma = expm(a)

print('Matrix a is...\n', a)
print('\nElement-wise exponential is ...\n', m1)
print('\nMatrix exponential is... ')
pprint(ma)


#*---------- ----------
#*     Euler's identity  
#*---------- ----------
eu1 = expm(1j*a)
eu2 = np.exp(1j*a)
eu3 = cosm(a) + 1j*sinm(a)
print(eu1-eu2)
print(eu1-eu3) #* this shall output zero matrix