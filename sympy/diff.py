import sympy as sym
from sympy           import Heaviside 
from sympy           import diff 
from sympy           import solve 
from sympy           import sin, cos, atan, acot
from sympy.printing  import pprint
from sympy           import simplify as simp
# from IPython.display import display  #* neat display for iPython
from sympy           import pi, exp
from sympy.matrices  import Matrix
from sympy.abc       import x, y, t, s, m, k





#*---------- ----------
#*    K (root locus)
#*---------- ----------
# ntr = s**2+3*s+2
# dtr = s**2+7*s+12

# # ntr = s**2+3*s+2
# # dtr = s**2-8*s+15
# K = -ntr/dtr

# output = diff(K, s)
# pprint(simp(output))


# sol = solve(output, s)
# print('\nbreakaway & breakin point...')
# pprint(sol)



# #*---------- ----------
# #*   Imaginary axis crossing
# #*---------- ----------
# expr = (1+k)*0-(25+8*k)*(6-6*k)
# sol = solve(expr, k)
# pprint(sol)


#*---------- ----------
#*    ODE
#*---------- ----------
eq1   = atan(x)-x/5
output = diff(eq1, x)
pprint(simp(output))


sol = solve(output, x)
print('\nsol is...')
pprint(sol)

eq2 = y**2*cos(x)-x**3*sym.ln(y)
dumm = diff(eq2, x)
out = diff(dumm, y)
pprint(simp(out))


eq3 = sin(x)**2
out = sym.integrate(eq3, x)
pprint(simp(out))


#* demo 
expr1 = x**2 +3*x +2
#expr1 = 2*(x**2)*cos(x)**2 +sin(x)**2
out = expr1.diff(x) #* call as method
pprint(out)

out2 = solve(expr1, x)
print(out2)

expr2 = cos(x)**2*sin(y)
out3 = diff(expr2, x, y)
print(out3)


