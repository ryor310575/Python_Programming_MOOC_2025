# Please write a program which asks the user to choose between addition and removal. 
# Depending on the choice, the program adds an item to or removes an item from the 
# end of a list. The item that is added must always be one greater than the last item 
# in the list. The first item to be added must be 1.

# The list is printed out in the beginning and after each operation. Have a look at 
# the example execution below:

# Sample output
# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!

# You may assume that, if the list is empty, there will not be an attempt to remove items.

# NB: this exercise doesn't ask you to write any functions, so you should not place any 
# code within an if __name__ == "__main__" block.

# If the specified item is not in the list, the remove function causes an error. 
# Just like with strings, we can check for the presence of an item with the in operator:

# my_list = [1, 3, 4]

# if 1 in my_list:
#     print("The list contains item 1")

# if 2 in my_list:
#     print("The list contains item 2")
# Sample output
# The list contains item 1


# Write your solution here
my_list = []
print("The list is now []")
i = 0
while True:
    item_action = input(f'a(d)d, (r)emove or e(x)it:')
    if item_action == "x":
        break
    elif item_action == "r":
        i -= 1
        my_list.pop(len(my_list) - 1)
        print(f'The list is now {my_list}')
    elif item_action == "d":
        i += 1
        my_list.append(i)
        print(f'The list is now {my_list}')
print("Bye!")