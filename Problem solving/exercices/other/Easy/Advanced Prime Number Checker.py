# Final Goal:
# A program that takes two numbers (start and end) and prints all prime numbers between them, counting the total number of primes found.
# Requirements:
# Validate inputs (start < end, positive numbers).
# Print prime numbers, 10 per line.
# Print "No prime numbers found" if no prime numbers are discovered.
# Print the execution time (use the time module).
import time
import math
line_limit = 10
while True:
    print("Enter the range:")
    try:
        num1 = int(input("The first number: "))
        num2 = int(input("The second number: "))
    except ValueError:
        print("Invalid input: you can enter just a positive integer numbers\n")
        continue
    if num1 > num2:
        print("Invalid input: the first number must be lower than second\n")
        continue
    elif num1 <= 0:
        print("Invalid input: the two numbers must be positive\n")
        continue
    elif num2 >= 1000000:
        print("DANGER!!: this range is very big, i can't let you try that, that is a risk on your computer. The available range is num2 = 999999\n")
        continue
    start_time = time.perf_counter()
    prime_nums = []
    for num in range(num1, num2 + 1):
        if num < 2:
            continue
        sqrt_num = int(math.sqrt(num))
        is_prime = True
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    if prime_nums == []:
        print(f"No prime numbers found in range [{num1}; {num2}]")
    else:
        len_prime_list = len(prime_nums)
        prime_nums_10by10 = ""
        start_sclicing_index = line_limit
        for i, prime_num in enumerate(prime_nums):
            if i == start_sclicing_index:
                prime_nums_10by10 += "\n"
                start_sclicing_index += line_limit
            prime_nums_10by10 += str(prime_num) + " "
        print(prime_nums_10by10)
        print(f"Found {len_prime_list} prime numbers:")
    end_time = time.perf_counter()
    print(f"Processing time: {end_time - start_time} seconds\n")
    while True:
        repeat = input("Do you want to repeat (Yes/No): ").lower()
        if repeat == "yes":
            repeat = True
            break
        elif repeat == "no":
            repeat = False
            break
        else:
            print("Invalid input: You can answer just by 'Yes' or 'No'\n")
            continue
    if repeat:
        print()
        continue
    else:
        break