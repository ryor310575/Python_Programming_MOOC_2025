# Given a list of integers, let's decide that two consecutive items in the 
# list are neighbours if their difference is 1. So, items 1 and 2 would be 
# neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, which looks 
# for the longest series of neighbours within the list, and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours 
# would be [5, 4, 3, 4], with a length of 4.

# An example function call:

# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))
# Sample output
# 4


# Write your solution here
def compare_neighbours(prev:int,mid:int)->bool:
    if abs(prev-mid)==1:
        return True
    else:
        return False


def longest_series_of_neighbours(my_list:list)->int:
    neighbours_list = []
    neighbours = 0
    counter=0
    list_lenght=len(my_list)
    while counter <= list_lenght - 1:
        if (counter + 1)<=(list_lenght - 1):
            if compare_neighbours(my_list[counter],my_list[counter+1])==True:
                neighbours +=1
            else:
                neighbours_list.append(neighbours)
                neighbours=0
        else:
            neighbours_list.append(neighbours)
            neighbours=0
        counter+=1
    if max(neighbours_list)==0:
        return max(neighbours_list)
    else:
        return max(neighbours_list)+1


if __name__ == "__main__":
    #my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    my_list = [1, 2,4,3,4,5,4,8,9,8,7,4,5,6,7,8,7,6,5]
    print(longest_series_of_neighbours(my_list))
