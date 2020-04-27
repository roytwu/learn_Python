import numpy as np
#from nummpy.matrices import Matrix

angle = 20
atr = np.pi/180;
Rz = np.matrix([ [np.cos(angle*atr), -np.sin(atr), 0], 
               [np.sin(angle*atr), np.cos(angle*atr), 0], 
               [0,0,1] ])

print(Rz) #* R_OB


angleFoo = np.arctan(3.5/2)/atr
print("angleFoo is ...", angleFoo)


length = np.sqrt(2*2+3.5*3.5)
r2b_length = length*np.cos((angleFoo-20)*atr)
print (r2b_length)


r2B = np.matrix([[r2b_length], [0], [0]])
print (r2B)


r2O = Rz*r2B
print ("Result is ...\n", r2O)