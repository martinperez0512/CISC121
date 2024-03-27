"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360377
Email: 22mp4@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""


def all_odd_or_even(*args):
    """
    This function takes all the arguments from in the main function and determines if the argument is empty, if they are
    integers and if they are all even or odd
    :param args: integers from the main function
    :returns: True if all the integers are even or odd, False otherwise
    """
    if len(args) == 0:  # returns False if nothing is in the args list
        return False
    for arg in args:  # checks all the elements in the list
        if not isinstance(arg, int):  # returns False if argument is not an integer
            return False
    if all(x % 2 == 0 for x in args) or all(x % 2 == 1 for x in args):  # checks if all integers are even or odd
        return True
    return False  # returns False if none of the conditions are met


def friends_to_dictionary():
    """
    This function initializes the friendship dictionary from the txt file and returns the dictionary
    :returns: friendship dictionary
    """
    friendship = {}  # creates empty dictionary
    with open("a2_friendship.txt", "r") as f:  # opens file. had to use
        # full file path since it was not opening properly
        for line in f:
            try:
                person, friend = line.strip().split("\t")
                if person not in friendship:
                    friendship[person] = []
                if friend not in friendship:
                    friendship[friend] = []
                friendship[person].append(friend)
                friendship[friend].append(person)
            except ValueError:
                return None
    return friendship  # returns dictionary


def all_my_friends(friend, friends_dict):
    """
    This function takes the friend input from the outer function and returns the input's friends or tells the user the
    input is not in the dictionary
    :param friend: input friend from the user in the main function
    :param friends_dict: dictionary with friends
    :returns: the friend and their friends
    """
    if friend not in friends_dict:  # checks input is in the dictionary
        print(f"{friend} not in the dictionary")
    else:
        return friends_dict.get(friend, [])  # returns corresponding friends of the input


def friendship_degree(friends_dict):
    """
    This function iterates over the dictionary and prints all the friends and who they are friends with line by line
    :param friends_dict: input friend from the user in the main function
    :returns: none
    """
    for friend in friends_dict:
        print(f"{friend} has {len(friends_dict[friend])} friends: {friends_dict[friend]}")
