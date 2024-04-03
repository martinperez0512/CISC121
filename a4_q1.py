"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from functions import is_anagram

s1 = input("Enter the first string (no spaces): ").upper()  # take string from user (ensured str was in uppercase)
s2 = input("Enter the second string (no spaces): ").upper()  # take string from user (ensured str was in uppercase)

if is_anagram(s1, s2):  # if strings are anagrams
    print("The strings are anagrams!")
else:  # if strings are not anagrams
    print("The strings are not anagrams.")
