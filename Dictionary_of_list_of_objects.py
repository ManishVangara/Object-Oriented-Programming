"""
Problem Statement

We have a list of customer objects. Complete the code so that we have a dictionary of customer objects based on location.
"""

class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'), 
                    Customer(102, "Jane", "Japan"),
                    Customer(103, "Kumar", "India")]

dict_of_customers = {}

for cust in list_of_customers:
    if cust.location not in dict_of_customers:
        dict_of_customers[cust.location] = Customer(cust.cust_id, cust.cust_name, cust.location)

## Accessing
print(dict_of_customers["India"].cust_id)


## Working Code

class Customer:
    def __init__(self, cust_id, cust_name, location):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.location = location

list_of_customers = [Customer(101, 'Mark', 'US'),
                     Customer(102, 'Jane', 'Japan'),
                     Customer(103, 'Kumar', 'India')]

dict_of_customer = {}
for customer in list_of_customers:
    dict_of_customer[customer.location] = customer

print ("Customer name in India is "+dict_of_customer["India"].cust_name)

for key,value in dict_of_customer.items():
    print ("Location: "+key+", Name: "+value.cust_name+", Id: "+(str(value.cust_id)))

