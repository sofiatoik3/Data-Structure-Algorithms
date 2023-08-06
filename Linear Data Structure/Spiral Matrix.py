# -*- coding: utf-8 -*-
"""

@author: sofia
"""


def spiralOrder(self, matrix):
    
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
     """
    row = len(matrix)
    column = len (matrix[0])
        
    path = []
        
    while (len(path) != row*column):
        for i in range (len(matrix[0])):
            path.append(matrix[0][i])
        matrix.pop(0)
        for j in range (len(matrix)):
            matrix[j].reverse()
        matrix = list(map(list, zip(*matrix)))
    return path
