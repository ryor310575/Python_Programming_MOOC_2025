# ******** Invert a dictionary ********
# Please write a function named invert(dictionary: dict), which takes a dictionary 
# as its argument. The dictionary should be inverted in place so that values become 
# keys and keys become values.

# An example of its use:

# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)
# Sample output
# {"first": 1, "second": 2, "third": 3, "fourth": 4}

# NB: the principles regarding lists covered here also hold for dictionaries passed 
# as arguments.
# If you have trouble completing this exercise, the visualisation tool might help 
# you understand what your code is or isn't doing.

# Write your solution here
# Write your solution here
def invert(dictionary: dict):
    new_dictionary={}
    for key, value in dictionary.items():
        new_dictionary[value]=key
    dictionary.clear()
    for key, value in new_dictionary.items():
        dictionary[key]=value
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)