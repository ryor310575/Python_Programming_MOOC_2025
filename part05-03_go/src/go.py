# In a game of Go two players take turns to place black and white stones on a game board. 
# The winner is the player who manages to encircle a bigger area on the board with their 
# own game pieces.

# Please write a function named who_won(game_board: list), which takes a two-dimensional 
# array as its argument. The array consists of integer values, which represent the following 
# situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare 
# the number of pieces each player has on the game board. Also, the size of the game board 
# is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. 
# If both players have the same number of pieces on the board, the function should return 
# the value 0.

# Write your solution here
def who_won(game_board: list)->int:
    winner=0
    g1_counter=0
    g2_counter=0
    g1=1
    g2=2
    for row in game_board:
        for col in row:
            if col == g1:
                g1_counter += 1
            elif  col == g2:
                g2_counter += 1
    if g1_counter == g2_counter:
        winner=0
    elif g1_counter > g2_counter:
        winner=1
    else:
        winner=2
    return winner

if __name__ == "__main__":
    go = [
            [2, 1, 0, 0, 2, 0, 2, 0, 0],
            [0, 0, 0, 1, 1, 0, 2, 0, 0],
            [0, 2, 0, 1, 0, 0, 2, 0, 2],
            [0, 2, 2, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 2, 2, 0],
            [1, 0, 1, 0, 2, 0, 2, 0, 2],
            [0, 0, 1, 1, 0, 2, 2, 0, 2],
            [0, 2, 1, 2, 0, 0, 2, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 2]]
    print(who_won(go))
