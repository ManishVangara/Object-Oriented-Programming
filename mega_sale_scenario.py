"""
Problem Statement:

Let us assume that in our online shopping app, we want to provide a limited 50% flat off on all mobile phones.
How can we write our code so that all mobile objects get a 50% off? One solution is to create a discount attribute and hard code the value as 50% as shown below:
"""

## Method 1 - Hard code the value into discount attribute
class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.discount = 50
    
    def purchase(self):
        total = self.price - self.price * self.discount/100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)

mob1 = Mobile(20000, "Apple")
mob2 = Mobile(30000, "Apple")
mob3 = Mobile(5000,"Samsung")

mob1.purchase()
mob2.purchase()
mob3.purchase()

# Need for static variables
# Method 2 

class Mobile():
    def __init__(self, price, brand):
        self.brand = brand
        self.price = price 
        self.discount = 0
    
    def purchase(self):
        total = self.price - self.price * self.discount/100
        print(self.brand, "mobile with price ", self.price, "is available after discount at ", total)
    
def enable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount = 50
    
def disable_discount(list_of_mobiles):
    for mobile in list_of_mobiles:
        mobile.discount = 0

mob1 = Mobile(130000, "Apple")
mob2 = Mobile(89900, "Apple")
mob3 = Mobile(72999, "Samsung")
mob4 = Mobile(60000, "OnePlus")
mob5 = Mobile(29999, "Nothing")

list_of_mobiles = [mob1, mob2, mob3, mob4, mob5]

mob1.purchase()

enable_discount(list_of_mobiles)

mob2.purchase()
mob3.purchase()

disable_discount(list_of_mobiles)

mob5.purchase()

"""
The challenge with the above code is all the objects have the discount attribute. However if we have to change the value, we have to do it one by one.
What we need is a way to make an attribute that is shared across objects but not owned by each object.
"""

## Static variables
## The variables which are created at the class level are called Static Variables.

class Mobile():
    discount = 0
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    def purchase(self):
        total = self.price - self.price * Mobile.discount/100 #Accessing Static Variable - discount
        print(self.brand, "mobile with price ", self.price, "is available after discount at ", total)

# Updating Static Variables using Functions
def enable_discount():
    Mobile.discount = 50
def disable_discount():
    Mobile.discount = 0

mob1 =Mobile(2000,"Apple")
mob2 = Mobile(3000, "B")
mob3 = Mobile(4000, "C")

mob1.purchase()
enable_discount()
mob2.purchase()
mob3.purchase()
disable_discount()
mob4.purchase()
    
# Static variables and Encapsulation
"""
We can make our static variable as a private variable by adding a double underscore in 
front of it. We can also create getter and setter methods to access and modify it.
"""
class Mobile():
    __discount = 66

    def get_discount(self):
        return Mobile.__discount
    
    def set_discount(self, discount):
        Mobile.__discount = discount

m1 = Mobile()
print(m1.get_discount())

## Need for Static Methods
"""
In the below code, we are invoking the getter and setter methods using a reference variable.
But the self is not used inside the method at all.
"""

class Mobile():
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.__discount / 100
        print ("Total is ",total)

    def get_discount(self):
        return Mobile.__discount

    def set_discount(self,discount):
        Mobile.__discount = discount

mob1=Mobile(20000, "Apple")
mob2=Mobile(30000, "Apple")
mob3=Mobile(5000, "Samsung")

print(mob1.get_discount())

## Static Methods - Intro
"""
Since static variable is object independent, we need a way to access the getter setter methods without an object. This is possible by creating static methods. Static methods are those methods which can be accessed without an object. They are accessed using the class name.

There are two rules in creating such static methods:

1. The methods should not have self
2. @staticmethod must be written on top of it
"""

class Car():
    __discount = 25
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    @staticmethod
    def get_discount():
        return Car.__discount
    
    @staticmethod
    def set_discount(discount):
        Car.__discount = discount

car1 = Car("Nissan", 2300000, "White")
print(car1.get_discount())

"""
We can access static methods directly using the class name, even without creating objects.
"""
class Car():
    __discount = 25
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    @staticmethod
    def get_discount():
        return Car.__discount
    
    @staticmethod
    def set_discount(discount):
        Car.__discount = discount

print(Car.get_discount())

## Mega Sale Complete Solution

class Mobile():
    __discount = 50
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    
    def purchase(self):
        total = self.price - self.price * Mobile.__discount/100
        print(self.brand, "mobile with price", self.price, "is available after discount at", total)
    
    @staticmethod
    def get_discount():
        return Mobile.__discount
    
    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount
    
    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)
    
    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

mob1 = Mobile(130000, "Apple")
mob2 = Mobile(89900, "Apple")
mob3 = Mobile(72999, "Samsung")
mob4 = Mobile(60000, "OnePlus")
mob5 = Mobile(29999, "Nothing")

Mobile.disable_discount()
mob1.purchase()

Mobile.enable_discount()

mob2.purchase()
mob3.purchase()

Mobile.disable_discount()
mob4.purchase()
mob5.purchase()

## Static Counter
"""
Let us say we want to assign a unique number to each mobile object. 
The first object should be given a number 1000 and subsequent objects should have that value increased by 1.
We can accomplish this by using a combination of static and instance variables as shown below:
"""

class Mobile():
    counter = 1000
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
        self.mobile_id = Mobile.counter
        Mobile.counter += 1

mob1 = Mobile(130000, "Apple")
mob2 = Mobile(89900, "Apple")
mob3 = Mobile(72999, "Samsung")
mob4 = Mobile(60000, "OnePlus")
mob5 = Mobile(29999, "Nothing")

print("Mobile id for mob1 is",mob1.mobile_id)
print("Mobile id for mob5 is",mob5.mobile_id)

print("Current value of counter is", Mobile.counter)

"""
Static - Summary

1. Static attributes are created at class level.
2. Static attributes are accessed using ClassName.
3. Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
4. The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined.
"""

