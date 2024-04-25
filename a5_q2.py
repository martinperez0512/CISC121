"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from stack_classes import Stack


def main():
    """
    Main function where the user is asked for values used to create the stack and print both the original input and the
    reversed stack.
    :returns: none
    """
    user_input = input("Enter a list of values separated by spaces: ")  # ask for values
    values = user_input.split()  # split values
    s = Stack()  # create stack object
    for value in values:  # for each value entered by the user
        s.push(value)  # add user values to the stack

    print("Original stack:", ' '.join(s.items))  # print original stack
    s.reverse()  # call method to reverse the stack
    print("Reversed stack:", ' '.join(s.items))  # print reversed stack


main()
