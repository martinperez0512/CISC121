"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-16
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""


def char_prime(my_char):
    """
    Converts an uppercase letter to a unique prime number 4 Based on the conversion given in the footnote
    :param my_char: a character in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)
    :returns: prime_int = a number unique to the letter
    """
    primes = {
        "A": 2, "B": 3, "C": 5, "D": 7, "E": 11, "F": 13, "G": 17, "H": 19,
        "I": 23, "J": 29, "K": 31, "L": 37, "M": 41, "N": 43, "O": 47, "P": 53,
        "Q": 59, "R": 61, "S": 67, "T": 71, "U": 73, "V": 79, "W": 83, "X": 89,
        "Y": 97, "Z": 101
    }  # create dictionary with prime numbers and their letters
    if my_char not in primes.keys():  # check user input is valid
        print("Error: please enter a string with no spaces")  # tell user input is invalid
        exit()  # exit program
    else:
        prime_int = primes[my_char]
        return prime_int  # return prime number


def primeify(my_string):
    """
    RECURSIVELY gives the product of prime corresponding to the letters in the string
    :param my_string: any string (str)
    :returns: prime_product = the product of all the primes for each letter
    """
    if len(my_string) == 0:
        return 1  # return if string is empty
    else:
        first_char = my_string[0]  # define first character in string
        remaining_chars = my_string[1:]  # define remaining characters
        prime_product = char_prime(first_char) * primeify(remaining_chars)  # recursively give product of other primes
        return prime_product


def is_anagram(string1, string2):
    """
    Determines if two strings are anagrams of each other
    :param string1: any string (str)
    :param string2: any string (str)
    :returns: is_anagram = whether or not they are anagrams (Boolean)
    """
    if primeify(string1) == primeify(string2):  # if strings are anagrams
        return True
    else:
        return False


def radix_sort(nums):
    """
    This function performs a radix sort on the prime numbers list outside the function
    :param nums: the prime list of both s1 and s2 being "primeified"
    :returns: nums: sorted prime numbers for both strings
    """
    radix = 10  # set radix
    max_length = True
    tmp, placement = -1, 1

    while max_length:  # while max_length is True
        max_length = False
        buckets = [list() for _ in range(radix)]  # declare and initialize buckets

        for i in nums:  # split nums between buckets
            tmp = i / placement
            buckets[int(tmp % radix)].append(i)
            if max_length and tmp > 0:
                max_length = True

        a = 0  # empty lists into nums array
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1

        placement *= radix  # move to next digit
    return nums
