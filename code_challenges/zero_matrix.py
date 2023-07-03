"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""
def zeroMatrix(input_matrix, rows, cols):
    columns_with_zeros = []
    rows_with_zeroes = []    
    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j]==0:
                columns_with_zeros.append(j)
                rows_with_zeroes.append(i)
    for i in range(rows):
        for j in range(cols):
            if i in rows_with_zeroes or j in columns_with_zeros:
                input_matrix[i][j] = 0
    
            
            
    
