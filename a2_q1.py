"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360377
Email: 22mp4@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from a2_functions import all_odd_or_even  # import function from the other file


def main():
    """
    This is the main function which calls the other functions from the program and asks the user if they want to
    participate and creates the list of integers/arguments that are passed into the all_odd_or_even function
    :returns: none
    """
    user_input = input("Do you want to participate in this activity? (yes/no) ")  # ask user to play
    if user_input.lower() != "yes":  # returns and exits the program if the user says anything other than yes
        return
    else:
        integers = []  # creates list with the inputs
        while True:
            user_input = input("Enter an integer: ")  # asks user to enter an integer
            try:
                integer = int(user_input)
                integers.append(integer)  # adds to integer list
                user_input = input("Do you want to add another integer? (yes/no) ")  # asks if they want to add again
                if user_input.lower() != "yes":  # exits the loop if the user says anything other than yes
                    break
            except ValueError:  # this tells user they had to input an integer and then exits the program
                print("Invalid input, please enter an integer")
                exit()

        result = all_odd_or_even(*integers)  # calls the all_odd_or_even function with our integers list as the argument
        if result:  # if function returns True it tells user all the arguments are either even or odd
            print("The arguments/integers are all either even or odd")
        else:  # if function returns False it tells the user the arguments are both even and odd
            print("The arguments/integers are NOT all either even or odd")


main()  # calls the main function
