#******************************************
#********* Previous Informations **********
#******************************************

#*********  Este programa abre el archivo multiples veces ********* 

# with open("people.csv") as new_file:
#     # print out the names
#     for line in new_file:
#         parts = line.split(";")
#         print("Name:", parts[0])

#     # find the oldest
# with open("people.csv") as new_file:
#     age_of_oldest = -1
#     for line in new_file:
#         parts = line.split(";")
#         name = parts[0]
#         age = int(parts[1])
#         if age > age_of_oldest:
#             age_of_oldest = age
#             oldest = name
#     print("the oldest is", oldest)
# #********* Este programa abre el archivo slo una vez *********
# people = []
# # read the contents of the file and store it in a list
# with open("people.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         people.append((parts[0], int(parts[1]), parts[2]))
#         print(type(people[0]))

# # print out the names
# for person in people:
#     print("Name:", person[0])

# # find the oldest
# age_of_oldest = -1
# for person in people:
#     name = person[0]
#     age = person[1]
#     if age > age_of_oldest:
#         age_of_oldest = age
#         oldest = name
# print("the oldest is", oldest)

#******************************************
#********* Creando un Diccionario *********
# This following program creates a dictionary grades based on the contents of the file. 
# The keys are the names of the students, and the value attached to each key is the list 
# of grades attained by the student. The program converts the grades to integer values, 
# so they can be processed easier.
# grades = {}
# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades[name] = []
#         for grade in parts[1:]:
#             grades[name].append(int(grade))
# print(grades)
# # Now we can print out some statistics on each student based on the contents of the dictionary grades:
# for name, grade_list in grades.items():
#     best = max(grade_list)
#     average = sum(grade_list) / len(grade_list)
#     print(f"{name}: best grade {best}, average {average:.2f}")
#******************************************************************************
#********* strip() Removing unnecessary lines, spaces and line breaks *********
#******************************************************************************
# last_names = []
# with open("people2.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         # ignore the header line
#         if parts[0] == "first":
#             continue
#         last_names.append(parts[1])
# print(last_names)
# a more efficient solution is to use the Python string method strip, which removes whitespace from 
# the beginning and end of a string. It removes all spaces, line breaks, tabs and other characters 
# which would not normally be printed out.
# last_names = []
# with open("people2.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "first":
#             continue # this was the header line, so it is ignored
#         last_names.append(parts[1].strip())
# print(last_names)

#*******************************************************
#********* Combining data from different files *********
#*******************************************************
# # Create the Name dictionary
# names = {}
# with open("employees.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic": # Obvia la cabecera
#             continue
#         names[parts[0]] = parts[1:] # Crear el diccionario

# # Create the Salaries dictionary
# salaries = {}
# with open("salaries.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic":  # Obvia la cabecera
#             continue
#         salaries[parts[0]] = int(parts[1]) +int(parts[2])  # Crear el diccionario
# # Create the Incomes
# print("incomes:")
# for pic, name in names.items():
#     if pic in salaries:
#         salary = salaries[pic]
#         print(f"{name[0]:20} {salary} euros")
#     else:
#         print(f"{name[0]:20} 0 euros")


#*******************************************************
#********* Combining data from different files *********
#*******************************************************
# names = {}

# with open("employees.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic":
#             continue
#         names[parts[0]] = parts[1]

# salaries = {}

# with open("salaries.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic":
#             continue
#         salaries[parts[0]] = int(parts[1]) +int(parts[2])

# print("incomes:")

# for pic, name in names.items():
#     if pic in salaries:
#         salary = salaries[pic]
#         print(f"{name:16} {salary} euros")
#     else:
#         print(f"{name:16} 0 euros")
#*******************************************************
#*************   Course grading, part 1   **************
#*******************************************************
# This program works with two CSV files. One of them contains information about some 
# students on a course:

# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder
# The other contains the number of exercises each student has completed each week:

# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
# As you can see above, both CSV files also have a header row, which tells you what each 
# column contains.

# Please write a program which asks the user for the names of these two files, reads the files, 
# and then prints out the total number of exercises completed by each student. If the files have 
# the contents in the examples above, the program should print out the following:

# Sample output:
# Student information: students1.csv
# Exercises completed: exercises1.csv
# pekka peloton 21
# jaana javanainen 27
# liisa virtanen 35

# Hint: while testing your program, you may quickly run out of patience if you always have to type 
# in the file names at the prompt. You might want to hard-code the user input, like so:

# if False:
#     # this is never executed
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # hard-coded input
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
# The actual functionality of the program is now "hidden" in the False branch of an if statement. 
# It will never be executed.

# Now, if you want to quickly verify the program works correctly also with user input, you can just 
# replace False with True:


# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"
# When you have verified your program works correctly, you can remove the if structure, keeping the 
# commands asking for input.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an 
# if __name__ == "__main__" block.

# NB2: If Visual Studio can't find the file and you have checked that there are no spelling errors, take 
# a look at these instructions.

# -----------------------------------------------------------------
# write your solution here
# -----------------------------------------------------------------

# Crear el diccionario de estudiantes
students_file=input("Student information: ")
student_info= {}
with open(students_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id": # Obvia la cabecera
            continue
        student_info[parts[0]] = parts[1:] # Crear el diccionario de estudiantes

# Create the Exercises completed dictionary
exercice_file=input("Exercises completed: ")
student_exercises = {}
with open(exercice_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":  # Obvia la cabecera
            continue
        exercises=[]
        for exercise in parts[1:]:
            exercises.append(int(exercise))
        student_exercises[parts[0]] = exercises  # Crear el diccionario
# Create the report
for pic, name in student_info.items():
    if pic in student_exercises:
        exercises_completed = sum(student_exercises[pic])
        print(f"{name[0]} {name[1].strip()} {exercises_completed}")
    else:
        continue
