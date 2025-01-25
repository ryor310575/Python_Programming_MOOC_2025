# Please write a program which works as a simply diary. The diary entries should be saved in the file 
# diary.txt. When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. If you want to keep 
# its contents, first make a copy of the file under a different name.

# The program should work as follows:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# When the program is executed for the second time, this should happen:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.


# Write your solution here
# with open("new_file.txt", "w") as my_file:
#     my_file.write("Hello there!\n")
#     my_file.write("This is the second line\n")
#     my_file.write("This is the last line\n")

# with open("new_file.txt", "a") as my_file:
#     my_file.write("This is the 4th line\n")
#     my_file.write("And yet another line.\n")

#     1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

#*******************************************************
#*********       escribir en un archivo         ********
#*******************************************************
def write_entry(current_file:str,entry:str)->bool:
    with open(current_file, "a") as my_file:
        my_file.write(f'{entry}\n')
#*******************************************************
#*********         leer en un archivo           ********
#*******************************************************
def read_entry(current_file:str)->str:
    file_info =""
    with open(current_file) as my_file:
        for line in my_file:
            file_info=file_info + line
    return file_info

def main():
    function=5
    while function != 0:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function=int(input("Function:"))
        if function == 0:
            print("Bye now!")
        elif function == 1:
            diary_entry=input("Diary entry:")
            if write_entry("diary.txt",diary_entry):
                print("Diary saved")
        elif function == 2:
            print(read_entry("diary.txt"))
# execute main
main()

