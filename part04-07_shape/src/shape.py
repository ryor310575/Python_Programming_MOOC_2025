# Please write a function named shape, which takes four arguments. 
# The first two parameters specify a triangle, as above, and the 
# character used to draw it. The first parameter also specifies the 
# width of a rectangle, while the third parameter specifies its height. 
# The fourth parameter specifies the filler character of the rectangle. 
# The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for 
# the actual printing out. Copy your solution to that exercise above the 
# code for this exercise. Please don't change anything in the line function.

# Some examples:

# Sample output
# shape(5, "X", 3, "*")
# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****

# Sample output
# shape(2, "o", 4, "+")
# o
# oo
# ++
# ++
# ++
# ++

# Sample output
# shape(3, ".", 0, ",")
# .
# ..
# ...




# Copy here code of line function from previous exercise and use it in your solution
def line(times,char):
    i = 0
    if char == "":
        char = "*"
    line = ""
    while i < times or len(line) < times:
        line = line + char[0]
        i += 1
    print(line)
# Square
def rectanle(w_size,h_size, character):
    # You should call function line here with proper parameters
    i = 1
    while i <= h_size:
        line(w_size, character)
        i += 1

# Triangle
def triangle(size,character):
    i=1
    while i <= size:
        line(i,character)
        i+=1
# Shape
def shape(t_size, t_symbol, s_size, s_symbol):
    triangle(t_size,t_symbol)
    rectanle(t_size,s_size, s_symbol)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")