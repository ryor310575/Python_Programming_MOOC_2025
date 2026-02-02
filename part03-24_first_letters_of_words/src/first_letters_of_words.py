# Please write a program which asks the user to type in a sentence.
# The program then prints out the first letter of each word in the sentence,
# each letter on a separate line.
#
# An example of expected behaviour:
#
# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

# Write your solution here
phrase=input("Please type in a sentence: ")
while True:
    if phrase.find(" ")<0:
        print(phrase[0])
        break
    else:
        print(phrase[0])
        phrase = phrase[phrase.find(" ") + 1:]