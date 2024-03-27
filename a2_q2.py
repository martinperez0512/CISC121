"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360377
Email: 22mp4@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from functions import friends_to_dictionary, friendship_degree  # import functions from the other file


def main():
    """
    This is the main function which calls the other two functions from the other program and executes them
    :returns: none
    """
    friendship_dict = friends_to_dictionary()  # initiates the dictionary
    friendship_degree(friendship_dict)  # calls function with the dictionary


main()  # calls the main function
