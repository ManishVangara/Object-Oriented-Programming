"""
What happens when we pass an object as a parameter to a function? 
In the below code, what will be the output?
"""

class Mobile():
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

def change_price(mobile_obj):
    mobile_obj.price = 3000

mob1 = Mobile(1000, "Apple")
change_price(mob1)
print(mob1.price)


## UNDERSTANDING PASS BY REFERENCE ##
"""
When we pass an object to a parameter, the parameter name becomes a reference variable.

Recollecting the balloon example, it is like creating one more ribbon to the same balloon. Thus there is one object with two reference variable, one the formal parameter and the actual parameter. Thus any change made through one reference variable will affect the other as well.


"""

class Mobile():
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    
    def change_price(mobile_obj):
        print("Id of object inside function", id(mobile_obj))
        mobile_obj.price = 3000

mob1 = Mobile(1000, "Apple")
print("Id of the object in driver code", id(mob1))

mob1.change_price()
print("Price of mob1", mob1.price)


## Pass by Reference Quiz

class Customer:
    def __init__(self, cust_id, age):
        self.cust_id = cust_id
        self.age = age

c1=Customer(100,20)

def change(c2):
    c2=Customer(100,21)

change(c1)
print(c1.age)

# We are creating a new customer object inside change() and hence the original customer object c1 is unaffected.

