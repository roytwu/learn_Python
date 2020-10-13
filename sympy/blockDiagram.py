"""
Author:      Roy Wu
Description: block diagram, feedback loop
"""
import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy.printing import pprint
from sympy.matrices import Matrix
from sympy          import simplify as simp
from sympy.abc      import s

def feedback (fw, lp):
    feedback = fw/(1+lp)
    return feedback


#*---------- ----------
#*    example 1
#*---------- ----------
g2, g3, h1, h2, h3 = sym.symbols('g2, g3, h1, h2, h3')

tf1 = feedback(g2*g3, g2*g3*h1)
# pprint(tf1) 

tf2 = feedback(tf1, tf1*(-h2))
# pprint(simp(tf2)) 

tf3 = feedback(tf2, tf2*h3)
# pprint(simp(tf3)) 


#*---------- ----------
#*    problem 13 (7th) 
#*---------- ----------
b1 = 1/s+4
b2 = feedback(5*s, 5*s)
b3= b1*b2

dumm1 = (3*s/5)+1
b4= feedback(b3, b3*dumm1)
# b5= feedback(b4, b4)
pprint(simp(b4))

#*---------- ----------
#*    problem 8 (8th)
#*---------- ----------
# b1 = 1/s+3
# b2 = feedback(2*s, 2*s)
# b3= b1*b2

# dumm1 = 4*s/2
# b4= feedback(b3, b3*dumm1)
# b5= feedback(b4, b4)
# pprint(simp(b5))

#*---------- ----------
#*    exercise 5.1
#*---------- ----------
b1 = s*s+(1/s)
b2 = 1/s
b3= b1*b2

dumm1 = 2*s
b4= feedback(b3, b3*dumm1)
pprint(simp(b4))


#*---------- ----------
#*    unity v.s. nonUnity
#*---------- ----------
G, Ge, H = sym.symbols('G, Ge, H')

Ge = G/(1+G*H-G)
T = feedback(Ge, Ge)
pprint(simp(T))


#*---------- ----------
#*    Example7.8
#*---------- ----------
R1 = 1/s
G1 = 100/(s*(s+10))
H1 = 1/(s+5)
T1 = feedback(G1, G1*H1)
E1= R1*(1-T1)
pprint(simp(E1))

Ge1 = G1/(1+G1*H1-G1)
E2 = R1/(1+Ge1)

pprint(simp(E1-E2)) 







