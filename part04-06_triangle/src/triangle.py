# Please write a function named triangle, which draws a triangle of hashes, 
# and takes one argument. The triangle should be as tall and as wide as 
# the value of the argument.

# The function should call the function line from the exercise above for 
# the actual printing out. Copy your solution to that exercise above the 
# code for this exercise. Please don't change anything in the line function.

# Some examples:
# triangle(6)
# print()
# #
# ##
# ###
# ####
# #####
# ######

# Sample output
# triangle(3)
# #
# ##
# ###

# Copy here code of line function from previous exercise
def line(times,char):
    i = 0
    if char == "":
        char = "*"
    line = ""
    while i < times or len(line) < times:
        line = line + char[0]
        i += 1
    print(line)

def triangle(size):
    # You should call function line here with proper parameters
    i=1
    while i <= size:
        line(i,"#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
