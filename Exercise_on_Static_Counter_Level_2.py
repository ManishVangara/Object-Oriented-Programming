"""Write a Python program to generate tickets for online bus booking, based on the class diagram given below.

class Diagram:
        Ticket
    - passenger_name
    - ticket_id
    - source
    - destination
    + counter -> static

    __init__(passenger_name, source, destination)
    + validate_source_destination()
    + generate_ticket()
    + get_ticket_id()
    + get_passenger_name()
    + get_source()
    + get_destination()

Method description:

Initialize static variable counter to 0
validate_source_destination(): Validate source and destination. source must always be Delhi and destination can be either Mumbai, Chennai, Pune or Kolkata. If both are valid, return true. Else return false
generate_ticket():
Validate source and destination
If valid, generate ticket id and assign it to attribute, ticket_id.Ticket id should be generated with the first letter of source followed by first letter of destination and an auto-generated value starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
Else, set ticket_id as None
Note: Perform case insensitive string comparison


For testing:

Create objects of Ticket class
Invoke generate_ticket() method on Ticket object
Display ticket id, passenger name, source, destination
In case of error/invalid data, display appropriate error message"""

class Ticket():
    counter = 0
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source.capitalize()
        self.__destination = destination.capitalize()
        self.__ticket_id = None
        Ticket.counter += 1
    
    def validate_source_destination(self):
        try:
            if self.__source == "Delhi" and (self.__destination == "Mumbai" or self.__destination == "Chennai" or self.__destination == "Pune" or self.__destination == "Kolkata"):
                return True
            else:
                return False
        except:
            print("N/A")
    
    def generate_ticket(self):
        if self.validate_source_destination() == True:
            if Ticket.counter < 10:
                self.__ticket_id = self.__source[0]+self.__destination[0]+'0'+str(Ticket.counter)
            else:
                self.__ticket_id = self.__source[0]+self.__destination[0]+str(Ticket.counter)
        else:
            self.__ticket_id = None
    
    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    
## ChatGPT code:

class Ticket:
    MAX_TICKETS = 10
    counter = 0
    
    def __init__(self, passenger_name, source, destination):
        if not isinstance(passenger_name, str):
            raise TypeError("passenger_name should be a string")
        if not isinstance(source, str):
            raise TypeError("source should be a string")
        if not isinstance(destination, str):
            raise TypeError("destination should be a string")
        self.__passenger_name = passenger_name
        self.__source = source.capitalize()
        self.__destination = destination.capitalize()
        self.__ticket_id = None
        Ticket.counter += 1
    
    def validate_source_destination(self):
        if self.__source == "Delhi" and self.__destination in ("Mumbai", "Chennai", "Pune", "Kolkata"):
            return True
        else:
            raise ValueError("Invalid source or destination")
    
    def generate_ticket(self):
        try:
            self.validate_source_destination()
            if Ticket.counter < Ticket.MAX_TICKETS:
                self.__ticket_id = self.__source[0] + self.__destination[0] + '0' + str(Ticket.counter)
            else:
                self.__ticket_id = self.__source[0] + self.__destination[0] + str(Ticket.counter)
        except ValueError:
            self.__ticket_id = None
    
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_source(self):
        return self.__source
    
    def get_destination(self):
        return self.__destination



"""
Problem Statement:

Even though we can use reference variables to access static values, if we are not careful, we may end up making mistakes which are hard to notice as shown in the below code

class Mobile:
    discount=50
    def display(self):
        print(self.discount)
         #The above line is valid way of accessing static
        print(Mobile.discount)

    def change(self):
        self.discount=40
        #The above line creates a new attribute
        #instead of modifying the static value
        #Now there are two discount variables,
        #one at class level and the other at object level
        #Hence best is to access Static through class name

m1=Mobile()
m1.display()#Will display 50 and 50

m1.change()
m1.display()#Will display 40 and 50
"""

class Mobile:
    discount=50
    def display(self):
        print(self.discount)
         #The above line is valid way of accessing static
        print(Mobile.discount)

    def change(self):
        self.discount=40
        #The above line creates a new attribute
        #instead of modifying the static value
        #Now there are two discount variables,
        #one at class level and the other at object level
        #Hence best is to access Static through class name

m1=Mobile()
m1.display()#Will display 50 and 50

m1.change()
m1.display()#Will display 40 and 50
