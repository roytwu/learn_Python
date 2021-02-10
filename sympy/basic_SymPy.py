"""
Author:      Roy Wu
Description: Basic sympy operation 
History:     xx/xx/2019 -- initial version
             02/09/2021 -- revisit
"""

import sympy as sym
# from sympy import * #* import every object from SymPy
from sympy import expand, factor
from sympy.printing import pprint
from sympy.matrices import Matrix #* creating matrices in SymPy
from sympy          import simplify as simp
from sympy.integrals.transforms import inverse_laplace_transform as invLT
#sym.init_printing()


#*---------- ----------
#*    basic operation
#*---------- ----------
# a=sym.sqrt(3)
# print(a)
#* in SymPy, variables are defined using symbols
x, y = sym.symbols('x, y')
ans1 = x + 2*y
print(ans1, "\n")

#* integrate
print(sym.integrate(1/x, x))

#* expanded form and factored form
ans2 = expand(x*ans1)
# print(ans2)
# print(factor(ans2))

ans3 = sym.diff(sym.sin(x)*sym.exp(x), x)
ans4 = sym.Integral(sym.sqrt(1/x), x)

# pretty-print
# sym.printing.pprint(ans2, ans3)


#*---------- ----------
#*    Spring-mass example
#*---------- ----------
s, k, m = sym.symbols('s, k, m')
# C  = Matrix([[1, 0]])
# sI = Matrix([[s, 0], [0, s]])
# A  = Matrix([[0, 1], [-k/m, 0]])
# cp = Matrix([[s, -1], [k/m, s]]).inv()
# B  = Matrix([[0], [1/m]])
# #T  = C*cp*B
# T  = C*(sI-A).inv()*B
# pprint(sym.simplify(T))


#*---------- ----------
#*    state transition matrix
#*---------- ----------
t = sym.symbols('t',  positive=True)
# A =  Matrix([[0, 1, 0], [0, 0, 1], [-24, -26, -9]])
# sI = Matrix([[s, 0, 0], [0, s, 0], [0, 0, s]])
# resolvent = (sI-A).inv()
# pprint(simp(resolvent))

# sol = invLT(resolvent, s, t) 
# pprint(simp(sol))

reToto = sI = Matrix([[s, -1], [1, s]]).inv()
sol = invLT(reToto, s, t) 
pprint(simp(sol))



