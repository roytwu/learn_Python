import numpy as np
import sympy as sym
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import symbols
# from sympy          import sin, cos
# from sympy.abc      import a, b, c, d
from math           import cos, sin
from numpy.linalg   import multi_dot

al, be, ga   = symbols("alpha beta gamma")
th, phi, psi = symbols("theta phi psi")

# def hXform2 (a, al, d, th):
#     Rotz  = Matrix([ [cos(th), -sin(th), 0, 0], [sin(th), cos(th), 0, 0], 
#                    [0, 0, 1, 0], [0, 0, 0, 1]])
#     Tranz = Matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
#     Tranx = Matrix([ [1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
#     Rotx  = Matrix([ [1, 0, 0, 0], [0, cos(al), -sin(al), 0], 
#                    [0, sin(al), cos(al), 0], [0, 0, 0, 1]])
#     out = Rotz*Tranz*Tranx*Rotx
#     return out


def hXform (a, al, d, th):
    Rotz  = np.array([ [cos(th), -sin(th), 0, 0], [sin(th), cos(th), 0, 0], 
                       [0, 0, 1, 0], [0, 0, 0, 1]])   
    Tranz = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
    Tranx = np.array([ [1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    Rotx  = np.array([ [1, 0, 0, 0], [0, cos(al), -sin(al), 0], 
                       [0, sin(al), cos(al), 0], [0, 0, 0, 1]])
    # dumm1 = np.matmul(Rotz, Tranz)
    # dumm2 = np.matmul(Tranx, Rotx)
    out = multi_dot([Rotz, Tranz, Tranx, Rotx])
    return out