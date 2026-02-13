#Write a program that accepts daily temperatures for a month (30 days) as a 2D array.
# +Requirements:
#   -Calculate the average temperature for each week.
#   -Find the coldest and warmest day in the month along with its position (week and day).
#   -Display memory consumption in bytes using float32.
#   -Compare the consumption if you used float64.
# +Constraints:
#   -Temperature range between -50 and 50 degrees Celsius.
#   -Use multidimensional indexing to access elements.

import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturaday", "Sunday"]

def temperature_inputs(month):
    weak = []
    n_days = 0
    while n_days < 7:
        day = float(input(f"-{days[n_days]}: "))
        weak.append(day)
        n_days += 1
    month.append(weak)

while True:
    month = []
    weaks = 0
    print("+Temperature of a month:")
    while weaks < 4:
        print(f"-> Weak {weaks + 1}:")
        temperature_inputs(month)
        weaks += 1
        print()
    
    month = np.array(month, dtype=np.float16)
    # -Calculate the average temperature for each week:
    print("+The average temperature for each week:")
    for i, weak in enumerate(month):
        print(f"-Weak {i + 1}: {weak.mean():.2f}°C")
    print()

    # -Find the coldest and warmest day in the month along with its position (week and day):
    print("+The coldest and warmest day:")
    c_days = []
    w_days = []
    for weak in month:
        c_days.append([weak.argmin(), weak.min()])
        w_days.append([weak.argmax(), weak.max()])
    c_days = np.array(c_days, dtype=np.float16)
    w_days = np.array(w_days, dtype=np.float16)
    print(f"-The coldest day: Weak {c_days[:, 1].min}")
    break