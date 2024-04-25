"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
import a5_hotel_classes
import random


def create_standard_rooms():
    """
    This function creates all the standard room objects and stores them in a list that is returned to the main program.
    The reason why in line it says (i + 100) is so that the room gets a unique room number and + 100 is to show that it
    is on the first floor (room 101, 124 etc.). The same is true for the other room types but since they are on
    different floors it shows i + 200 and i + 300.
    :returns: standard_rooms, list with all the standard room objects
    """
    standard_rooms = []  # create empty list
    for i in range(1, 90):  # iterate over the amount of rooms
        stand_room = a5_hotel_classes.StandardRoom(i + 100, True)  # create room object
        standard_rooms.append(stand_room)  # add to list
    return standard_rooms  # return list


def create_suites():
    """
    This function creates all the suite objects and stores them in a list that is returned to the main program
    :returns: suites, list with all the suite objects
    """
    suites = []  # create empty list
    for i in range(1, 20):  # iterate over the amount of rooms
        suite_room = a5_hotel_classes.Suite(i + 200, True)  # create room object
        suites.append(suite_room)  # add to list
    return suites  # return list


def create_taylor_suites():
    """
    This function creates all the taylor suite objects and stores them in a list that is returned to the main program
    :returns: standard_rooms, list with all the taylor suite objects
    """
    taylor_suites = []  # create empty list
    for i in range(1, 14):  # iterate over the amount of rooms
        taylor_suite = a5_hotel_classes.TaylorSuite(i + 300, True)  # create room object
        taylor_suites.append(taylor_suite)  # add to list
    return taylor_suites  # return list


def main():
    """
    This is the main function which contains the menu for the user to check in and add services/see the bill
    :returns: None
    """
    standard_rooms = create_standard_rooms()  # variable for standard room objects
    suites = create_suites()  # variable for suite objects
    taylor_suites = create_taylor_suites()  # variable for taylor suite objects
    print("Welcome")
    guest_choice = int(input("Press 1 to check in or 2 to exit: "))  # ask user if they want to check in
    while True:
        if guest_choice == 1:
            print("Please enter the following information:")  # get name, room type and checkout date from user
            guest_name = input("Your name: ")
            guest_room_type = input("What kind of room you would like? (Standard, Suite or Taylor Suite): ").lower()
            guest_check_out_date = input("Until what date do you plan on staying? (enter as YYYY-MM-DD) ")
            guest_1 = a5_hotel_classes.Guest(guest_name, guest_check_out_date)  # create guest object

            if guest_room_type == "standard":  # if user chooses standard room
                standard = a5_hotel_classes.StandardRoom(random.choice(standard_rooms), True)  # pick random room
                if standard.is_available():  # if room is available
                    standard.guest_check_in(guest_1)  # check in with guest info
                    print(standard.room_number)  # show guest their room number
                else:  # if room is not available
                    print(f"Sorry, no {guest_room_type} rooms are available")
            elif guest_room_type == "suite":  # if user chooses suite
                suite = a5_hotel_classes.Suite(random.choice(suites), True)  # pick random room
                if suite.is_available():  # if room is available
                    suite.guest_check_in(guest_1)  # check in with guest info
                    print(suite.room_number)  # show guest their room number
                else:  # if room is not available
                    print(f"Sorry, no {guest_room_type} rooms are available")
            elif guest_room_type == "taylor suite":  # if user chooses taylor suite
                taylor_suite = a5_hotel_classes.TaylorSuite(random.choice(taylor_suites), True)  # pick random room
                if taylor_suite.is_available():  # if room is available
                    taylor_suite.guest_check_in(guest_1)  # check in with guest info
                    print(taylor_suite.room_number)  # show guest their room number
                else:  # if room is not available
                    print(f"Sorry, no {guest_room_type} rooms are available")
            else:  # if user enters invalid room type
                print("Enter a valid room type")
                return  # return

            print("Would you like any additional services? \nSnacks = $10 \nTaxi = $20\nMovie = $5 ")  # print services
            snacks = a5_hotel_classes.Service("Snacks", 10)  # create service object
            taxi = a5_hotel_classes.Service("Taxi", 20)  # create service object
            movie = a5_hotel_classes.Service("Movie", 5)  # create service object
            guest_service = input("Enter services you would like (put none if you don't want services): ").lower()
            if "snacks" in guest_service:  # check if user wants this service
                a5_hotel_classes.Guest.add_service(guest_1, snacks)  # add to guest object
            if "taxi" in guest_service:  # check if user wants this service
                a5_hotel_classes.Guest.add_service(guest_1, taxi)  # add to guest object
            if "movie" in guest_service:  # check if user wants this service
                a5_hotel_classes.Guest.add_service(guest_1, movie)  # add to guest object

            guest_total = input("Would you like to see your total bill? (yes/no) ").lower()  # ask if user wants bill
            if guest_total == "yes":  # if user wants to see bill. Room costs are not included (professor said it's OK)
                a5_hotel_classes.Guest.send_bill(guest_1)  # call method with guest input and print bill
            else:  # if user does not want to see bill
                print("OK, enjoy your stay!")

            guest_choice = int(input("Press 1 to check in or 2 to exit "))  # ask if user wants to check in again

        else:  # if initial input is invalid
            exit()


main()
