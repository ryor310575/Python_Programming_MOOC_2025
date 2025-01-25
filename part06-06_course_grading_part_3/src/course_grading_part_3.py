# ********************************************************
# **************** Course grading, part 3 ****************
# ********************************************************
# This exercise will continue from the previous one. Now we shall print out some statistics based 
# on the CSV files.

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3

# Each row contains the information for a single student. The number of exercises completed, the number 
# of exercise points awarded, the number of exam points awarded, the total number of points awarded, 
# and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

# You might find the f-strings covered in part 4 useful here.

# F-strings differentiate between strings and numbers when it comes to justifying columns:

# word = "python"
# print(f"{word:10}continues")
# print(f"{word:>10}continues")
# Sample output
# python    continues
#     pythoncontinues
# As you can see above, by default strings are justified to the left edge of the area specified for them. The > symbol can be used to justify to the right edge.

# With number values the logic is reversed:

# number = 42
# print(f"{number:10}continues")
# print(f"{number:<10}continues")
# Sample output
#         42continues
# 42        continues
# With numbers the default behaviour is to justify to the right edge. The symbol < can be used to justify to the left edge.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

# tee ratkaisu tänne
#*******************************************************
#*********   Convertir puntos a grado o nivel  *********
# Este Programa convierte los valores de un puntaje
# desde el 0 al 100 en grados del 0 al 9
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
#*******************************************************
#*********  Convertir puntos a grado o nivel   *********
# Convierte las notas obtenidas en un exament en una 
# escala de 0 a 5
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

#*******************************************************
#*********  Convertir un archivo a diccionario  ********
# Esta funcion convierte un archivo en un diccionario 
# 1) Toma una palabra del header y obvia el encabezado
# 2) Asume que el archivo esta separado por ;
# 3) Evaluamos si los argimentos son numeros y los 
#    evaluamos como numeros si son cadenas los evaluamos 
#    como cadenasevaluamos como numeros si son cadenas 
#    los evaluamos como cadenas
# 4) Crear el diccionario de estudiantes la primera 
#    columba como Key y el resto como lista
#*******************************************************
def file_to_dictionary(fle_name:str,header:str)->dict:
    file_info = {} #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == header: # Obvia la cabecera
                continue
            arg_list=[]
            for arg in parts[1:]: # Evaluamos si los argimentos son numeros y los evaluamos como numeros si son cadenas los evaluamos como cadenas
                try:
                    arg_list.append(int(arg)) # 
                except:
                    arg_list.append(arg.strip())
            file_info[parts[0]] = arg_list # Crear el diccionario de estudiantes la primera columba como Key y el resto como lista
    return file_info

def main():
    #*** Solicitud de nombre de Files ***
    if True:
        #Create the students info dictionary
        students_file=input("Student information: ")
        student_dict= file_to_dictionary(students_file,"id")

        # Create the exam completed dictionary
        exercice_file=input("Exercises completed: ")
        exercice_dict = file_to_dictionary(exercice_file,"id")

        # Create the exam points dictionary
        exam_points_file=input("Exam points: ")
        exam_points_dict = file_to_dictionary(exam_points_file,"id")
    else:
        #*** Asignacion teemporal fija para correr pruebas ***
        student_file="students1.csv"
        exercice_file="exercises1.csv"
        exam_points_file="exam_points1.csv"
        student_dict=file_to_dictionary(student_file,"id")
        exercice_dict=file_to_dictionary(exercice_file,"id")
        exam_points_dict=file_to_dictionary(exam_points_file,"id")
    # Create the report
    print(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")

    for pic, name in student_dict.items():
        if pic in exercice_dict:
            total_name=name[0] + " " + name[1]
            exec_nbr=sum(exercice_dict[pic])
            exam_point=sum(exam_points_dict[pic]) # exm_pts
            exercises_completed = int(sum(exercice_dict[pic])/40 *10) # exec_pts
            total_points= exercises_completed+exam_point #tot_pts 
            grade_points=examPoints_to_grade(exercises_completed+exam_point) # grade
            print(f"{total_name:30}{exec_nbr:<10}{exercises_completed:<10}{exam_point:<10}{total_points:<10}{grade_points}")
        else:
            continue

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# name                                  exec_nbr  exec_pts. exm_pts.  tot_pts  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3

# name                          exec_nbr  sexec_pt. exm_pts.  tot_pts  grade
# pekka peloton                 21                5               9               14              0
# jaana javanainen              27                6               11              17              1
# liisa virtanen                35                8               14              22              3

main()
