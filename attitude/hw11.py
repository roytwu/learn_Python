import numpy as np


angle = 20      #*in degrees 
atr = np.pi/180 # angle to radian
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
print ("Result is ...\n", r2_O)