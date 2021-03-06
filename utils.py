# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt as sq
def fact(n):
	if n < 0 :
		raise ValueError ('Must Be positive')
	if n ==0:
		return 1 
	else :
		return (n*fact(n-1))
		



def roots(a, b, c):
	delta = (b**2) - (4 * a * c)
	if delta < 0:
		return ()
	elif delta == 0 :
		return (-b/(2*a))
	else :
		x = (-b + sq(delta)) / (2 * a)
		y = (-b - sq(delta)) / (2 * a)
		return (y,x)
		



def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
