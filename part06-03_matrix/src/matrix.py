# Matrix
# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix 
# in the file, and then return the sum of the elements or the element with the greatest value, 
# as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row 
# in the matrix. For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4
# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program. It is very worthwhile to spend 
# a moment considering which functionalities are shared by the three functions you are asked to write. 
# Notice that the three functions named above do not take any arguments, but any helper functions you 
# write may take arguments. The file you are working with is always named matrix.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there are no spelling errors, 
# take a look at the instructions before this exercise.

#======================================
# write your solution here
# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades = parts[1:]
#         print("Name:", name)
#         print("Grades:", grades)
#         for items in parts:
#             print(items)
def str_to_num_list(line:list)->list:
    line_list=[]
    for numbers in line:
        line_list.append(int(numbers))
    return line_list
def row_max(file:str)->list:
    row_max=[]
    with open(file) as new_file:
        for line in new_file:
            parts_str = line.split(",")
            parts_num=str_to_num_list(parts_str)
            row_max.append(max(parts_num))
    return row_max
def row_sums()->list:
    row_sum=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts_str = line.split(",")
            parts_num=str_to_num_list(parts_str)
            row_sum.append(sum(parts_num))
    return row_sum
def matrix_sum()->int:
    mtx_sum=sum(row_sums())
    return mtx_sum
def matrix_max()->int:
    file="matrix.txt"
    mtx_max=max(row_max(file))
    return mtx_max


if __name__ == "__main__":
    # file_name="matrix.txt"
    # print(row_sums(file_name))
    # print(matrix_sum(file_name))
    # print(matrix_max(file_name))
    # row_sums("matrix.txt")
    # matrix_sum("matrix.txt")
    # matrix_max("matrix.txt")

    row_sums()
    matrix_sum()
    matrix_max()
