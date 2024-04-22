"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
##define variables
x = float(0)
y = float(0)

import math
## (x ** 2) + (y ** 2) = (z ** 2)
try:
    x = float(input("Please enter a number: "))
    y = float(input("Please enter another number: "))
    a = input("is one of the numbers the hypotenuse of a right triangle? ")
except:
    print("error: you inputed a non-number")
try:
    if a == "Yes" or a == "yes" or a == "y":
        if x > y:
            zz = (x**2) - (y**2)
            z = zz**0.5
            z = round(z, 1)
            print(f"the lenght of the missing side is {z}")
        elif y > x:
            zz = (y**2) - (x**2)
            z = zz**0.5
            z = round(z, 1)
            print(f"the lenght of the missing side is {z}")
        elif y == x:
            print("no it isnt you fool")
    elif a == "No" or a == "no" or a == "n":
        print("good for you then")
    elif a != "yes" and a != "Yes" and a != "no" and a != "No" and a != "n" and a != "y":
        print("your input is invalid.")
except:
    print("your input is invalid")