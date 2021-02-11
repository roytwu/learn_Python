"""
Author:      Roy Wu
Description: Homogeneous transformation
History:     xx/xx/2020 - intial version
             02/11/2021 - revisit
"""
import numpy as np
import sympy as sym
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy          import symbols
from sympy          import Matrix
# from sympy.abc      import a, b, c, d
from math           import cos, sin
from numpy.linalg   import multi_dot
import copy

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


def hXformSym (a, al, d, th):
    Rotz  = Matrix([ [sym.cos(th), -sym.sin(th), 0, 0], [sym.sin(th), sym.cos(th), 0, 0], 
                       [0, 0, 1, 0], [0, 0, 0, 1]])   
    Tranz = Matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
    Tranx = Matrix([ [1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    Rotx  = Matrix([ [1, 0, 0, 0], [0, sym.cos(al), -sym.sin(al), 0], 
                       [0, sym.sin(al), sym.cos(al), 0], [0, 0, 0, 1]])
    out = Rotz*Tranz*Tranx*Rotx
    return out

def hXFormSYM (input):
    a  = input[0]
    al = input[1]
    d  = input[2]
    th = input[3]
    Rotz  = Matrix([ [sym.cos(th), -sym.sin(th), 0, 0], [sym.sin(th), sym.cos(th), 0, 0], 
                       [0, 0, 1, 0], [0, 0, 0, 1]])   
    Tranz = Matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, d], [0, 0, 0, 1]])
    Tranx = Matrix([ [1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    Rotx  = Matrix([ [1, 0, 0, 0], [0, sym.cos(al), -sym.sin(al), 0], 
                       [0, sym.sin(al), sym.cos(al), 0], [0, 0, 0, 1]])
    out = Rotz*Tranz*Tranx*Rotx
    return out


def hatSym(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    output = Matrix([ [0, -x3, x2], [x3, 0, -x1], [-x2, x1, 0]])
    return output

def veeSym(matrix):
    x1 = matrix[2, 1]
    x2 = matrix[0, 2]
    x3 = matrix[1, 0]
    output = Matrix([ [x1], [x2], [x3]])
    return output



    


