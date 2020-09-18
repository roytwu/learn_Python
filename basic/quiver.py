"""
Author:      Roy Wu
Description: 3D vector plotting
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy                import linalg
from mpl_toolkits.mplot3d import Axes3D 
import quiver

fig = plt.figure()
ax = plt.axes(projection='3d')

#*---------- ----------
#*    3D vector plot  
#*---------- ----------
a = 0.5
m1 = np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])
m2 = np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])
x1 = np.array([0, 1.5, 0])
x2 = np.array([3, 0, 0])

y1= m1.dot(x1)
y2= m2.dot(x2)
print('y1 is....', y1)
print('y2 is....', y2)

# q1 = ax.quiver(0, 0, 0, x1[0], x1[1], x1[2]) #* draw vector x1
# q2 = ax.quiver(0, 0, 0, x2[0], x2[1], x2[2]) #* draw vector x2
# q3 = ax.quiver(0, 0, 0, y2[0], y2[1], y2[2])


#*---------- ----------
#*    3D vector plot  (rotaiton over 2pi)
#*---------- ----------
rg  = np.linspace(-np.pi, np.pi, 20) 

for th in rg:
  mtx = np.array([[math.cos(th), -math.sin(th), 0], [math.sin(th), math.cos(th), 0], [0., 0, 1]])
  y= mtx.dot(x2)
  ax.quiver(0, 0, 0, y[0], y[1], y[2])


ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 3])


plt.show()

<<<<<<< HEAD

# #* Spring-mass example
# s, k, m = sym.symbols('s, k, m')
# C  = Matrix([[1, 0]])
# sI = Matrix([[s, 0], [0, s]])
# A  = Matrix([[0, 1], [-k/m, 0]])
# B  = Matrix([[0], [1/m]])
# T  = C*(sI-A).inv()*B
# pprint(sym.simplify(T))
=======
print(quiver)
>>>>>>> 8a70f5118b11b49797d9071499015324db0c8e10
