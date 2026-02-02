# Please write a program which asks the user for a string and then prints
# out a frame of * characters with the word in the centre.
# The width of the frame should be 30 characters.
# You may assume the input string will always fit inside the frame.
#
# If the length of the input string is an odd number, you may print out
# the word in either of the two possible centre locations.
#
# Sample output
# Word: testing
#
# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python
#
# ******************************
# *           python           *
# ******************************
# Write your solution here
word=input("Word: ")
word_length=len(word)
print("*"*30)
if word_length%2==0:
    space_right=" " * ((30-2-word_length)//2)
    space_left=" " * ((30-2-word_length)//2)
    print("*"+space_right+word+space_left+"*")
else:
    space_right=" " * ((30-2-(word_length-1))//2)
    space_left=" " * (((30-2-(word_length-1))//2)-1)
    print("*"+space_right+word+space_left+"*")
print("*"*30)