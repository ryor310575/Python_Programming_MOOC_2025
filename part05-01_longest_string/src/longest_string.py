# Please write a function named longest(strings: list), which takes a list of strings 
# as its argument. The function finds and returns the longest string in the list. 
# You may assume there is always a single longest string in the list.

# An example of expected behaviour:
# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))
# Sample output
# howdydoody

# Write your solution here
def longest(my_list:list)->str:
    lenght_list=[]
    for word in my_list:
        lenght_list.append(len(word))
    # max_length=max(lenght_list)
    # longest_word_positon=lenght_list.index(max(lenght_list))
    longest_word=my_list[lenght_list.index(max(lenght_list))]
    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
