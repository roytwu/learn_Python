import numpy as np
import sympy as sym
from numpy.linalg   import multi_dot
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import sin, cos
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform #* use custom module


a1, alpha1, d1, th1 = symbols('a_1, alpha_1, d_1, theta_1')
a2, alpha2, d2, th2 = symbols('a_2, alpha_2, d_2, theta_2')
a3, alpha3, d3, th3 = symbols('a_3, alpha_3, d_3, theta_3')

#* sanity check
# a1=a2=a3=1
# th1=th2=th3=0

a1=a2=a3=5.0
th1=np.pi/2.0
th2=th3=0

#*---------- ----------
#*    RRR manipulator
#*---------- ----------
jt1 = hXform(a1, 0, 0, th1)
jt2 = hXform(a2, 0, 0, th2)
jt3 = hXform(a3, 0, 0, th3)
T = multi_dot([jt1, jt2, jt3]).round(3)
# pprint(T)


#*---------- ----------
#*    SSRMS
#*---------- ----------
jt1 = hXform(0, -np.pi/2, 1.0, np.pi/2)  #*la
jt2 = hXform(0, -np.pi/2, 1.2, -np.pi/2) #*lb
jt3 = hXform(5, 0, 1.4, -np.pi/2) #*lc
jt4 = hXform(5, 0, 0, 0) #* d=0
jt5 = hXform(0, np.pi/2, 1.6, -np.pi) #* lf
jt6 = hXform(0, -np.pi/2, 1.8, np.pi/2) #* lg
jt7 = hXform(0, 0, 2.0, 0) #* lg
T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6, jt7]).round(3)
pprint(T)


# jt1 = hXform(0, -np.pi/2, 1.0, np.pi/2)
# jt2 = hXform(0, -np.pi/2, 1.2, np.pi/2)
# jt3 = hXform(5, 0, 1.4, np.pi/2)
# jt4 = hXform(5, 0, 1.6, -np.pi/4)
# jt5 = hXform(0, np.pi/2, 1.8, -np.pi/4)
# jt6 = hXform(0, -np.pi/2, 2.0, -np.pi/4)
# T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6]).round(3)
# pprint(T)






