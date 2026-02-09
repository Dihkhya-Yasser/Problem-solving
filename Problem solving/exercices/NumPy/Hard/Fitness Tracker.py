# A program that tracks your weekly workouts (6 days × 4 exercises).
# Requirements:
#   Create a 6×4 matrix.
#   Calculate the maximum and minimum exercise for each day.
#   Calculate the total weekly time for each exercise.
#   Display the best training day (highest total time).
#   Compare float64 vs uint16 (since minutes are positive numbers).

import numpy as np

weak_days_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weak_exercises_time = [] # I do this to escape create a new 'array' all the time. we append to list (because append in array create a new array don't append actualy), and after we will create a single array

def exercise_inputs(weak):
    day = []
    n = 0
    while n < 4:
        try:
        	exercise = int(input(f"Exercise {n + 1}: "))
        except ValueError:
        	print("Invalid input: the time must be positive integer")
        	print()
        	continue
        if exercise < 0:
        	print("Invalid input: the time can't be negative")
        	print()
        	continue
        elif exercise > 240:
        	print("Invalid input: this time is impossible and not available")
        	print()
        	continue
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
        
    # -Create a 6×4 matrix:
    weak_exercises_time = np.array(weak_exercises_time, dtype=np.uint16)
    
    # -Calculate the maximum and minimum exercise for each day:
    print("+the maximum and minimum exercise:")
    for name, day in zip(weak_days_name, weak_exercises_time):
    	print(f"-{name}:")
    	print(f"Min: exercise {day.argmin() + 1} --> {day.min()} minutes")
    	print(f"Max: exercise {day.argmax() + 1} --> {day.max()} minutes")
    	print()
    
    # -Calculate the total weekly time for each exercise:
    print("+The total weekly time for each exercise:")
    for n in range(4):
    	print(f"-Exercise {n + 1}: {weak_exercises_time[:, n].sum()} minutes")
    print()
    
    # -Display the best training day (highest total time):
    total_time_days = np.array([weak_exercises_time[0].sum(), weak_exercises_time[1].sum(), weak_exercises_time[2].sum(), weak_exercises_time[3].sum(), weak_exercises_time[4].sum(), weak_exercises_time[5].sum()], dtype=np.uint16)
    print(f"+The best training day: {weak_days_name[total_time_days.argmax()]} --> {total_time_days.max()} minutes")
    print()
    
    # -Compare float64 vs uint16 (since minutes are positive numbers):
    float64 = weak_exercises_time.astype(np.float64).nbytes
    uint16 = weak_exercises_time.nbytes
    print("+Compare float64 vs uint16:")
    print(f"-float64: {float64} bytes")
    print(f"-uint16: {uint16} bytes")
    print(f"-Defference: {float64 - uint16} bytes")
    print()
    
    # Repeat:
    while True:
    	repeat = input("Do you want to repeat ? (Yes/No): ").lower()
    	if repeat == "yes" or repeat == "no":
    		break
    	else:
    		print("Invalid input: you can answer just by 'Yes' or 'No'")
    		print()
    		continue
    
    if repeat == "yes":
    	print()
    	continue
    else:
    	break
