# Please write a function named mean, which takes a list of integers as an argument. 
# The function returns the arithmetic mean of the values in the list.

# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)
# Sample output
# mean value is 3.0

# Write your solution here
def length(items: list)->int:
    return len(items)
def mean(my_list: list) -> float:
    list_length = length(my_list)
    list_sum=sum(my_list)
    list_mean=list_sum/list_length
    return list_mean
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)