#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = []
	for submat in matrix:
		result = list(map(lambda e: e**2, submat))
		new_matrix.append(result)
	return new_matrix
