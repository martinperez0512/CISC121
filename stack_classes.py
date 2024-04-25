"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""


class Stack:
    def __init__(self):
        """
        Initialize values from the user
        """
        self.items = []  # user values stored in a list

    def push(self, item):
        """
        Add item from user to stack
        :param item: item entered by user
        :returns: none
        """
        self.items.append(item)  # add item to stack

    def reverse(self):
        """
        Reverse the stack of items entered by the user
        :returns: none
        """
        self.items = self.items[::-1]  # reverse stack
