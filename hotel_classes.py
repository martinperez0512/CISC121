"""
CISC-121 2023W
Name: Martin Perez
Student Number: 20360277
Email: 22mp4@queensu.ca
Date: 2023-03-29
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""


class HotelRoom:
    def __init__(self, room_number: int, available: bool):
        """
        Initializes the room object and attributes
        :param room_number: room number, random integer from main program
        :param available: if the room is available or not
        """
        self.room_number = room_number
        self.available = available
        self.guest = None
        self.check_out_date = None

    def is_available(self) -> bool:
        """
        This function checks if the room is available
        :returns: True if room is available, False otherwise
        """
        if self.available:  # if room is available
            return True
        else:  # if room is unavailable
            return False

    def guest_check_in(self, guest):
        """
        This function checks a guest into a room and updates the availability
        :param guest: the guest checking in (guest object)
        :returns: None
        """
        if self.is_available():  # check if rooms are available
            self.guest = guest
            self.available = False  # change availability
        else:
            print(f"Room {self.room_number} is not available")  # print if no rooms are available

    def __str__(self):
        """
        Tell the user which room number is theirs
        :returns: message telling user their room number
        """
        return f"You have checked into room #{self.room_number}"


class StandardRoom(HotelRoom):
    def __init__(self, room_number: int, available: bool):
        """
        Initializes standard room object and attributes
        :param room_number: room number, random integer from main program
        :param available: if the room is available or not
        """
        super().__init__(room_number, available)  # call attributes from parent class
        self.available_date = 0  # since room is smaller, it is available on the same day as the checkout


class Suite(HotelRoom):
    def __init__(self, room_number: int, available: bool):
        """
        Initializes suite object and attributes
        :param room_number: room number, random integer from main program
        :param available:  if the room is available or not
        """
        super().__init__(room_number, available)  # call attributes from parent class
        self.available_date = 1  # add one because of longer cleaning


class TaylorSuite(HotelRoom):
    def __init__(self, room_number: int, available: bool):
        """
        Initializes taylor suite object and attributes
        :param room_number: room number, random integer from main program
        :param available:  if the room is available or not
        """
        super().__init__(room_number, available)  # call attributes from parent class
        self.available_date = 2  # add two because of longer cleaning


class Guest:
    def __init__(self, name, check_out_date):
        """
        Crete guest object from the info given in the main program
        :param name: guests name
        :param check_out_date: guests check out date
        """
        self.name = name
        self.check_out_date = check_out_date
        self.services = []
        self.total_bill = 0

    def add_service(self, service):
        """
        Add a service to the bill of a guest
        Parameters: service (Service): The service to add to the guest's list of services
        Returns: None
        """
        self.services.append(service)  # add service
        self.total_bill += service.cost  # add cost of service to total

    def send_bill(self):
        """
        Based on the total services and bill total provides a printed statement of all services with the total cost
        Parameters: None
        Returns: int: The guest's total bill not including the cost of the room
        """
        print(f"Your total bill is ${self.total_bill}.")
        return self.total_bill


class Service:
    def __init__(self, name: str, cost: int):
        """
        Create the service objects
        :param name: name of service
        :param cost: cost of service
        """
        self.name = name
        self.cost = cost
