# Please write a function named spruce, which takes one argument. 
# The function prints out the text a spruce!, and the a spruce tree, 
# the size of which is specified by the argument.

# Calling spruce(3) should print out

# Sample output
# a spruce!
#   *
#  ***
# *****
#   *
# Calling spruce(5) should print out

# Sample output
# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *
# Write your solution here

# You can test your function by calling it within the following block
# This line function print a line with two kind of characters
def line(times1,char1,times2,char2):
    i = 0
    if char1 == "":
        char1 = "*"
    line1 = ""
    line2 = ""
    line = ""
    while i < times1 or len(line1) < times1:
        line1 = line1 + char1[0]
        i += 1
    i=0
    while i < times2 or len(line2) < times2:
        line2 = line2 + char2[0]
        i += 1
    line=line1+line2
    print(line)

# Base
def base(w_size,character):
    pad_base= w_size - 1
    base = " " * pad_base + "*"
    print(base)

# Triangle
def triangle(size,character):
    i=1
    while i <= size:
        max_base_triangle = 2 * i - 1
        max_pad=size-i
        line(max_pad," ",max_base_triangle,character)
        i+=1

# SPRUCE
def spruce(t_size):
    print("a spruce!")
    t_symbol="*"
    triangle(t_size,t_symbol)
    base(t_size,t_symbol)
# MAIN FUNCTION
if __name__ == "__main__":
    spruce(5)