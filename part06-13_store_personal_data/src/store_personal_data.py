# Please write a function named store_personal_data(person: tuple), which takes a tuple containing 
# some identifying information as its argument.

# The tuple contains the following elements:

# Name (string)
# Age (integer)
# Height (float)
# This should be processed and written into the file people.csv. The file may already contain some 
# data; the new entry goes to the end of the file. The data should be written in the format

# name;age;height

# Each entry should be on a separate line. If we call the function with the argument 
# ("Paul Paulson", 37, 175.5), the function should write this line to the end of the file:

# Paul Paulson;37;175.5
# Write your solution here
#******************** FUNCTION *************************
#*********       escribir en un archivo         ********
#*******************************************************
# Please write a function named store_personal_data(person: tuple), 
# which takes a tuple containing some identifying information as its argument.
# The tuple contains the following elements: Name (string), Age (integer), Height (float)
# This should be processed and written into the file people.csv. The file may 
# already contain some data; the new entry goes to the end of the file. 
# The data should be written in the format: name;age;height
def store_personal_data(person: tuple):
    string_to_safe=f'{person[0]};{person[1]};{person[2]}'
    current_file="people.csv"
    with open(current_file, "a") as my_file:
        my_file.write(f'{string_to_safe}\n')
if __name__ == "__main__":
    peson_data=("Paul Paulson", 37, 175.5)
    store_personal_data(peson_data)

