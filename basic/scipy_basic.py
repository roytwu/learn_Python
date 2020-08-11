"""
Author:      Roy Wu
Description: Basics about SciPy
"""
import numpy             as np
import matplotlib.pyplot as plt
from scipy.linalg import expm, sinm, cosm
from scipy.fft    import fft, ifft
from pprint       import pprint 

# a = np.arange(15).reshape(3,5) #* 3 rows x 5 columns
a = np.arange(9).reshape(3,3) #* 3 rows x 5 columns
m1 = np.exp(a) 
ma = expm(a)

#*---------- ----------
#*     Euler's identity  
#*---------- ----------
eu1 = expm(1j*a)
eu2 = np.exp(1j*a)
eu3 = cosm(a) + 1j*sinm(a)
print(eu1-eu2)
print(eu1-eu3) #* this shall output zero matrix


N = 50  #* number of sample points
T = 1   #* sample spacing 
x = np.linspace(0.0, N*T, N)
y = np.exp(-x)
yf = fft(y) 
xf = np.linspace(0.0, 1/(2.0*T), N//2)
plt.plot(xf, 2.0/N*np.abs(yf[0:N//2]))
plt.grid()
plt.show()

xf2 = np.linspace(0.0, 2, N)
yf2 =1/(xf2+1)
plt.plot(xf2,yf2) 
plt.grid()
plt.show()




