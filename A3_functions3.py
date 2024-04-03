"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
import sys


def display_info(table, district_num):
    """
    This function takes the district number given by the user and prints the corresponding number of polling stations,
    valid ballots, total ballots cast and percentage of voter turnout, it only prints these values and does not return
    them.
    :param table: list of dictionaries
    :param district_num: district number entered by user
    :returns: none
    """
    row = None
    for r in table:  # loop to find user district number in table
        if r["Electoral District Number"] == str(district_num):
            row = r  # change row to r
            break

    if row is None:
        print(f"No data found for electoral district {district_num}")  # tell user district number is invalid
    else:
        num_polling_stations = int(row["Polling Stations"])  # variable for Polling Stations
        num_valid_ballots = int(row["Valid Ballots"])  # variable for Valid Ballots
        total_ballots_cast = int(row["Total Ballots Cast"])  # variable for Total Ballots Cast
        voter_turnout_pct = float(row["Percentage of Voter Turnout"])  # variable for Percentage of Voter Turnout

        print()
        print(f"Polling Stations: {num_polling_stations}, Valid Ballots: {num_valid_ballots}, Total Ballots Cast: "
              f"{total_ballots_cast}, Voter Turnout: {voter_turnout_pct:.2f}%")  # print the info
        print()


def unique_districts(table, province):
    """
    This function takes a province from the user and prints out all the electoral districts within the province/
    territory.
    :param table: list of dictionaries
    :param province: Province/territory entered by user in main function
    :returns: none 
    """
    districts = []  # create empty list
    for row in table:
        if row["Province"] == province:  # check the province in table matches province/territory from user
            district_name = row["Electoral District Name"]  # get corresponding district name
            if district_name not in districts:
                districts.append(district_name)  # add district name to list
    print()
    print(districts)  # print list
    print()


def find_maximum(table, key):
    """
    This function takes a key from the user and searches for the maximum value of that key. It prints out the maximum
    value and the electoral district number it is in. So if the user enters the key "Population" the function prints the
    maximum population and the corresponding electoral district number
    :param table: list of dictionaries
    :param key:
    :returns: none
    """
    max_val = -sys.maxsize  # max value with the imported sys function
    max_district = None  # create maximum district 
    for row in table:
        val = int(row[key].replace(",", ""))
        if val > max_val:
            max_val = val  # new maximum value 
            max_district = row["Electoral District Number"]  # get the corresponding electoral district number
    print()
    print(max_val, ":", max_district)  # print the maximum value and district number
    print()


def find_minimum(table, key):
    """
    This function takes a key from the user and searches for the minimum value of that key. It prints out the minimum
    value and the electoral district number it is in. So if the user enters the key "Population" the function prints the
    minimum population and the corresponding electoral district number
    :param table: list of dictionaries
    :param key: key from user 
    :returns: none
    """
    min_val = None  # create minimum value
    min_district = None  # create minimum district
    for row in table:
        val = int(row[key])
        if min_val is None or val < min_val:
            min_val = val  # new minimum value
            min_district = row["Electoral District Number"]  # get the corresponding electoral district number
    print()
    print(min_val, ":", min_district)  # print the minimum value and district number
    print()


def total_votes(table):
    """
    This function counts the total votes in each province/territory and prints out all the provinces and territories
    with the total ballots cast in alphabetical order.
    :param table: list of dictionaries
    :returns: none
    """
    provinces = {}
    for district in table:
        province = district["Province"]  # get the provinces/territories in list of dictionaries
        total_ballots = district["Total Ballots Cast"]  # get total ballots cast from each electoral district
        if province in provinces:
            provinces[province] += int(total_ballots)  # add the ballots
        else:
            provinces[province] = int(total_ballots)
    result = []
    print()
    print("Total Votes:")
    for province in sorted(provinces.keys()):  # sort the provinces into alphabetical order
        total = provinces[province]
        result.append({"Province": province, "Total Ballots Cast": total})  # add province and total to list
        print(province + ': ' + str(total))  # print list with province and total
    print()


