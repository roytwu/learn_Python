"""
Author:      Roy Wu
Description: fibonacci numbers 
             function 1 is the memorized version, give the result fast
             function 2 is the straight version, it takes time to calculate
"""

known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]

	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res 
	return res	

def fibonacci2(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci2(n-1) + fibonacci2(n-2)		

