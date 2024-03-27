"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360377
Email: 22mp4@queensu.ca
Date: 2023-01-18
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
import random


def is_valid(num1, num2):  # function to check if the numbers are valid
    if 10 <= (num1 - num2) <= 50:
        return True


def print_number(num):  # function to print the numbers and the conditions
    output = ""  # empty string
    if num % 5 == 0:
        output += "apple "
    if num % 7 == 0:
        output += "pen "
    if "3" in str(num):
        output += "pineapple "
    if output:  # if the number meets the conditions it will print a string with the conditions met
        print(output)
    else:
        print(num)  # prints just the integer


def main():  # main function
    num1 = random.randint(0, 100)  # generate the numbers
    num2 = random.randint(0, 100)
    while is_valid(num1, num2):  # while the function returns True the bottom conditions will be applied
        if num1 > num2:
            if num1 - num2 < 10:
                num1 = 2 * num1
            elif num1 - num2 > 50:
                num1 = (num1 + 2) // 3
        else:
            if num2 - num1 < 10:
                num2 = 2 * num2
            elif num2 - num1 > 50:
                num2 = (num2 + 2) // 3
    print("This pair of integers is valid:", num1, num2)
    for i in range(min(num1, num2), max(num1, num2) + 1):  # for loop to check the conditions of the numbers
        print_number(i)  # calls the function and prints the numbers


main()
