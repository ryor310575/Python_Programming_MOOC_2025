# Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, 
# or all lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p

# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B

# Write your solution here
char_1=input("1st letter: ")
char_2=input("2nd letter: ")
char_3=input("3rd letter: ")
if char_3 > char_2 and char_2 > char_1 or char_1>char_2 and char_2>char_3:
    print(f"The letter in the middle is {char_2}")
elif char_2 > char_1 and char_1 > char_3 or char_3>char_1 and char_1>char_2:
    print(f"The letter in the middle is {char_1}")
elif char_1 > char_3 and char_3 > char_2 or char_2>char_3 and char_3>char_1:
    print(f"The letter in the middle is {char_3}")