# A program that accepts daily temperatures for a week (7 float values) from the user, then:
# -Converts all temperatures from Celsius to Fahrenheit.
# -Calculates the average temperature.
# -Displays the maximum and minimum temperatures.
# -Stores the data using the minimum possible memory space (use an appropriate dtype).
# -Displays the consumed memory size.
# Requirements: Use vectorized NumPy operations (no for loops for conversion), print the array size in bytes.

import numpy as np

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturaday", "Sunday"]

while True:
    print("Enter daily temperatures for a week:")

    try:
        t_c_monday = float(input("Monday: "))
        t_c_tuesday = float(input("Tuesday: "))
        t_c_wednesday = float(input("Wednesday: "))
        t_c_thursday = float(input("Thursday: "))
        t_c_friday = float(input("Friday: "))
        t_c_saturday = float(input("Saturaday: "))
        t_c_sunday = float(input("Sunday: "))
    except ValueError:
        print("Invalid input: you can enter just a float numbers")
        print()
        continue
    
    daily_t_c_week = np.array([t_c_monday, t_c_tuesday, t_c_wednesday, t_c_thursday, t_c_friday, t_c_saturday, t_c_sunday], dtype=np.float64)
    t_min = daily_t_c_week.min()
    t_max = daily_t_c_week.max()
    if t_min >= -65504.0 and t_max <= 65504.0:
        daily_t_c_week = daily_t_c_week.astype(np.float16)
    elif t_min >= -3.4028235e+38 and t_max <= 3.4028235e+38:
        daily_t_c_week = daily_t_c_week.astype(np.float32)
    else:
        daily_t_c_week = daily_t_c_week.astype(np.float64)

    # -Converts all temperatures from Celsius to Fahrenheit:
    print()
    print("+Celsius to Fahrenheit:")
    daily_t_f_week = daily_t_c_week * 1.8 + 32
    for d, t in zip(week_days, daily_t_f_week):
        print(f"{d}: {t:.2f}°F")

    # -Calculates the average temperature:
    print()
    t_c_week = daily_t_c_week.mean()
    print(f"+The average temperature: {t_c_week:.2f}°C")

    # -Displays the maximum and minimum temperatures:
    print()
    t_min_day = week_days[daily_t_c_week.argmin()]
    t_max_day = week_days[daily_t_c_week.argmax()]
    print(f"+The minimum temperature: {t_min_day} {t_min}°C")
    print(f"+The maximum temperature: {t_max_day} {t_max}°C")

    # -Displays the consumed memory size:
    print()
    print(f"+Your data take {daily_t_c_week.nbytes} bytes in memory")

    # -Repeat:
    while True:
        print()
        repeat = input("Do you want to repeat? (Yes/No): ").lower()
        if repeat == "yes":
            break
        elif repeat == "no":
            break
        else:
            print("Invalid input: you can answer just by Yes or No")
            continue
    if repeat == "yes":
        print()
        continue
    else:
        break