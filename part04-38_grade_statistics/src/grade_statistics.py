# In this exercise you will write a program for printing out grade statistics for a 
# university course.

# The program asks the user for results from different students on the course. 
# These include exam points and numbers of exercises completed. The program then 
# prints out statistics based on the results.

# Exam points are integers between 0 and 20. The number of exercises completed is 
# an integer between 0 and 100.

# The program keeps asking for input until the user types in an empty line. 
# You may assume all lines contain valid input, which means that there are two 
# integers on each line, or the line is empty.

# And example of how the data is typed in:

# Sample output
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:

# When the user types in an empty line, the program prints out statistics. 
# They are formulated as follows:

# The exercises completed are converted into exercise points, so that completing 
# at least 10% of the exercises grants one point, 20% grants two points, and so 
# forth. Completing all 100 exercises grants 10 exercise points. The number of 
# exercise points granted is an integer value, rounded down.

# The grade for the course is determined based on the following table:

#   exam points + exercise points	        grade
#       0–14	                            0 (i.e. fail)
#       15–17	                            1
#       18–20	                            2
#       21–23	                            3
#       24–27	                            4
#       28–30	                            5
# There is also an exam cutoff threshold. If a student received less than 10 points from 
# the exam, they automatically fail the course, regardless of their total number of points.

# With the example input from above the program would print out the following statistics:

# Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *
# Floating point numbers should be printed out with one decimal precision.

# NB: this exercise doesn't ask you to write any specific functions, so you 
# should not place any code within an if __name__ == "__main__" block. 
# If any functionality in your program is e.g. in the main function, you should 
# include the code calling this function normally, and not contain it in an if 
# block like in the exercises which specify certain functions.

# Hint:
# The user input in this program consists of lines with two integer values:

# Sample output
# Exam points and exercises completed: 15 87

# You have to first split the input line in two and then convert the sections into 
# integers with the int function. Splitting the input can be achieved in the same 
# way as in the exercise First, second and last words, but there is a simpler way 
# as well. The string method split will chop the input up nicely. You will find more 
# information by searching for python string split online.

# Write your solution here

#--------------------------------------
# Collect data from the students
#--------------------------------------
def collect_data() -> list:
    data_list=[]
    while True:
        student_data=input("Exam points and exercises completed: ")
        if student_data=="":
            break
        data_list.append(student_data)
    return data_list

#--------------------------------------
# Toma una cadena con dos numeros y devuele un puntaje 
# de la conversion de 0 - 100 a 0 - 10
#--------------------------------------
def convert_answered_questions(data_str:str,position:int)->int:
    list_10_2_100 = list(data_str.split(" "))
    number_10_2_100 = int(list_10_2_100[position])
    number_10_2_100 = number_10_2_100/10
    return number_10_2_100

#--------------------------------------
# Grade Calculations this take a list of strings and return a 
# List of integers
#--------------------------------------
def grade_calculations(data_list:list,passing=False)->list:
    grade_list=[]
    for data_pair in data_list:
        answered_questions=convert_answered_questions(data_pair,1)
        exam_points=int(list(data_pair.split(" "))[0])
        if exam_points < 10 and passing==True:
            grade_list.append(0)
        else:
            grade_list.append(int(exam_points+answered_questions))
    return grade_list
#--------------------------------------
# normaliza la escala de 0 a 30 a una escala de 0 a 5
#--------------------------------------
def grade_normalzation(data_number:int)->int:
    data_normal=0
    if data_number>=0  and data_number < 15:
        data_normal=0
    elif data_number>=15  and data_number < 18:
        data_normal=1
    elif data_number>=18  and data_number < 21:
        data_normal=2
    elif data_number>=21  and data_number < 24:
        data_normal=3
    elif data_number>=24  and data_number < 28:
        data_normal=4
    elif data_number>=28  and data_number <= 30:
        data_normal=5
    return data_normal

#--------------------------------------
# Normaliza una lista de valores
#--------------------------------------
def list_normalzation(data_list:list)->list:
    list_normal=[]
    for data in data_list:
        list_normal.append(grade_normalzation(data))
    return list_normal

#--------------------------------------
# Points average function select the average from
#--------------------------------------
def data_average(data_list:list)->float:
    avrg=0
    for data in data_list:
        avrg=avrg + float(data)
    avrg=avrg/len(data_list)
    return avrg

#--------------------------------------
# Pass Percentage function
#--------------------------------------
def data_passing(data_list:list)->float:
    passing=0
    new_list=list_normalzation(grade_calculations(data_list,True))
    for data in new_list:
        if data > 0:
            passing +=1
    passing = 100 * passing/len(new_list)
    return passing

#--------------------------------------
# stars line
#--------------------------------------
def star_line(times):
    i = 0
    line=""
    while i < times or len(line) < times:
        line = line + "*"
        i += 1
    return line

#--------------------------------------
# Frequency in stars
#--------------------------------------
def frequency_stars(data_list:list)->list:
    star_list=[]
    counter_i = 0
    counter_i = data_list.count(5)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(4)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(3)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(2)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(1)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(0)
    stars = star_line(counter_i)
    star_list.append(stars)
    return star_list

#--------------------------------------
# the main function
#--------------------------------------
def main():
    my_list=collect_data()
    processed_list=list_normalzation(grade_calculations(my_list,True))
    print("Statistics:")
    print(f'Points average: {data_average(grade_calculations(my_list)):.1f}')
    print(f'Pass percentage: {data_passing(my_list):.1f}')
    print("Grade distribution:")
    print(f'5: {frequency_stars(processed_list)[0]}')
    print(f'4: {frequency_stars(processed_list)[1]}')
    print(f'3: {frequency_stars(processed_list)[2]}')
    print(f'2: {frequency_stars(processed_list)[3]}')
    print(f'1: {frequency_stars(processed_list)[4]}')
    print(f'0: {frequency_stars(processed_list)[5]}')

# run the main function
main()