"""
Created on: Tue Jan 15 14:51:35 2019
File name:  basic_SymPy.py
Author:     wur
"""

import sympy as sym
#from sympy import symbols 

a=sym.sqrt(3)
print(a)

#* in SymPym, variables are defined using symbols
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