# Please write a function named length which takes a list as its argument and returns 
# the length of the list.

# my_list = [1, 2, 3, 4, 5]
# result = length(my_list)
# print("The length is", result)

# # the list given as an argument doesn't need to be stored in any variable
# result = length([1, 1, 1, 1])
# print("The length is", result)
# Sample output
# The length is 5
# The length is 4
# Write your solution here
# You can test your function by calling it within the following block

def length(items: list)->int:
    return len(items)
def mean(my_list: list) -> str:
    list_length = length(my_list)
    list_sum=sum(my_list)
    list_mean=list_sum/list_length
    return f'mean value is {list_mean}'
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)