from sympy.integrals.transforms import laplace_transform as LT
from sympy.integrals.transforms import inverse_laplace_transform as invLT
import sympy as sym
from sympy           import Heaviside 
from sympy           import sin, cos, tan, cot
from sympy.printing  import pprint
from sympy           import simplify as simp
from IPython.display import display  #* neat display for iPython
from sympy           import pi, exp
from sympy.matrices  import Matrix

from sympy.abc import x, y, t, s, m
dmp = sym.symbols('dmp')

#*---------- ----------
#*    Basic
#*---------- ----------
om = sym.symbols('omega')
toto = sin(om)**2
tata = cos(om)**2
out = simp(toto + tata)
# print(out, '\n\n') #* regular print
# pprint(out)        #* pretty print
# print('\n\n')
# display(out)       #* latex print


#* Laplace transform of step function
u  = Heaviside(t)    #* step function
foo = cos(om*t)*u    #* (7) in Laplace transform table
fooLT = LT(foo, t, s)
pprint(fooLT[0])
#display(fooLT[0])


#*---------- ----------
#*    1st order ODE
#*---------- ----------
y = sym.Function('y')     #* y
dydt   = y(t).diff(t)     #* y_dot
left  = dydt -5*y(t)      #* ODE-left 
right = -exp(-2*t)        #* ODE-right 
expr = sym.Eq(left, right)  #* ODE expression
#display(expr)

#sol = sym.dsolve(expr, ics={y(0): 3})  #* solve ODE with "dsolve()"
#display(sym.apart(sol))

#*---------- ----------
#*    2nd order ODE
#*---------- ----------
y = sym.Function('y')     #* y
dydt = y(t).diff(t)     #* y_dot
ddy  = dydt.diff(t)     #* y_ddot

print('\ndydt is...')
pprint(dydt)
print('\n\n d2ydt2 is...')
pprint(ddy)

left  = ddy + 12*dydt + 32*y(t)  #* ODE(Example 2.3)
right = 32*u 
expr = sym.Eq(left, right)  #* ODE expression
pprint(expr)

sol = sym.dsolve(expr, ics={y(0): 0, y(t).diff(t).subs(t, 0): 0})  #* solution of ODE
print('\nSolutio of the ODE is...\n\n')
pprint(sym.expand(sol))

Y = 1/s - 2/(s+4) +1/(s+8)
sol2 = invLT(Y, s, t)  #* solution from inverse laplace transform
print('\n====== =====')
print('\nSolutio from invLT is...\n\n')
pprint(sym.expand(sol2))

print('\nComparing the results...\n\n')
compare = sol2 - sol.rhs
pprint(simp(compare))


#*---------- ----------
#*    polynomial
#*---------- ----------
# dum1 = (s+5)*(s+70)*10
# dum2 = s*(s+45)*(s+55)*(s**2+7*s+110)*(s**2+6*s+95)
# expr = dum1/dum2

# expr = (3*s+5)/(s**2-3*s-10)
# tDomain = invLT(expr, s, t)

expr = 1/(s*(2*s**2+4*s))
tDomain = invLT(expr, s, t)

#print(expr, '\n')
#display(expr)
#display(sym.expand(expr))
print('===== =====')
display(sym.expand(tDomain))


#*---------- ----------
#*    state space to transfer function
#*---------- ----------
# #* Spring-mass example
# s, k, m = sym.symbols('s, k, m')
# C  = Matrix([[1, 0]])
# sI = Matrix([[s, 0], [0, s]])
# A  = Matrix([[0, 1], [-k/m, 0]])
# B  = Matrix([[0], [1/m]])
# T  = C*(sI-A).inv()*B
# pprint(sym.simplify(T))