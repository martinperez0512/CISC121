"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
from A4_functions import is_anagram, primeify, radix_sort

s1 = input("Enter the first string (no spaces): ").upper()  # take string from user (ensured str was in uppercase)
s2 = input("Enter the second string (no spaces): ").upper()  # take string from user (ensured str was in uppercase)

if is_anagram(s1, s2):  # if strings are anagrams
    print("The strings are anagrams!")
else:  # if strings are not anagrams
    print("The strings are not anagrams.")


def a4_q2(string1, string2):
    """
    This function takes the two strings entered by the user and "primeifies" both strings and sorts them in the
    radix_sort function.
    :param string1: first string entered by the user
    :param string2: second string entered by the user
    :returns: None
    """
    prime_list1 = primeify(string1)  # primeify string1
    prime_list2 = primeify(string2)  # primeify string2

    prime_list = list(set([prime_list1] + [prime_list2]))  # create list of primes

    sorted_primes = radix_sort(prime_list)  # call radix_sort to sort list of primes

    print(f"Sorted list of primes: {sorted_primes}")  # print sorted list


a4_q2(s1, s2)
