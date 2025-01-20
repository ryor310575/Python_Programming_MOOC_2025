# Please write a function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears 
# first in the string should be returned.

# An example of expected behaviour:

# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))
# Sample output
# b
# e

# Write your solution here
def most_common_character(my_string:str)->int:
    list_occurrencies=[]
    max_occurrencies=0
    for characters in my_string:
        list_occurrencies.append(my_string.count(characters))
    max_occurrencies=max(list_occurrencies)
    return my_string[list_occurrencies.index(max_occurrencies)]
#if __name__ == "__main__":
if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))