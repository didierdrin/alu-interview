#!/usr/bin/python3
"""
This is the modele of pascal triangle
"""
def pascal_triangle(n):
    """
	Returns a list of integer lists representing the pascArr triangle n
    """
    if n <= 0:
        return [] 
    pascArr = [[1]]  
    for i in range(1, n): 
        row = [1]
        for j in range(1, i):
            row.append(pascArr[i - 1][j - 1] + pascArr[i - 1][j])
        row.append(1) 
        pascArr.append(row) 
    return pascArr 
