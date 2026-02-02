# A program that tracks your weekly workouts (6 days × 4 exercises).
# Requirements:
#   Create a 6×4 matrix.
#   Calculate the maximum and minimum exercise for each day.
#   Calculate the total weekly time for each exercise.
#   Display the best training day (highest total time).
#   Compare float64 vs uint16 (since minutes are positive numbers).

import numpy as np

weak_exercises_time = [] # I do this to escape create a new 'array' all the time. we append to list (because append in array create a new array don't append actualy), and after we will create a single array

def exercise_inputs(weak):
    day = []
    n = 0
    while n < 4:
        exercise = int(input(f"Exercise {n + 1}: "))
        day.append(exercise)
        n += 1 # I put this line here, because number of exercises up actualy after line 'x.append(exercise)'
    weak.append(day)

while True:
    n = 0
    while n < 6:
        if n == 0:
            print("Monday:")
            exercise_inputs(weak_exercises_time)
        elif n == 1:
            print("Tuesday:")
            exercise_inputs(weak_exercises_time)
        elif n == 2:
            print("Wednesday:")
            exercise_inputs(weak_exercises_time)
        elif n == 3:
            print("Thursday:")
            exercise_inputs(weak_exercises_time)
        elif n == 4:
            print("Friday:")
            exercise_inputs(weak_exercises_time)
        else:
            print("Saturday:")
            exercise_inputs(weak_exercises_time)
        n += 1
        print()
    weak_exercises_time = np.array(weak_exercises_time, dtype=np.uint16)
    
    print(weak_exercises_time)
    print(weak_exercises_time.ndim)
    break