"""
Author:      Roy Wu
Description: 3D vector plotting
"""
import math
import numpy             as np
import matplotlib.pyplot as plt
from numpy                import linalg
from mpl_toolkits.mplot3d import Axes3D 


fig = plt.figure()
ax = plt.axes(projection='3d')

#*---------- ----------
#*    3D vector plot  
#*---------- ----------
m1 = np.array([[math.cos(0.3), 0, math.sin(0.3)], [0, 1, 0], [-math.sin(0.3), 0, math.cos(0.3)]])
m2 = np.array([[math.cos(0.3), -math.sin(0.3), 0], [math.sin(0.3), math.cos(0.3), 0], [0, 0, 1]])
x1 = np.array([0, 1.5, 0])
x2 = np.array([3, 0, 0])

y1= m1.dot(x1)
y2= m2.dot(x2)
print('y1 is....', y1)
print('y2 is....', y2)

# q1 = ax.quiver(0, 0, 0, x1[0], x1[1], x1[2])
# q2 = ax.quiver(0, 0, 0, x2[0], x2[1], x2[2])
# q3 = ax.quiver(0, 0, 0, y2[0], y2[1], y2[2])


#*---------- ----------
#*    3D vector plot  
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