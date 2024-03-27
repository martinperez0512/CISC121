"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360377
Email: 22mp4@queensu.ca
Date: 2023-01-18
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
import random


def add_yourself():
    """
    This function adds my info to the txt file. Since my info only needs to appear once in the final txt file, this
    function is only called once
    :return: none
    """
    your_name = input("Enter your name: ")
    your_age = str(input("Enter your age: "))
    your_favourite_colour = input("Enter your favourite colour ")
    with open("myspace_profiles.txt", "a") as file:  # adds my name and info to the file
        file.write("\n-\n" + your_name + "\n" + your_age + "\n" + your_favourite_colour + "\n")


def add_other_people():
    """
    This function allows the user to add more people to the txt file. The user enters the name they want and the age
    and colour are randomly selected.
    :return: none
    """
    name = input("Enter the name of the person you want to add: ")
    age = str(random.randint(18, 22))
    colors = ["green", "red", "yellow", "pink", "blue", "orange"]
    color = random.choice(colors)
    with open("myspace_profiles.txt", "a") as file:  # adds the name and info the file
        file.write("\n-\n" + name + "\n" + age + "\n" + color + "\n")


def main():
    """
    This is the main function. Here the other functions are called, the add_yourself function is not called since I
    already entered my info and so the function doesn't need to be called again.
    """
    add_other_people()  # calls function
    with open("myspace_profiles.txt", "r") as file:  # prints the file with the new info
        print(file.read())


main()
