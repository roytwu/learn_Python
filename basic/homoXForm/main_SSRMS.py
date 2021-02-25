"""
Author:      Roy Wu
Description: Symbolic computations for homogeneous transformation
History:     02/25/2021 - intial version
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

#*---------- ----------
#*    SSRMS (forward K)
#*---------- ----------
#* th1=th6=pi/2, th2=th3=th4=-pi/2, th5=-pi, th7=0
la=10
lb=12
lc=14
ld=50
le=50
lf=16
lg=18
lh=20

#* zero position
th1 = 0
th2 = th3 = th4 = th5 = th6 = th7 =0 
#* X: ld, le -lc 
#* Y: lb, lf
#* Z: la-lc-lf-lh    

# #* cofiguration 1
# th1 = np.pi/2
# th2 = -np.pi/2
# th3 = -np.pi/2
# th4 = -np.pi/2
# th5 = -np.pi
# th6 = np.pi/2
# th7 = 0


jt1 = hXform(0, -np.pi/2, la, th1)  #* la
jt2 = hXform(0, -np.pi/2, lb, th3)  #* lb
jt3 = hXform(ld, 0, lc, th2)        #* lc, ld
jt4 = hXform(le, 0, 0, th4)         #* le
jt5 = hXform(0, np.pi/2, lf, th5)   #* lf
jt6 = hXform(0, -np.pi/2, lg, th6)  #* lg
jt7 = hXform(0, 0, lh, th7)         #* lh
T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6, jt7]).round(3)
pprint(T)


# lA, lB, lC, lD = symbols('l_a, l_b, l_c, l_d')
# lE, lF, lG, lH = symbols('l_e, l_f, l_g, l_h')

# jt1 = hXformSym(0, -np.pi/2, lA, th1)  #* la
# jt2 = hXformSym(0, -np.pi/2, lB, th3)  #* lb
# jt3 = hXformSym(lD, 0, lC, th2)        #* lc, ld
# jt4 = hXformSym(lE, 0, 0, th4)         #* le
# jt5 = hXformSym(0, np.pi/2, lF, th5)   #* lf
# jt6 = hXformSym(0, -np.pi/2, lG, th6)  #* lg
# jt7 = hXformSym(0, 0, lH, th7)         #* lh
# T = jt1*jt2*jt3*jt4*jt5*jt6*jt7
# #T = T.evalf(2)
# pprint(nsimp(T, tolerance=1e-10, rational=True))



# jt1 = hXform(0, -np.pi/2, 1.0, np.pi/2)
# jt2 = hXform(0, -np.pi/2, 1.2, np.pi/2)
# jt3 = hXform(5, 0, 1.4, np.pi/2)
# jt4 = hXform(5, 0, 1.6, -np.pi/4)
# jt5 = hXform(0, np.pi/2, 1.8, -np.pi/4)
# jt6 = hXform(0, -np.pi/2, 2.0, -np.pi/4)
# T = multi_dot([jt1, jt2, jt3, jt4, jt5, jt6]).round(3)
# pprint(T)