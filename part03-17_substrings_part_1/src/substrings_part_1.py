# Please write a program which asks the user to type in a string.
# The program then prints out all the substrings which begin with
# the first character, from the shortest to the longest.
# Have a look at the example below.
#
# Sample output
# Please type in a string: test
# t
# te
# tes
# test

# Write your solution here
word=input("Please type in a string: ")
counter=1
word_length=len(word)
# print(f"The length is {word_length}")
while counter<=word_length:
    partial_word=word[:counter]
    print(partial_word)
    # print(f"{counter}: {partial_word}")
    counter+=1