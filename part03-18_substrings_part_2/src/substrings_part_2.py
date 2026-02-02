# Please write a program which asks the user to type in a string.
# The program then prints out all the substrings which end with the last character,
# from the shortest to the longest. Have a look at the example below.
#
# Sample output
# Please type in a string: test
# t
# st
# est
# test
# ------ Wrong Approach -------------------
# this approach consider all the possibilities. Although
# the example describe something more simple.
# word=input("Please type in a string: ")
# counter0=0
# word_length=len(word)
# sub_str=[]
# order_sub_str=[]
# while counter0<=word_length-1:
#     counter1 = counter0 + 1
#     while counter1<=word_length:
#         partial_word=word[counter0:counter1]
#         # print(f"{counter0}/{counter1}: {partial_word}")
#         if partial_word[-1]==word[-1] and partial_word not in sub_str:
#             sub_str.append(partial_word)
#         counter1+=1
#     counter0+=1
# order_sub_str=sorted(sub_str,key=len)
# print(len(order_sub_str))
# print(order_sub_str)
# for cadena in order_sub_str:
#     print(cadena)

# Write your solution here
word=input("Please type in a string: ")
word_length=len(word)
counter=word_length-1
# print(f"The length is {word_length}")
while counter>=0:
    partial_word=word[counter:]
    print(partial_word)
    # print(f"{counter}: {partial_word}")
    counter-=1