"""
Author:      Roy Wu
Description: rogid body velocity
History:     03/14/2021 - intial version
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
from sympy.abc      import a, b, c, t
from sympy          import lambdify

from homoTrans import hXform #* use custom module
from homoTrans import hXformSym #* use custom module
from homoTrans import hatSym #* use custom module
from homoTrans import veeSym #* use custom module


th = sym.Function('theta')     #* y
# dydt   = y(t).diff(t)     #* y_dot

l0, l1, l2 = symbols('l0, l1, l2')

Rz= Matrix([ [cos(th(t)), -sin(th(t)), 0], [sin(th(t)), cos(th(t)), 0], [0, 0, 1]])    #* SO(3)
O_d =  Matrix([ [-l2*sin(th(t))], [l1+l2*cos(th(t))], [l0]])  #* d w.r.t. {O}
# dummy = Matrix([[0, 0, 0 , 1]])
# T = Rz.row_join(O_d) #* matrix concatenation
# T = T.col_join(dummy)  
# pprint(T)



#* find the 1st order time derivative
dotRz=  Rz.diff(t)
O_dotd = O_d.diff(t)
# pprint(simp(dotRz))
# pprint(simp(O_dotd))


O_v = -dotRz*(Rz.T)*O_d+O_dotd
O_omg = veeSym(dotRz*(Rz.T))
pprint(simp(O_v))
pprint(simp(O_omg))




