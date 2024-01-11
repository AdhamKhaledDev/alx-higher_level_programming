#!/usr/bin/python3
"""
A function that calculates the squared value of every integer in a matrix.
"""
def square_matrix_simple(matrix=[]):
	new_matrix = []
	for neo in matrix:
		result = list(map(lambda e: e**2, neo))
		new_matrix.append(result)
	return new_matrix
