"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
import csv
from A3_functions3 import main  # import the main function from functions3.py


def read_csv_file():
    """
    This function reads the csv file stored in the computer and creates a list of dictionaries from the information in
    the file
    :returns: csv file as a list of dictionaries
    """
    data = []  # create empty list
    with open("CISC121_A3/A3_elections_data.csv", newline='', encoding='utf-8-sig') as csvfile:  # open file
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data  # return list of dictionaries


info = read_csv_file()  # store function in the variable
main(info)  # call the main function from the other python file with the csv file data
