# The file solutions.csv contains some solutions to mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
# As you can see above, on each line the format is name_of_student;problem;result. All the operations 
# are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the 
# original file.

# NB: the function should have the exact same result, no matter how many times it is called. 
# That is, it shouldn't matter if the function is called once

# filter_solutions()
# or multiple times in a row

# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()
# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly 
# the same in either case.

# Write your solution here
#**********
#* Metodo 1
#**********
# with open("coders.csv", "w") as my_file:
#     my_file.write("Eric;Windows;Pascal;10\n")
#     my_file.write("Matt;Linux;PHP;2\n")
#     my_file.write("Alan;Linux;Java;17\n")
#     my_file.write("Emily;Mac;Cobol;9\n")

#**********
#* Metodo 2
#**********
# coders = []
# coders.append(["Eric", "Windows", "Pascal", 10])
# coders.append(["Matt", "Linux", "PHP", 2])
# coders.append(["Alan", "Linux", "Java", 17])
# coders.append(["Emily", "Mac", "Cobol", 9])

# with open("coders.csv", "w") as my_file:
#     for coder in coders:
#         line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
#         my_file.write(line+"\n")

#**********
#* Metodo 3
#**********
# with open("coders.csv", "w") as my_file:
#     for coder in coders:
#         line = ""
#         for value in coder:
#             line += f"{value};"
#         line = line[:-1]
#         my_file.write(line+"\n")
#*******************************************************
# Filtering the contents of a file
# Please write a function named filter_solutions() which
# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
#*******************************************************


#******************** FUNCTION *************************
#*********       escribir en un archivo         ********
#*******************************************************
def write_entry(current_file:str,entry:str)->bool:
    with open(current_file, "a") as my_file:
        my_file.write(f'{entry}\n')

#*********************FUNCTION**************************
#*********         test line           ********
# Toma una linea con el formato: Kirka;79-15;22 
# revisa que la operacion sea correcta y devuelve 
# Verdadero o Falso
#*******************************************************
def operation_test(line_to_test:str)->bool:
    test_flag=False
    line_to_test=line_to_test.strip()
    parts = line_to_test.split(';')
    result=int(parts[2])
    operation=parts[1]
    if '+' in operation:
        suma=operation.split("+")
        test=int(suma[0])+int(suma[1])
        if test == result:
            test_flag=True
    elif '-' in operation:
        resta=operation.split("-")
        test=int(resta[0])-int(resta[1])
        if test == result:
            test_flag=True
    return test_flag
def filter_solutions():
    #*** Clean de flter files ***
    open('incorrect.csv', 'w').close()
    open('correct.csv', 'w').close()
    with open("solutions.csv") as solutions_file:
        for line in solutions_file:
            line=line.strip()
            if operation_test(line.strip()):
                receive_flag=write_entry('correct.csv',line)
            else:
                receive_flag=write_entry('incorrect.csv',line)


if __name__ == "__main__":
    filter_solutions()
