import time

class Bill():
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = None
    
    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total = 0
        if len(quantity_list) == len(price_list):
            for i,j in zip(quantity_list, price_list):
                total += i * j
            total_fees = total + consultation_fees
            self.__bill_amount = total_fees
        else:
            print("Enter list of equal lengths")
    
    # Getter Methods
    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount


start = time.time()

b1 = Bill(160799, "Manish")
b1.calculate_bill_amount(300, [2,4],[30,40,50])

print(b1.get_bill_amount())

print(b1.get_patient_name())

end = time.time()

print("The time of execution of above program is: ", (end-start) * 10**3, "ms")


## Code from ChatGPT to handle errors

import time

class Bill():
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = None
    
    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total = 0
        try:
            if len(quantity_list) == len(price_list):
                for i,j in zip(quantity_list, price_list):
                    total += i * j
                total_fees = total + consultation_fees
                self.__bill_amount = total_fees
            else:
                raise ValueError("Lengths of quantity_list and price_list should be equal")
        except (ValueError, TypeError) as e:
            print("Error: ", e)
    
    # Getter Methods
    def get_bill_id(self):
        return self.__bill_id
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_amount(self):
        return self.__bill_amount


start = time.time()

b1 = Bill(160799, "Manish")
b1.calculate_bill_amount(300, [2,4],[30,40,50])

print(b1.get_bill_amount())

print(b1.get_patient_name())

end = time.time()

