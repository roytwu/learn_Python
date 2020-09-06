from sympy.integrals.transforms import laplace_transform as LT
from sympy.integrals,transforms import inverse_laplace_transform as invLT
import sympy as sym
from sympy import Heaviside


#* in SymPy, variables are defined using symbols
x, y, t, s = sym.symbols('x, y, t, s')
a, b, c = sym.symbols('a, b, c')
#u = sym.symbols('u', cls = Function)

u = Heaviside(t) #* step function
print(u)

output = LT(u, t, s)
print(output)