# ******** Largest number ********
# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...
# Please write a function named largest, which reads the file and returns the 
# largest number in the file.

# Notice that the function does not take any arguments. The file you are working 
# with is always named numbers.txt.

# NB: If Visual Studio Code can't find the file and you have checked that there 
# are no spelling errors, take a look at the instructions following this exercise.
# ===========================
# with open("/Users/ryanortega/example.txt","r") as new_file:
#     count = 0
#     total_length = 0
#     for line in new_file:
#         line = line.replace("\n", "")
#         count += 1
#         print("Line", count, line)
#         length = len(line)
#         total_length += length
# print("Total length of lines:", total_length)

# write your solution here
# with open(""/Users/ryanortega/Library/Application Support/tmc/vscode/mooc-programming-24/part06-01_largest_number/src/numbers.txt","r") as new_file:
def largest():
    with open("numbers.txt","r") as new_file:
        numbers=[]
        # print(new_file.read())
        # print("===========================")
        for line in new_file:
            line = line.replace("\n", "")
            number =  int(line)
            numbers.append(number)
    return max(numbers)
if __name__ == "__main__":
    largest()







