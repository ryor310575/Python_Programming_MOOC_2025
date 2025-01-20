# Please write a function named transpose(matrix: list), which takes a two-dimensional 
# integer array, i.e., a matrix, as its argument. The function should transpose the matrix. 
# Transposing means essentially flipping the matrix over its diagonal: columns become rows, 
# and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# The following matrix

# 1 2 3
# 4 5 6
# 7 8 9
# transposed looks like this:

# 1 4 7
# 2 5 8
# 3 6 9
# The function should not have a return value. The matrix should be modified directly 
# through the reference.
# Write your solution here
def transpose(matrix: list):
    # Esta forma de construir la matriz crea dependencia
    # new_matrix=[[99] * len(matrix)] * len(matrix[0])
    # En este ejeccicio no es necesario crear una copia de la matriz original?
    rows=len(matrix)
    cols=len(matrix[0])
    raw_value=0
    col_value=0
    count_row=0
    count_col=0
    while count_row<rows:
        count_col=count_row
        while count_col<cols:
            raw_value=matrix[count_row][count_col]
            col_value=matrix[count_col][count_row]
            matrix[count_col][count_row]=raw_value
            matrix[count_row][count_col]=col_value
            count_col+=1
        count_row+=1

if __name__ == "__main__":
    my_matrix=[[0,1,2],
               [10,11,12],
               [20,21,22]]
    print(my_matrix)
    transpose(my_matrix)
    print(my_matrix)