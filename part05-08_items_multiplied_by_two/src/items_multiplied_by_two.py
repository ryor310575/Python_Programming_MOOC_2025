# Please write a function named double_items(numbers: list), which takes a list of 
# integers as its argument.

# The function should return a new list, which contains all values from the original 
# list doubled. The function should not change the original list.

# An example of the function at work:

# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)
#     print("doubled:", numbers_doubled)
# Sample output
# original: [2, 4, 5, 3, 11, -4]
# doubled: [4, 8, 10, 6, 22, -8]
# Write your solution here
def double_items(numbers: list) -> list:
    double_list=[]
    for number in numbers:
        double_list.append(number * 2)
    return double_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)