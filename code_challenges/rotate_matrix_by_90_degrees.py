"""
    Given an n x n square matrix, write a program to rotate the matrix by 90 degrees in the clockwise direction. 
"""
import copy
class RotateMatrix90Degrees:    
    def bruteForceCockwise(self, input_matrix, n):
        """
        time complexity: O(n2)
        Space Complexity: O(n2)
        """
        temp_matrix = copy.deepcopy(input_matrix)
        for row_num in range(n):
            for col_num in range(n):
                temp_matrix[col_num][n-1-row_num] = input_matrix[row_num][col_num]
        return temp_matrix
    
    def layerwiseRoatation(self, input_matrix, n):   
        """
        time complexity: O(n2)
        Space Complexity: O(1)
        """     
        layers = n//2
        for i in range(layers):
            for j in range(i, n-1-i):
                temp = input_matrix[i][j]
                input_matrix[i][j] = input_matrix[n - 1 - j][i]
                input_matrix[n - 1 - j][i] = input_matrix[n - 1 - i][n - 1 - j]
                input_matrix[n - 1 - i][n - 1 - j] = input_matrix[j][n - 1 - i]
                input_matrix[j][n - 1 - i] = temp
        return input_matrix
    
    def layerwiseAnticlockwiseRoation(self, input_matrix, n):
        """
        time complexity: O(n2)
        Space Complexity: O(1)
        """ 
        layers = n//2
        for i in range(layers):
            for j in range(i, n-1-i):
                temp = input_matrix[i][j]
                input_matrix[i][j] = input_matrix[j][n-1-i]
                input_matrix[j][n-1-i] = input_matrix[n-1-i][n-1-j]
                input_matrix[n-1-i][n-1-j] =input_matrix[n-1-j][i]
                input_matrix[n-1-j][i] = temp