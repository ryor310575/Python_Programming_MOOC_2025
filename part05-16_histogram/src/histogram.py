# We would like to analyze this list of words in different ways. For instance, 
# we would like to know how many times each word appears in the list.
# def counts(my_list):
#     words = {}
#     for word in my_list:
#         # if the word is not yet in the dictionary, initialize the value to zero
#         if word not in words:
#             words[word] = 0
#         # increment the value
#         words[word] += 1
#     return words

# # call the function
# word_list = [
#   "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
#   "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
#   "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
# ]
# print(counts(word_list))

# We would like to analyze this list of words in different ways. For instance, we would 
# like to know how many times each word appears in the list.
# word_list = [
#   "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
#   "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
#   "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
# ]
# def categorize_by_initial(my_list):
#     groups = {}
#     for word in my_list:
#         initial = word[0]
#         # initialize a new list when the letter is first encountered
#         if initial not in groups:
#             groups[initial] = []
#         # add the word to the appropriate list
#         groups[initial].append(word)
#     return groups

# groups = categorize_by_initial(word_list)

# for key, value in groups.items():
#     print(f"words beginning with {key}:")
#     for word in value:
#         print(word)

# ******** Histogram ********
# Please write a function named histogram, which takes a string as its argument. 
# The function should print out a histogram representing the number of times each 
# letter occurs in the string. Each occurrence of a letter should be represented 
# by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out

# Sample output
# a **
# b **
# while histogram("statistically") should print out

# Sample output
# s **
# t ***
# a **
# i **
# c *
# l **
# y *
# Write your solution here
def histogram(word:int):
    groups={}
    stars=""
    for character in word:
        if character not in groups:
            groups[character]=""
        groups[character]=str(groups[character]) + "*"
    for key, value in groups.items():
        print (f'{key} {value}')
if __name__ == "__main__":  
    histogram("statiiiiiiiiiiiisticccccally")
