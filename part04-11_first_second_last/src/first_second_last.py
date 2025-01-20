# Please write three functions: first_word, second_word and last_word. 
# Each function takes a string argument.

# As their names imply, the functions return either the first, the second 
# or the last word in the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two 
# separate words, and all words are separated by exactly one space character. 
# There will be no spaces in the beginning or at the end of the argument strings.

# sentence = "it was a dark and stormy python"

# print(first_word(sentence)) # it
# print(second_word(sentence)) # was
# print(last_word(sentence)) # python
# Sample output
# it
# was
# python

# Write your solution here
def first_word(a: str) -> str:
    b = a.split()
    return b[0]
def second_word(a: str) -> str:
    b = a.split()
    return b[1]
def last_word(a: str) -> str:
    b = a.split()
    return b[len(b)-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))