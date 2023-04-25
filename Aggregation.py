"""
If a class A owns class B, then A is said to aggregate class B.
This is also commonly known as "has-A" relationship.
For Example, in our shopping app, a Customer has an Address. 
First let us look at the Customer class and Address class independently.
"""
# class Customer():
#     def __init__(self, name, age, phone_no):
#         self.__name = name
#         self.__age = age
#         self.__phone_no = phone_no
    
#     def view_details(self):
#         pass
#     def update_details(self):
#         pass

# class Address():
#     def __init__(self, door_no, street, area, pincode):
#         self.__door_no = door_no
#         self.__street = street
#         self.__area = area
#         self.__pincode = pincode
    
#     def update_address(self):
#         pass

# ## Adding the extra attribute in the Customer class so that it can aggregate the Address class as shown below:

# class Customer():
#     def __init__(self, name, age, phone_no, address):
#         self.__name = name
#         self.__age = age
#         self.__phone_no = phone_no
#         self.__address = address
    
#     def view_details(self):
#         pass
#     def update_details(self):
#         pass

# class Address():
#     def __init__(self, door_no, street, area, pincode):
#         self.__door_no = door_no
#         self.__street = street
#         self.__area = area
#         self.__pincode = pincode

#     def update_address(self):
#         pass

# # Address of Jack
# add1 = Address(123, "5th Lane", 56001)
# # Address of Jane Arin
# add2 = Address(567, "6th Lane", 82006)

# # Customer Jack
# cus1 = Customer("Jack", 24, 1234, None)
# # Customer Jane
# cus2 = Customer("Jane", 25, 5678, None)

# # Now
# cus1 = Customer("Jack", 24, 1234, add1)
# cus2 = Customer("Jane", 25, 5678, add2)

# Accessing Aggregated Attributes

"""
Since the Customer class has aggregated the Address class,
the address object is available in all the methods of the Customer class, just like regular attributes.
"""

class Customer():
    def __init__(self, name, age, phone_no, address):
        self.__name = name
        self.__age = age
        self.__phone_no = phone_no
        self.__address = address
    
    def view_details(self):
        print(self.__name, self.__age, self.__phone_no)
        print(self.__address.door_no, self.__address.street, self.__address.pincode)

    def update_details(self, add):
        self.__address = add
    
class Address():
    def __init__(self, door_no, street, pincode):
        self.door_no = door_no
        self.street = street
        self.pincode = pincode
    
    def update_address(self):
        pass

add1 = Address(123, "5th Lane", 56001)
add2 = Address(567, "6th Lane", 82006)
cus1 = Customer('Jack', 24, 1234, add1)

cus1.view_details()
cus1.update_details(add2)
cus1.view_details()

## Aggregation and Encapsulation

"""
Private variables cannot be accessed outside the class. This is true even in aggregation.
The owning class cannot access the private attributes of the aggregated class directly.
"""
# class Customer:
#     def __init__(self, name, age, phone_no, address):
#         self.name = name
#         self.age = age
#         self.phone_no = phone_no
#         self.address = address

#     def view_details(self):
#         print (self.name, self.age, self.phone_no)    
#         print (self.address.__door_no, self.address.__street, self.address.__pincode) #This line here is trying to access the private variables of Address class which leads to an error.

# class Address:
#     def __init__(self, door_no, street, pincode):
#         self.__door_no = door_no
#         self.__street = street
#         self.__pincode = pincode

#     def update_address(self):
#         pass

# add1=Address(123, "5th Lane", 56001)
# cus1=Customer("Jack", 24, 1234, add1)

# cus1.view_details()

## Aggregation and Getter/Setter Methods
"""
Once we have appropriate accessor and mutator methods
we can start accessing the private variables of the aggregated class using those methods.
"""

class Customer():
    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.address = address
    
    def view_details(self):
        print(self.name, self.age, self.phone_no)
        print(self.address.get_door_no(), self.address.get_street(), self.address.get_pincode())

class Address():
    def __init__(self, door_no, street, pincode):
        self.__door_no = door_no
        self.__street = street
        self.__pincode = pincode
    
    def get_door_no(self):
        return self.__door_no
    def get_street(self):
        return self.__street
    def get_pincode(self):
        return self.__pincode
    
    def set_door_no(self, value):
        self.__door_no = value
    def set_street(self, value):
        self.__street = value
    def set_pincode(self, value):
        self.__pincode = value
    
    def update_address(self):
        pass

add1 = Address(123, "5th Lane", 56001)
cus1 = Customer("Jack", 24, 1234, add1)

cus1.view_details()

## Dependency via Formal Parameter - Try out
"""
Sometimes a class may depend on another class for sone of its use. This is not a strict
relationship and hence will not appear in the class diagram.

For example, in the below code, the Customer class depends on a payment object for purchasing. Here payment is a local variable and not a attribute.
"""

class Customer():
    def __init__(self, name, age, phone_no):
        self.name = name 
        self.age = age
        self.phone_no = phone_no
    
    def purchase(self, payment):
        if payment.type == "card":
            print("Paying by card")
        elif payment.type == "e-wallet":
            print("Paying by e-wallet")
        else:
            print("Paying by cash")

class Payment():
    def __init__(self, type):
        self.type = type

payment1 = Payment("card")
c = Customer("Jack", 23, 1234)

c.purchase(payment1)

## Dependency via Local Variable

"""
Apart from an object being passed as a parameter to the method, 
we can also create an object locally inside a method. 
This again is a weaker dependency which does not reflect in the class diagram.

Also, sometimes we may access the static values of another class directly in our method. This again is a weaker relationship.
"""
#Object creation
class Customer:
    def __init__(self, name,cust_type,bill):
        self.name = name
        self.bill = bill
        self.cust_type=cust_type
    def calulate_bill(self):
        tax1=Tax(self.cust_type)
        final_bill=self.bill*tax1.tax_details(self.cust_type)
        return final_bill
class Tax:
    def __init__(self,cust_type):
        self.cust_type=cust_type
    def tax_details(self,cust_type):
        if(cust_type=="Student"):
            return 5
        else:
            return 10
cust1=Customer("Maddy","Student",100)
print(cust1.calulate_bill())

#Usage of static
class CustomerCare:
    helpline=111000
class Customer:
    def call_support(self):
        print("Calling ",CustomerCare.helpline)
Customer().call_support()


