# *********************************************
# *********  Course grading, part 2  **********
# *********************************************
# Let's expand the program created in the previous exercise. Now also the exam points awarded to 
# each student are contained in a CSV file. The contents of the file follow this format:

# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2
# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the 
# exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process 
# the files and print out a grade for each student.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3

# Each completed exercise is counted towards exercise points, so that completing at least 10 % of 
# the total exercices awards 1 point, completing at least 20 % awards 2 points, etc. Completing 
# all 40 exercises awards 10 points. The number of points awarded is always an integer number.

# The final grade for the course is determined based on the sum of exam and exercise points according 
# to the following table:

# exam points + exercise points         grade
#       0-14	                        0 (fail)
#       15-17                           1
#       18-20	                        2
#       21-23	                        3
#       24-27	                        4
#       28-	                            5
# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an 
# if __name__ == "__main__" block.

# *********************************************
# wite your solution here
# *********************************************

# Convertir puntos a grado o nivel
#*******************************************************
def percentage_to_points(completed_exercises:int)->int:
    points=0
    if completed_exercises<10:
        points=0
    elif completed_exercises<20:
        points=1
    elif completed_exercises<30:
        points=2
    elif completed_exercises<40:
        points=3
    elif completed_exercises<50:
        points=4
    elif completed_exercises<60:
        points=5
    elif completed_exercises<70:
        points=6
    elif completed_exercises<80:
        points=7
    elif completed_exercises<90:
        points=8
    elif completed_exercises<100:
        points=9
    else:
        points=10
    return points
# Convertir puntos a grado o nivel
#*******************************************************
def examPoints_to_grade(points:int)->int:
    grade=0
    if points > 14 and points <=17:
        grade =1
    elif points > 17 and points <=20:
        grade =2
    elif points > 20 and points <=23:
        grade =3
    elif points > 23 and points <=27:
        grade =4
    elif points > 27:
        grade =5
    return grade

# Convertir un archivo a diccionario
#*******************************************************
def file_to_dictionary(fle_name:str,header:str)->dict:
    file_info = {} #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == header: # Obvia la cabecera
                continue
            arg_list=[]
            for arg in parts[1:]: # Evaluamos si los argimentos son numeros y losevaliamos como numeros si son cadenas los evaluamos como cadenas
                try:
                    arg_list.append(int(arg)) # 
                except:
                    arg_list.append(arg.strip())
            file_info[parts[0]] = arg_list # Crear el diccionario de estudiantes la primera columba como Key y el resto como lista
    return file_info

def main():
    #*** Solicitud de Files ***
    # Create the students info dictionary
    students_file=input("Student information: ")
    student_dict= file_to_dictionary(students_file,"id")

    # Create the exam completed dictionary
    exercice_file=input("Exercises completed: ")
    exercice_dict = file_to_dictionary(exercice_file,"id")

    # Create the exam points dictionary
    exam_points_file=input("Exam points: ")
    exam_points_dict = file_to_dictionary(exam_points_file,"id")

    # #*** Asignacio fija para correr pruebas ***
    # student_file="students1.csv"
    # exercice_file="exercises1.csv"
    # exam_points_file="exam_points1.csv"
    # student_dict=file_to_dictionary(student_file,"id")
    # exercice_dict=file_to_dictionary(exercice_file,"id")
    # exam_point_dict=file_to_dictionary(exam_points_file,"id")
    # Create the report
    for pic, name in student_dict.items():
        if pic in exercice_dict:
            exam_point=sum(exam_points_dict[pic])
            exercises_completed = int(sum(exercice_dict[pic])/40 *10)
            grade_points=examPoints_to_grade(exam_point+exercises_completed)
            print(f"{name[0]} {name[1]} {grade_points}")
        else:
            continue

main()

