# Please write a function named sum_of_positives, which takes a list of 
# integers as its argument. The function returns the sum of the positive 
# values in the list.

# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)
# Sample output
# The result is 9

# Write your solution here
def sum_of_positives(my_list:list):
    suma=0
    for numero in my_list:
        if numero>=0:
            suma=suma+numero
    return suma
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 6]
    result = sum_of_positives(my_list)
    print("The result is", result)