"""
Some practice for CISC 121 exam on April 27th 2023 at 9AM in Mitchell hall gym 3
"""
test = [5, 2, 3, 7, 8, 4, 1, 9, 6]


def bubble_sort(mylist):
    end = len(mylist) - 1
    swap = True
    while swap:
        swap = False  # flip to True if elements are swapped
        # can you think of why we use end instead of len(mylist)?
        for i in range(0, end):
            if mylist[i] > mylist[i + 1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
                swap = True
        # since bubble sort moves the greatest element to the end
        # we can set our end point to one less each time
        end = end - 1
    return mylist


print(bubble_sort(test))
