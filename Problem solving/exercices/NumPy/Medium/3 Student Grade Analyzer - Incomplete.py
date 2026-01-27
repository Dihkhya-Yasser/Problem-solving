# A program that accepts grades for 3 students in 3 subjects (a 3x3 matrix).
# Requirements:
#   Calculate the average grade for each student.
#   Calculate the average grade for each subject.
#   Print the ID of the student with the highest average.
#   Calculate memory usage with float64 versus float16 and print the difference.
#   Validate inputs: Grades must be between 0 and 100.
# Condition: Do not use loops for mathematical calculations (use NumPy functions only).

# "math": float(input("Math: ")),
# "p_a_c": float(input("Physics and Chemistry: ")),
# "english": float(input("English: "))
# raise Exception("Invalid input: the grade must be between 0 and 100")

import numpy as np

class Student:
    def __init__(self, name, grades):
        self.__name = name
        self.__grades = grades

    def get_name(self):
        return self.__name
    def get_grades(self):
        return self.__grades
    
def student_inputs():
    name = input("Enter his name: ")
    print("Enter his grades:")
    grades = {}
    grades["math"] = float(input("Math: "))
    #if grades.
    return Student(name, grades)

students = []
while True:
    while len(students) != 3:
        if Student.number_of_students == 0:
            print("The first student:")
        elif Student.number_of_students == 1:
            print("The second student:")
        else:
            print("The third student:")
        try:
            student = student_inputs()
            students.append(student)
            print()
        except ValueError:
            print("Invalid input: the grades must be float numbers")
        except Exception:
            continue
