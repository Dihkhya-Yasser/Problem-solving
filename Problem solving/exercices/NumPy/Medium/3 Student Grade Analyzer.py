# A program that accepts grades for 3 students in 3 subjects (a 3x3 matrix).
# Requirements:
#   Calculate the average grade for each student.
#   Calculate the average grade for each subject.
#   Print the ID of the student with the highest average.
#   Calculate memory usage with float64 versus float16 and print the difference.
#   Validate inputs: Grades must be between 0 and 100.
# Condition: Do not use loops for mathematical calculations (use NumPy functions only).

import numpy as np

school_subjects = ["Math", "Physics and Chemistry", "English"] # Number of subjects

def check_grade_name(grade, name=""):
    # -Validate inputs: Grades must be between 0 and 100:
    if grade < 0 or grade > 100:
        print("Invalid input: the grade must be between 0 and 100")
        raise Exception
    if len(name) > 30:
        print("Invalid input: the name is very long, the limit is 30 charachers")
        raise Exception
def student_inputs():
    name = input("Enter his name: ")
    check_grade_name(0, name)
    print("Enter his grades:")
    math = float(input("Math: "))
    check_grade_name(math)
    p_a_c = float(input("Physics and Chemistry: "))
    check_grade_name(p_a_c)
    english = float(input("English: "))
    check_grade_name(english)

    students.append(name)
    return [math, p_a_c, english]

while True:
    grades = []
    students = []
    number_of_students = 0

    print("="*50+"// Intputs \\\\"+"="*50)

    while number_of_students < len(school_subjects):
        if number_of_students == 0:
            print("The first student:")
        elif number_of_students == 1:
            print("The second student:")
        else:
            print("The third student:")
        try:
            grades.append(student_inputs())
        except ValueError:
            print("Invalid input: the grades must be float numbers")
            continue
        except Exception:
            continue
        finally:
            print()
        number_of_students += 1
    grades = np.array(grades, dtype=np.float16)

    print("="*50+"// Outputs \\\\"+"="*50)

    # -Calculate the average grade for each student:
    print("The average grade for each student:")
    average_grades_students = np.array([grades[0].mean(), grades[1].mean(), grades[2].mean()], dtype=np.float16)
    n = 0
    while n < len(school_subjects):
        print(f"{students[n]}: {average_grades_students[n]:.2f}")
        n += 1
    print()

    # -Calculate the average grade for each subject:
    print("the average grade for each subject:")
    average_grades_subjects = np.array([grades[:, 0].mean(), grades[:, 1].mean(), grades[:, 2].mean()], dtype=np.float16)
    
    print(f"Math: {average_grades_subjects[0]:.2f}")
    print(f"Physics and Chemistry: {average_grades_subjects[1]:.2f}")
    print(f"English: {average_grades_subjects[2]:.2f}")
    print()

    # -Print the ID of the student with the highest average:
    print(f"The student with the highest average: {students[np.argmax(average_grades_students)]}")
    print()

    # -Calculate memory usage with float64 versus float16 and print the difference:
    print("Calculate memory")
    print(f"Memory usage with flaot64: {grades.astype(np.float64).nbytes} bytes")
    print(f"Memory usage with flaot16: {grades.nbytes} bytes")
    print(f"Difference: {grades.astype(np.float64).nbytes - grades.nbytes} bytes")
    print()

    print("="*25+"// Repet \\\\"+"="*25)

    # -Repeat:
    while True:
        repeat = input("Do you want to repeat (Yes/No): ").lower()
        if repeat == "yes" or repeat == "no":
            break
        else:
            print("Invalid input: you can ansewr just by 'Yes' or 'no'")
            print()
    if repeat == "yes":
        continue
    else:
        break
