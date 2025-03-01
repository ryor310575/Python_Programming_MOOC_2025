# Please write a function named distinct_numbers, which takes a list of 
# integers as its argument. The function returns a new list containing 
# the numbers from the original list in order of magnitude, and so that 
# each distinct number is present only once.

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]

# Write your solution here
def distinct_numbers(my_list : list)->list:
    unique_list=[]
    my_list.sort()
    for number1 in my_list:
        if number1 not in unique_list:
            unique_list.append(number1)
    return unique_list


if __name__ == "__main__":
    my_list = [8,8,4,5,6,6,7,7,3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]