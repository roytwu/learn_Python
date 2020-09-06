from sympy.integrals.transforms import laplace_transform as LT
from sympy.integrals.transforms import inverse_laplace_transform as invLT
import sympy as sym
from sympy          import Heaviside 
from sympy          import sin, cos, tan, cot
from sympy.printing import pprint
from sympy          import simplify as simp


#* in SymPy, variables are defined using symbols
t, s = sym.symbols('t, s')
a, b, c = sym.symbols('a, b, c')
om = sym.symbols('omega')

#*---------- ----------
#*    Step function  
#*---------- ----------
u = Heaviside(t) #* step function
pprint(u)

out1 = LT(u, t, s)
print(out1)

out2 = invLT(out1[0], s, t)
print(out2)

foo = cos(om*t)*u     #* (7) in Laplace transform table
fooLT = LT(foo, t, s)
#pprint(simp(fooLT))

#*---------- ----------
#*    Laplace transform of a ODE
#*---------- ----------
y = sym.Function('y')     #* y
dydt   = y(t).diff(t)     #* y_dot
d2ydt2 = dydt.diff(t)     #* y_ddot

print('\ndydt is...')
pprint(dydt)
print('\n\n d2ydt2 is...')
pprint(d2ydt2)

left  = d2ydt2 + 12*dydt + 32*y(t)  #* ODE(Example 2.3)
right = 32*u 
expr = sym.Eq(left, right)  #* ODE expression
# pprint(expr)

sol = sym.dsolve(expr, ics={y(0): 0, y(t).diff(t).subs(t, 0): 0})  #* solution of ODE
pprint(simp(sol))

Y = 1/s - 2/(s+4) +1/(s+8)
sol2 = invLT(Y, s, t)  #* solution from inverse laplace transform
print('\n ====== =====')
pprint(simp(sol2))





