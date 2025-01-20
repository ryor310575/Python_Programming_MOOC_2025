# Please write a function named times_ten(start_index: int, end_index: int), which creates and 
# returns a new dictionary. The keys of the dictionary should be the numbers between start_index 
# and end_index inclusive

# The value mapped to each key should be the key times ten.

# For example:

# d = times_ten(3, 6)
# print(d)
# Sample output
# {3: 30, 4: 40, 5: 50, 6: 60}

# Write your solution here
# Write your solution here
def times_ten(start_index: int, end_index: int)-> dict:
    dictionary={}
    counter=start_index
    while counter <= end_index:
        dictionary[counter]=counter * 10
        counter += 1
    return dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)