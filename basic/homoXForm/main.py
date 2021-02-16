"""
Author:      Roy Wu
Description: Symbolic computations for homogeneous transformation
History:     xx/xx/2020 - intial version
             02/11/2021 - revisit
"""
import numpy as np
import sympy as sym
from numpy.linalg   import multi_dot
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import nsimplify as nsimp
from sympy          import sin, cos
from sympy          import symbols
from sympy.abc      import a, b, c, d
from sympy          import lambdify

from homoTrans import hXform #* use custom module
from homoTrans import hXformSym #* use custom module
from homoTrans import hatSym #* use custom module
from homoTrans import veeSym #* use custom module


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
#*    SSRMS (forward K)
#*---------- ----------
#* th1=th6=pi/2, th2=th3=th4=-pi/2, th5=-pi, th7=0
la=10
lb=12
lc=14
ld=50
le=50
lf=18
lg=16
lh=13

# #* cofiguration 1
# th1 = np.pi/2
# th2 = -np.pi/2
# th3 = -np.pi/2
# th4 = -np.pi/2
# th5 = -np.pi
# th6 = np.pi/2
# th7 = 0

#* zero position
th1 = 0
th2 = th3 = th4 = th5 = th6 = th7 =0 
#* X: ld, le -lc 
#* Y: lb, lf
#* Z: la-lc-lf-lh    

jt1 = hXform(0, -np.pi/2, la, th1)  #* la
jt2 = hXform(0, -np.pi/2, lb, th3)  #* lb
jt3 = hXform(ld, 0, lc, th2)        #* lc, ld
jt4 = hXform(le, 0, 0, th4)         #* le
jt5 = hXform(0, np.pi/2, lf, th5)   #* lf
jt6 = hXform(0, -np.pi/2, lg, th6)  #* lg
jt7 = hXform(0, 0, lh, th7)         #* lh
T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6, jt7]).round(3)
pprint(T)


lA, lB, lC, lD = symbols('l_a, l_b, l_c, l_d')
lE, lF, lG, lH = symbols('l_e, l_f, l_g, l_h')

jt1 = hXformSym(0, -np.pi/2, lA, th1)  #* la
jt2 = hXformSym(0, -np.pi/2, lB, th3)  #* lb
jt3 = hXformSym(lD, 0, lC, th2)        #* lc, ld
jt4 = hXformSym(lE, 0, 0, th4)         #* le
jt5 = hXformSym(0, np.pi/2, lF, th5)   #* lf
jt6 = hXformSym(0, -np.pi/2, lG, th6)  #* lg
jt7 = hXformSym(0, 0, lH, th7)         #* lh
T = jt1*jt2*jt3*jt4*jt5*jt6*jt7
#T = T.evalf(2)
pprint(nsimp(T, tolerance=1e-10, rational=True))






# jt1 = hXform(0, -np.pi/2, 1.0, np.pi/2)
# jt2 = hXform(0, -np.pi/2, 1.2, np.pi/2)
# jt3 = hXform(5, 0, 1.4, np.pi/2)
# jt4 = hXform(5, 0, 1.6, -np.pi/4)
# jt5 = hXform(0, np.pi/2, 1.8, -np.pi/4)
# jt6 = hXform(0, -np.pi/2, 2.0, -np.pi/4)
# T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6]).round(3)
# pprint(T)


# #*---------- ----------
# #*    HW#6
# #*---------- ----------
# x= Matrix([ [3], [5], [-7]])
# y= Matrix([ [-1], [2], [3]])
# out = hatSym(x)*y
# pprint(out)