def selection_sort(table, key):
    """
    This function sorts the table(list of dictionaries) by the key entered by the user in increasing order. So if the
    user enters the key "Population" the function will sort the table by size of population, so from the electoral
     district with the lowest population to the district with the highest population.
    :param table: list of dictionaries
    :param key: key from user
    :return:
    """
    if table and any(key in d for d in table):  # checks if key from user is valid
        n = len(table)
        for i in range(n - 1):
            min_index = i  # initial minimum index
            for j in range(i + 1, n):
                if int(table[j][key]) < int(table[min_index][key]):
                    min_index = j  # change the minimum index
            if i != min_index:
                table[i], table[min_index] = table[min_index], table[i]  # swap
        return table
    else:
        return None  # returns none if key is invalid


def binary_search(table, target):
    """
    This function takes a variable target from the user and uses a binary search to search for the percentage of voter
    turnout in the district which the user enters the electoral district number.
    :param table: list of dictionaries
    :param target: electoral district number from user
    :returns: percentage of voter turnout in the target electoral district number
    """
    table = selection_sort(table, "Electoral District Number")  # sort Electoral District Number for the binary search
    low = 0
    high = len(table) - 1

    while low <= high:
        mid = (low + high) // 2
        if table[mid]["Electoral District Number"] == str(target):
            return table[mid]["Percentage of Voter Turnout"]  # return percentage of voter turnout
        elif table[mid]["Electoral District Number"] < str(target):
            low = mid  # shorten the list
        else:
            high = mid  # shorten the list

    return None  # return none if percentage of voter turnout is not found


def main(info):
    """
    This is the main function which is called in the other program. It has a menu where the user enters a number for
    which function they want to call.
    :param info: function which creates the list of dictionaries from the a3_q1 program which is used all throughout the
    python program
    :returns: none
    """
    print("Welcome \n Enter a corresponding choice number for the option you would like \n 1 = Display information"
          " for an electoral district \n 2 = Show unique districts by the given province \n 3 = Find the maximum of any"
          " value \n 4 = Find the minimum of any value \n 5 = Total votes each province/territory \n 6 = Sort a key"
          " into increasing order \n 7 = View percentage of voter turnout for specific district \n Any other number"
          " = exit program")  # show user menu
    user_choice = int(input("Enter your choice here: "))  # get option from user
    while True:  # used while loop so user can stay in the program as long as they want
        if user_choice < 1 or user_choice > 7:
            print("Thank you for visiting")
            exit()  # exit program if user enters number not in the menu
        else:
            if user_choice == 1:
                user_number = int(input("Enter the district number you would like to see data for: "))
                display_info(info, user_number)  # call function with district number
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 2:
                user_province = input("Enter the province here: ")  # get province from user
                unique_districts(info, user_province)  # call function with province/territory
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 3:
                print("Options are:\nPopulation, Electors, Polling Stations, Valid Ballots, Rejected Ballots, and "
                      "Total Ballots Cast")  # show user valid options
                user_key = input("Enter which data you would like to see the maximum value: ")
                find_maximum(info, user_key)  # call function with key
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 4:
                print("Options are:\nPopulation, Electors, Polling Stations, Valid Ballots, Rejected Ballots, and "
                      "Total Ballots Cast")  # show user valid options
                user_key = input("Enter which data you would like to see the maximum value: ")
                find_minimum(info, user_key)  # call function with key
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 5:
                total_votes(info)  # call function
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 6:
                user_key = input("Enter which data you would like to sort: ")  # get key from user
                test = selection_sort(info, user_key)  # call function
                if test:  # if user_key is in info
                    print()
                    print(f"Sorted by {user_key}")
                    print()
                else:  # if user_key is not in info
                    print()
                    print("Invalid key")
                    print()
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))

            elif user_choice == 7:
                electoral_dist_num = int(input("Enter the Electoral District Number here: "))
                search = binary_search(info, electoral_dist_num)  # call function
                if search:  # if district number is in info
                    print()
                    print(f"Found: {electoral_dist_num} = {search}%")
                    print()
                else:  # if district info is not in info
                    print()
                    print("Item was not found")
                    print()
                user_choice = int(input("Enter your choice here (refer to the number index above for your choice): "))
