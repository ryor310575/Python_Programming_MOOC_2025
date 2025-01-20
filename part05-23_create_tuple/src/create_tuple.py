# ****** Create a tuple ******
# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments
# An example of its use:
# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))
# Sample output
# (-1, 5, 7)
# Write your solution here
def sum_list(my_list:list)->list:
    summatory=0
    for number in my_list:
        summatory=summatory+number
    return summatory

def create_tuple(x: int, y: int, z: int) -> tuple:
    new_tuple=()
    temp_list=[]
    temp_list.append(x)
    temp_list.append(y)
    temp_list.append(z)
    temp_list.sort()
    new_tuple=(min(temp_list),max(temp_list),sum_list(temp_list))
    return new_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))