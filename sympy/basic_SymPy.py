"""
Created on: Tue Jan 15 14:51:35 2019
File name:  basic_SymPy.py
Author:     wur
"""

import sympy as sym
#sym.init_printing()

a=sym.sqrt(3)
print(a)

#* in SymPy, variables are defined using symbols
x, y = sym.symbols('x, y')
ans1 = x + 2*y
print(ans1, "\n")

#* integrate
print(sym.integrate(1/x, x))

#* expanded form and factored form
from sympy import expand, factor
ans2 = expand(x*ans1)
print(ans2)
print(factor(ans2))

ans3 = sym.diff(sym.sin(x)*sym.exp(x), x)
ans4 = sym.Integral(sym.sqrt(1/x), x)

# pretty-print
sym.printing.pprint(ans2, ans3)


#* import every object from SymPy
from sympy import *
printing.pprint(ans4)


#* creating matrices in SymPy
from sympy.printing import pprint
from sympy.matrices import Matrix
I = Matrix([[1,0,0],[0,1,0], [0,0,1]])
pprint(2*I)
pprint(eye(3))


#* Equals sign
from sympy import sin, cos, tan, cot
a = sin(x)
b = cos(x)
out = a**2+b**2
print(sym.simplify(out-1))





