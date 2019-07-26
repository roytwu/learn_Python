"""
File name:   plot.py
Developer:   roy
Description: read and plot (IMU velocity) date from text file
"""
import math
import numpy             as np
import matplotlib        as mpl
import matplotlib.pyplot as plt

print('\nProgram starts... \n')

#* --- variable initialization ---
time, X, Y, Z = [], [], [], []  #* empty lists
initTime = 0
found = False

#* --- iterate each line of the text file ---
for line in open('velocityOutput_2.txt', 'r'):
    values = [float(string) for string in line.split()]
     
    #* find out initial timestamp
    if found == False:
        initTime = values[0]
        found = True 
   
    #* convert from mini-sec to sec
    timeInSec = (values[0] - initTime)*0.001
    
    time.append(timeInSec)      #* timestamp
    X.append(values[1])         #* x-axis
    Y.append(values[2])         #* y-axis
    Z.append(values[3])         #* z-axis
    
#* --- plot figure ---
plt.figure(figsize=(10, 4))                         #* setup figure size
plt.plot(time, X, '-b', label='velocity X-axis')   #* plot!!!
plt.legend(loc='upper right')                      #* setup label position
plt.xlabel('sec', fontsize=12)
plt.ylabel('m/s', fontsize=12)
plt.savefig('velocityIMU_2.png', dpi=220, bbox_inches='tight') 
#mpl.pyplot.show()
    
