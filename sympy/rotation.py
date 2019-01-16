# -*- coding: utf-8 -*-
"""
File name:   rottion.py
Date:        Created on Wed Jan 16 16:36:31 2019
Author:      wur
Description: symbolic computations for rattion matrices
"""

import sympy as sym
from sympy.printing import pprint
from sympy.matrices import *

I = Matrix([[1,0,0],[0,1,0], [0,0,1]])

pprint(2*I)
pprint(eye(3))