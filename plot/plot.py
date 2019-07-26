"""
File name:   plot.py
Developer:   wur
Description: 
"""
import math
import numpy             as np
import matplotlib        as mpl
#import matplotlib.pyplot as plt

time, X, Y, Z = [], [], [], []

print('\nProgram starts... \n')

for line in open('velocityOutput_0.txt', 'r'):
    values = [float(s) for s in line.split()]
    time.append(values[0])
    X.append(values[1])
    Y.append(values[2])
    Z.append(values[3])
    
    
    mpl.pyplot.plot(time, X)
    mpl.pyplot.show()