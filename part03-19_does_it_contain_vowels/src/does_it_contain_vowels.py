# Please write a program which asks the user to input a string.
# The program then prints out different messages if the string
# contains any of the vowels a, e or o.
#
# You may assume the input will be in lowercase entirely.
# Have a look at the examples below.
#
# Sample output
# Please type in a string: hello there
# a not found
# e found
# o found
#
# Sample output
# Please type in a string: hiya
# a found
# e not found
# o not found
#---------- Solutions one ----------------
# Write your solution here
phrase= input("Please type in a string: ")
phrase_lower=phrase.lower()
a_case=""
e_case=""
o_case=""
if "a" in phrase_lower:
    a_case="a found"
else:
    a_case = "a not found"
if "e" in phrase_lower:
    e_case="e found"
else:
    e_case = "e not found"
if "o" in phrase_lower:
    o_case="o found"
else:
    o_case = "o not found"
print(a_case)
print(e_case)
print(o_case)