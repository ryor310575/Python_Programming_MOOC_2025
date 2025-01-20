# Tuples without parentheses
# The parentheses are not strictly necessary when defining tuples. The following two 
# variable assignments are identical in their results:

# numbers = (1, 2, 3)
# numbers = 1, 2, 3
# This means we can also easily return multiple values using tuples. Let's have 
# alook at he following example:

# def minmax(my_list):
#   return min(my_list), max(my_list)

# my_list = [33, 5, 21, 7, 88, 312, 5]

# min_value, max_value = minmax(my_list)
# print(f"The smallest item is {min_value} and the greatest item is {max_value}")
# Sample output
# The smallest item is 5 and the greatest item is 312


# *********** Student database PART 1 ***********
# NB: Some exercises have multiple parts, and you can receive points for the different 
# parts separately. You can submit a partially completed exercise by choosing 
# 'Submit Solution' from the menu next to the button for executing tests .
# In this series of exercises you will create a simple student database. Before diving 
# in, please spend a moment reading through the instructions and thinking about what 
# sort of data structures are necessary for organising the data stored by your program.

# adding students
# First write a function named add_student, which adds a new student to the database. 
# Also write a preliminary version of the function print_student, which prints out the 
# information of a single student.

# These function are used as follows:

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")
# Your program should now print out

# Sample output
# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database

# Part 2: adding completed courses
# Please write a function named add_course, which adds a completed course to the 
# information of a specific student in the database. The course data is a tuple 
# consisting of the name of the course and the grade:

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")
# When some courses have been added, the information printed out changes:

# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
# ****** Part 3: repeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, 
# if the course is already in the database in that specific student's information, the 
# grade recorded in the database should never be lowered if the course is repeated.

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")
# Sample output
# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5
# ****** Part 4: summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the database.

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)
# This should print out

# Sample output
# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza
# Write your solution here
#Greather Grade for a course
def greather_grade(students_dict: dict, student_name:str, course_name:str)->int:
  courses_grade=[]
  if students_dict.get(student_name) != None:
    for courses_tuples in students_dict[student_name]:
      if courses_tuples[0]==course_name:
        courses_grade.append(courses_tuples[1])
  return max(courses_grade)

# Dictionaty with the greatest grade
def dictionary_greatest_grade(students_dict: dict)->dict:
  new_dictionary={}
  courses_names=[]
  for names, courses_list in students_dict.items():
    courses_names_grades=[]
    for courses_tuples in courses_list:
      if courses_tuples[0] not in courses_names:
        courses_names.append(courses_tuples[0])
        great_grade=greather_grade(students_dict,names,courses_tuples[0])
        courses_names_grades.append((courses_tuples[0],great_grade))
      new_dictionary[names]=courses_names_grades
  return new_dictionary
# Average by studet
def average_grade(students_dict: dict, student_name:str)->int:
  unique_courses_dict=dictionary_greatest_grade(students_dict)
  courses_average=0.0
  course_sum=0
  course_count=0
  if unique_courses_dict.get(student_name) != None:
    course_list=unique_courses_dict[student_name] # Lista de todos los cursos del alumno
    for courses_tuples in course_list:
      if courses_tuples[1]!=0:
        course_sum+=courses_tuples[1]
        course_count+=1
  if course_sum==0 and course_count==0:
    course_count=1
  courses_average= 1.0 * course_sum / course_count
  return courses_average

def print_student(students_dict: dict, name:str):
  course_avrg_grade=0
  course_count=0
  final_report=""
  course_done=""
  # print("*** print_student ***")
  if students_dict.get(name) == None:
    print(f'{name}: no such person in the database')
  elif len(students_dict[name]) == 0:
    print(f'{name}:')
    print(" no completed courses")
  else:
    course_done = ""
    for courses in students_dict[name]:
      course_greather_grade=0
      if courses[1]!=0 and course_done.find(courses[0])==-1:
        course_greather_grade=greather_grade(students_dict, name, courses[0])
        course_done = course_done + f'  {courses[0]} {course_greather_grade}' + "\n"
        course_avrg_grade+=courses[1]
        course_count+=1
    course_done=course_done[:-1]
    if course_count != 0:
      final_report= f'{name}:' + "\n" + f' {course_count} completed courses:' + "\n"
      final_report= final_report + course_done 
      final_report = final_report + "\n" + f' average grade {1.0 * average_grade(students_dict, name):.1f}'
    else:
      final_report= f'{name}:' + "\n" + f' no completed courses' + "\n"
      final_report=final_report[:-1]
    
    print (final_report)

def add_student(students_dict: dict, name:str):
  # print("*** students_dict ***")
  students_dict[name]=[]

def add_course(students_dict: dict, name:str, course:tuple):
  students_dict[name].append(course)


def summary(students_dict:dict):
  unique_courses_dict=dictionary_greatest_grade(students_dict)
  students_courses_completed={}
  courses_grade_avg=[]
  courses_completed_grade=[]
  courses_completed_names=[]
  for students_keys, students_values in unique_courses_dict.items():
    courses_completed=[]
    for courses in students_values:  # Hacemos lista de estudiantes con sus cursos aprobados
      if courses[1] != 0:
        courses_completed.append(courses)
      # Esta lista contiene solo los cursos que pasaron.
      students_courses_completed[students_keys]=courses_completed
  # Hacer la lista de cursos pasados por alumno.
  for students_keys, students_values in students_courses_completed.items():
     # Hacer la lista de cursos pasados por alumno.
    courses_completed_names.append(students_keys)
    courses_completed_grade.append(len(students_values))
     # Hacer la lista de promedio de notas pasados por alumno.
    grade_avg=0
    for grades in students_values:
      grade_avg=(grade_avg+grades[1])
    courses_grade_avg.append(grade_avg/len(students_values))
  max_value=max(courses_completed_grade)
  name_max_value=courses_completed_names[courses_completed_grade.index(max_value)]
  max_avg=max(courses_grade_avg)
  name_max_avg=courses_completed_names[courses_grade_avg.index(max_avg)]

  print(f'students {len(students_dict)}')
  print(f'most courses completed {max_value} {name_max_value}')
  print(f'best average grade {max_avg:.1f} {name_max_avg}')

    




if __name__ == "__main__":
  # print("*** MAIN ***")
  students = {}
  add_student(students, "Peter")
  add_course(students, "Peter", ("Software Development Methods", 1))
  print_student(students, "Peter")
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Software Development Methods", 1))
  add_course(students, "Peter", ("Software Development Methods", 5))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  print_student(students, "Emily")
  print()
  print_student(students, "Peter")
  print()
  print_student(students, "Eliza")
  print()
  summary(students)