# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))
# Sample output
# False
# True

# Write your solution here
# Write your solution here
# ************************
# ****** Review Raw ******
# ************************
def row_correct(sudoku: list, row_no: int)-> bool:
    good_row = True
    counter_number=0
    for sk_number in range(1,10):
        if sudoku[row_no].count(sk_number)>1:
            good_row = False
    return good_row

# ************************
# *** Review Column ******
# ************************
def column_correct(sudoku: list, column_no: int)->bool:
    col_corr=True
    col_list=[]
    for row in sudoku:
        col_list.append(row[column_no])
    for sk_number in range(1,10):
        if col_list.count(sk_number)>1:
            col_corr = False
    return col_corr

# ************************
# **** Review Block ******
# ************************
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    rigth_block=True
    block_list=[]
    top_row=row_no+2
    top_col=column_no+2
    count_row=row_no
    while count_row <= top_row:
        count_col=column_no
        while count_col <= top_col:
            block_list.append(sudoku[count_row][count_col])
            count_col += 1
        count_row += 1
    for sk_number in range(1,10):
        if block_list.count(sk_number)>1:
            rigth_block = False
    return rigth_block

# ************************
# ***** Review Grid ******
# ************************
def sudoku_grid_correct(sudoku: list)->bool:
    right_grid = False
    right_raw= True
    right_col= True
    right_block= True
    grid_size=len(sudoku)
    # Review Raw
    for row_no in range(0,grid_size):
        right_raw=row_correct(sudoku, row_no)
        if right_raw==False:
            break
    # Review column
    for column_no in range(0,grid_size):
        right_col=column_correct(sudoku, column_no)
        if right_col==False:
            break
    # Review block
    block_list=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for block_no in block_list:
        right_block=block_correct(sudoku, int(block_no[0]), int(block_no[1]))
        if right_block==False:
            break
    # Review gid
    if right_raw == True and right_col == True and right_block == True:
        right_grid=True
    return right_grid

#*****************
#*** Execution ***
#*****************
if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
