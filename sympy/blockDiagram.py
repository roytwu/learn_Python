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


def feedback (fw, lp):
    feedback = fw/(1+lp)
    return feedback


g2, g3, h1, h2, h3 = sym.symbols('g2, g3, h1, h2, h3')

tf1 = feedback(g2*g3, g2*g3*h1)
pprint(tf1) 

tf2 = feedback(tf1, tf1*(-h2))
pprint(simp(tf2)) 

tf3 = feedback(tf2, tf2*h3)
pprint(simp(tf3)) 