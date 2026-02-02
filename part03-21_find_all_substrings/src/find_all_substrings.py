# Please make an extended version of the previous program,
# which prints out all the substrings which are at least three characters long,
# and which begin with the character specified by the user.
# You may assume the input string is at least three characters long.
#
# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot
#
# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan
#
# Hint the following example may give you some inspiration as to
# how this exercise could be tackled:
#
# word = input("Word: ")
# while True:
#     if len(word) == 0:
#         break
#     print(word)
#     word = word[2:]
# Sample output
# Word: mammoth
# mammoth
# mmoth
# oth
# h
# Write your solution here
word=input("Please type in a word: ")
character=input("Please type in a character: ")
word_lower=word.lower()
word_sliced=word_lower
while True:
    char_position = word_sliced.find(character)
    word_sliced=word_sliced[char_position:]
    if len(word_sliced)<3:
        break
    else:
        word_to_print=word_sliced[:3]
        word_sliced=word_sliced[1:]
        print(word_to_print)