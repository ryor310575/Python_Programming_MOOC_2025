# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

# An example of how the function should work:

# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']

# More slices
# In fact, the [] syntax works very similarly to the range function, which means we can also give it a step:

# my_string = "exemplary"
# print(my_string[0:7:2])
# my_list = [1,2,3,4,5,6,7,8]
# print(my_list[6:2:-1])
# Sample output
# eepa
# [7, 6, 5, 4]

# If we omit either of the indexes, the operator defaults to including everything. Among other things, this allows us to write a very short program to reverse a string:

# my_string = input("Please type in a string: ")
# print(my_string[::-1])
# Sample output
# Please type in a string: exemplary
# yralpmexe

# Write your solution here

def everything_reversed(my_list:list)->list:
    reversed_list=[]
    reversed_word=""
    for words in my_list:
        reversed_word=words[::-1]
        reversed_list.append(reversed_word)
    return reversed_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)