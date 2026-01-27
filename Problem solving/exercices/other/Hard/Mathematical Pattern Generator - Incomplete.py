# Final Goal:
# A program that takes a number n and prints 5 different mathematical patterns based on n.
# Requirements:
# Pattern 1: Ascending number triangle.
# Pattern 2: Descending number triangle.
# Pattern 3: Symmetric number pyramid.
# Pattern 4: Spiral number square.
# Pattern 5: Pascal's Triangle.
while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input: the number must be positive integer")

    #---Pattern 1---
    x = 0
    while x != n:
        x += 1
        result = ""
        for i in range(1, x + 1):
            result += str(i) + " "
        print(result)
    print()
    
    #---Pattern 2---
    x = n
    while x != 0:
        result = ""
        for i in range(1, x + 1):
            y = n + 1
            y -= i
            result += str(y) + " "
        x -= 1
        print(result)
    print()
    
    #---Pattern 3---
    x = 0
    y = 0
    while x != n:
        y += 2
        result = ""
        for i in range(1, n + x):
            result += " "
            if i == n + x - 1 or i == n + x - y:
                result += str(x + 1)
            break
        x += 1
        print(result)
    print()