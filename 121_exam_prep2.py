"""
Some practice for CISC 121 exam on April 27th 2023 at 9AM in Mitchell hall gym 3
Data structures - @ ln 11
Searching/sorting algorithms - @ ln 147
Searching/sorting algorithms full code - @ ln 262
Recursion - @ ln 397
"""


# # # Data structures # # #

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, elem):
        self.stack.append(elem)
        self.size += 1

    def pop(self):
        if len(self.stack) == 0:
            print("empty")
            return
        elem = self.stack.pop()
        self.size -= 1
        return elem


class Queue:
    def __init__(self):
        self.q = []
        self.size = 0

    def enqueue(self, elem):
        self.q.append(elem)
        self.size += 1

    def dequeue(self):
        # check if the queue is empty
        elem = self.q.pop(0)
        self.size -= 1
        return elem


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = None
        self.size = 0
        self.value = value

    def insert_at_head(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
            return
        # list is not empty
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_in_middle(self, value):
        # suppose the list is sorted in ascending order
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
            return
        # list is not empty
        new_node = Node(value)
        # check if the head node is smaller than the new one
        if new_node.data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        # else the node should go somewhere in the middle of the list
        curr = self.head
        # since we already checked whether the new node should be inserted
        # before the head node, we can go ahead and start checking from
        # the second node (self.head.next)
        # another reason to use curr.next instead of curr is that it allows
        # us to effectively keep 2 pointers: the current node (curr), and the
        # next one (curr.next)
        while curr.next is not None and curr.next.data < new_node.data:
            curr = curr.next
        # here, we have either reached the end of the list, or curr.next
        # is greater than our new node, and the new node should go between
        # curr and curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        # done!

    def insert_at_tail(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
            return
        # list not empty
        new_node = Node(value)
        # iterate through the nodes until we reach the last one
        # we will have reached the last one when curr.next is None
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def delete(self, value):
        if self.size == 0:
            print('empty list')
            return
        # list is not empty
        prev = None
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # if the current node is the head node, we just
                # reassign the head node to be head.next
                if curr is self.head:
                    self.head = self.head.next
                    self.size -= 1
                    return
                # if the current node isn't the head node, we
                # have to reroute the previous node's next to be
                # the current node's next (i.e., skip over curr)
                else:
                    prev.next = curr.next
                    self.size -= 1
                    return
            else:  # we haven't yet found the node to delete
                prev = curr
                curr = curr.next

        # if we get here, curr is None and the node isn't in the list
        print('node not in list')
        return


# # # Searching/sorting algorithms # # #

# Algorithm for bubble sort
# def bubble_sort(mylist):
    """
    for all elements of list
        if list[i] > list[i+1]
            swap list[i], list[i+1]
        end if
    end for
    return list
    """
    pass


# Algorithm for insertion sort
# def insertion_sort(mylist):
    """
    for elements of list from index 1 to n-1
        while the current element is greater than the one
        before it
            swap it with the element before it
            repeat this until it is in the correct place
        end while
    end for
    return mylist
    """
    pass


# Algorithm for selection sort
# def selection_sort(mylist):
    """
    for all elements of the list
        set min to the current element
        for all elements after min
            find the smallest element
        end for
        if the smallest element is not min
            swap the values
        end if
    end for
    return mylist
    """
    pass


# Algorithm for merge sort
# def merge_sort(mylist):
    """
    divide the unsorted list into n sublists, each
    with one element (these sublists are sorted)
    merge the sublists to produce new sorted sublists
    until you have a fully sorted list

    if the list has more than 1 element in it
        declare mid variable and left/right sublists
        recursively sort the two halves; this will
        return sorted left and right sublists
        while there are elements in one or both sublists
            pick the smaller element in the sublists and
            put it in the correct position of the list
        end while
        while there are still elements in one sublist
        but not the other
            add the elements in the sublist to the list
        end while
    end if
    """
    pass


# Algorithm for quick_sort
# def partition(mylist, low, high):
    """
    set rightmost index as pivot
    set a pointer to an element greater than the pivot;
    initialize this to low-1 (invalid index)
    for all elements up to (not including) the pivot
        if current element <= pivot
            increment pointer by 1
            swap this element with the one stored
            in the pointer
        end if
    end for
    increment the pointer by 1
    swap the pivot with the element stored in the pointer
    return the new index of the pivot
    """
    pass


# Algorithm for binary search
# def bin_search(mylist, target):
    """
    Remember that this assumes that the list is sorted.

    set low, high variables for first, last elements to
    examine in the list
    while high ≥ low
        compute middle index mid
        if target == list[mid]
            we are done, return mid
        end if
        if target < list[mid]
            search the left half: high = mid - 1
        end if
        if target > list[mid]
            search the right half: low = mid + 1
        end if
    end while
    """
    pass


# # # Searching/sorting algorithms code # # #

# Bubble sort
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


# Insertion sort
def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        # use j to "walk" along the list from i to 0
        j = i
        while (j > 0) and (mylist[j - 1] > mylist[j]):
            mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
            j -= 1
    return mylist


# Selection sort
def selection_sort(mylist):
    for i in range(len(mylist)):  # complexity n
        # set min to be the current element and j to
        # compare the elements after min to min
        min = i
        j = min + 1
        # find the smallest value
        while j < len(mylist):  # complexity n
            if mylist[j] < mylist[min]:
                min = j
            j += 1
            # if i isn't the smallest value, swap it with min
        if min != i:
            mylist[min], mylist[i] = mylist[i], mylist[min]
    return mylist


# Merge sort
def merge_sort(mylist):
    if len(mylist) > 1:
        # variable for middle index, left and right sublists
        mid = len(mylist) // 2
        L = mylist[:mid]
        R = mylist[mid:]

        # recursively sort the two halves
        merge_sort(L)
        merge_sort(R)

        # now we have sorted sublists
        i, j, k = 0, 0, 0

        # until we run out of elements in L or R, pick
        # the smaller element and put it in the next
        # position of the list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                mylist[k] = L[i]
                i += 1
            else:
                mylist[k] = R[j]
                j += 1
            k += 1

        # when we run out of elements in L or R, put
        # the remaining elements in the list
        while i < len(L):
            mylist[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            mylist[k] = R[j]
            j += 1
            k += 1


# quick_sort
def partition(mylist, low, high):
    # set last element as pivot
    pivot = mylist[high]

    # pointer for greater element
    i = low - 1

    for j in range(low, high):
        # check if the current element is ≤ pivot
        if mylist[j] <= pivot:
            # increment the pointer and swap it with the element
            i += 1
            mylist[i], mylist[j] = mylist[j], mylist[i]

    # swap the pivot with the greater element
    mylist[i + 1], mylist[high] = mylist[high], mylist[i + 1]

    # return the position of the pivot
    return i + 1


def quick_sort(mylist, low, high):
    if low < high:
        # find pivot element with smaller elements on left
        # and larger elements on right
        pivot = partition(mylist, low, high)

        # recursively sort the left and right portions
        quick_sort(mylist, low, pivot - 1)
        quick_sort(mylist, pivot + 1, high)


# Binary search
def bin_search(mylist, target):
    low = 0
    high = len(mylist) - 1
    while high >= low:
        mid = (high + low) // 2
        if target == mylist[mid]:
            return mid
        if target < mylist[mid]:
            high = mid - 1  # search left half
        else:  # target > mylist[mid]
            low = mid + 1  # search right half
    return -1  # if not found


# # # Recursion # # #

# 4. Recursive function to compute sum of digits
def sum_digits(num):
    # Base cases
    if len(str(num)) == 0:
        return 0
    if len(str(num)) == 1:
        return int(num)
    # Recursive case: anything else
    else:
        return (int(str(num)[-1])) + sum_digits(int(str(num)[1:]))


# 5. Recursive function to reverse string
def reverse_string(string):
    # Base cases: empty or length 1
    if len(string) == 0 or len(string) == 1:
        return string
    # Recursive case: anything else
    else:
        return string[-1] + reverse_string(string[:-1])


"""
tracing:
'abc'
'c' + reverse_string('ab')
'c' + 'b' + reverse_string('a')
'c' + 'b' + 'a' = 'cba'
"""
