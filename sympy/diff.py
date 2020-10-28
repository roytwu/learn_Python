import sympy as sym
from sympy           import Heaviside 
from sympy           import diff 
from sympy           import solve 
from sympy           import sin, cos, tan, cot
from sympy.printing  import pprint
from sympy           import simplify as simp
# from IPython.display import display  #* neat display for iPython
from sympy           import pi, exp
from sympy.matrices  import Matrix
from sympy.abc       import x, t, s, m



#*---------- ----------
#*    K
#*---------- ----------
ntr = s**2+3*s+2
dtr = s**2+7*s+12

# ntr = s**2+3*s+2
# dtr = s**2-8*s+15
K = -ntr/dtr

output = diff(K, s)
pprint(simp(output))


sol = solve(output, s)
print('\nbreakaway & breakin point...')
pprint(sol)



