# Let's revisit the course grading project from the previous section.

# As we left if last time, the program read and processed files containing student 
# information, completed exercises and exam results. We'll add a file containing 
# information about the course. An example of the format of the file:

# Sample data

# name: Introduction to Programming
# study credits: 5
# The program should then create two files. There should be a file called results.txt 
# with the following contents:

# Sample data
# Introduction to Programming, 5 credits
# ======================================
# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
# The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.

# Additionally, there should be a file called results.csv with the following format:

# Sample data
# 12345678;pekka peloton;0
# 12345687;jaana javanainen;1
# 12345699;liisa virtanen;3
# When the program is executed, it should look like this:

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# Course information: course1.txt
# Results written to files results.txt and results.csv

# That is, the program only asks for the names of the input files. All output should be 
# written to the files. The user will only see a message confirming this.

# NB: this exercise doesn't ask you to write any functions, so you should not place any 
# code within an if __name__ == "__main__" block.
#******************** FUNCTION *************************
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
#******************** FUNCTION *************************
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

#******************** FUNCTION *************************
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

#******************** FUNCTION *************************
#*********           Write DICT a FILE          ********
#*******************************************************
def save_dict_to_file(filename:str, dict_to_save:dict):
    with open(filename, "w") as my_file:
        for id, data in dict_to_save.items():
            my_file.write(f'{id};{data[0]};{data[1]}\n')

#******************** FUNCTION *************************
#*********           Write STR a FILE           ********
#*******************************************************
def save_str_to_file(filename:str, string_to_save:dict):
    with open(filename, "w") as my_file:
        my_file.write(string_to_save)

#******************** FUNCTION *************************
#*********         Print a file content         ********
#*******************************************************
def read_and_print_file(filename:str):
    with open(filename) as my_file:
        for line in my_file:
            line=line[:-1]
            print(line)

#******************** FUNCTION *************************
#*********       Read courseX.txt to STR        ********
#*******************************************************
def read_courseX_file(filename:str)->str:
    course_info=""
    course_list=[]
    with open(filename) as my_file:
        for line in my_file:
            parts=line.split(':')
            course_list.append(parts[1].strip())
    course_info=f'{course_list[0]}, {course_list[1]} credits'
    return course_info



def main():
    #*** Clean de resoults files ***
    open('results.csv', 'w').close()
    open('results.txt', 'w').close()
    results_csv={}
    results_txt=""
    #*** Request the data files ***
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

        # Create course information string
        course_file=input("Course information: ")
        course_str = read_courseX_file(course_file)
    else:
        #*** Asignacion teemporal fija para correr pruebas ***
        student_file="students1.csv"
        exercice_file="exercises1.csv"
        exam_points_file="exam_points1.csv"
        course_file="course1.txt"
        student_dict=file_to_dictionary(student_file,"id")
        exercice_dict=file_to_dictionary(exercice_file,"id")
        exam_points_dict=file_to_dictionary(exam_points_file,"id")
        course_str = read_courseX_file(course_file)
    # Create the report
    results_txt=course_str + '\n'
    results_txt=results_txt+"======================================" + '\n'
    results_txt= results_txt+"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade" + '\n'

    

    for pic, name in student_dict.items():
        if pic in exercice_dict:
            total_name=name[0] + " " + name[1]
            exec_nbr=sum(exercice_dict[pic])
            exam_point=sum(exam_points_dict[pic]) # exm_pts
            exercises_completed = int(sum(exercice_dict[pic])/40 *10) # exec_pts
            total_points= exercises_completed+exam_point #tot_pts 
            grade_points=examPoints_to_grade(exercises_completed+exam_point) # grade
            # Built the string to safe to file results.txt
            results_txt=results_txt+f'{total_name:30}{exec_nbr:<10}{exercises_completed:<10}{exam_point:<10}{total_points:<10}{grade_points}'+'\n'
            #print(f"{total_name:30}{exec_nbr:<10}{exercises_completed:<10}{exam_point:<10}{total_points:<10}{grade_points}")
            # Built the dictionary to safe to file results.csv
            results_csv[pic]=[total_name,grade_points]
        else:
            continue
    save_dict_to_file("results.csv",results_csv)
    save_str_to_file("results.txt", results_txt)
    print("Results written to files results.txt and results.csv")
    # read_and_print_file("results.csv")
    # read_and_print_file("results.txt")

    

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