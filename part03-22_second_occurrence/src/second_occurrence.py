# Please write a program which finds the second occurrence of a substring.
# If there is no second (or first) occurrence, the program should print out a message accordingly.
#
# In this exercise the occurrences cannot overlap.
# For example, in the string aaaa the second occurrence of the substring aa is at index 2.
#
# Some examples of expected behaviour:
#
# Sample output
# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.
#
# Sample output
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.
#
# Sample output
# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.

# Write your solution here
word=input("Please type in a string: ")
sub_str=input("ase type in a substring: ")
counter=0
position=0
while True:
    if counter>1:
        print(f"The second occurrence of the substring is at index {position-len(sub_str)}.")
        break
    elif word.find(sub_str) < 0:
        print("The substring does not occur twice in the string.")
        break
    else:
        str_position=word.find(sub_str)
        position = position + str_position
        word=word[str_position:]
        word=word[len(sub_str):]
        position = position + len(sub_str)
        counter+=1
