"""
Some practice for CISC 121 exam on April 27th 2023 at 9AM in Mitchell hall gym 3
"""


def factorial(n):
    try:
        if n == 0:
            return 1
        else:
            fact_n = n * factorial(n - 1)
            return fact_n
    except TypeError:
        print("please enter an integer")


def main():
    num = int(input("Enter a number: "))
    print(factorial(num))

main()
