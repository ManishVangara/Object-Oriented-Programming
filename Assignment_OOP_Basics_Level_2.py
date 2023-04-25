class Flower():
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
    
    def validate_flower(self):
        flower_names = ["Orchid", "Rose", "Jasmine"]
        if self.__flower_name.capitalize() in flower_names:
            return True
        else:
            return False

    def validate_stock(self, required_quantity):
        quantity = required_quantity
        if self.__stock_available >= quantity:
            return True
        else:
            return False

    def sell_flower(self,required_quantity):
        quantity = required_quantity
        if self.validate_flower() and self.validate_stock(quantity):
            self.__stock_available -= quantity
        
    def check_level(self):
        # order_level = {"orchid": 15, "rose": 25, "jasmine": 40}
        if self.__flower_name.lower() == 'orchid':
            if self.__stock_available < 15:
                return True
            else:
                return False
        elif self.__flower_name.lower() == "rose":
            if self.__stock_available < 25:
                return True
            else:
                return False
        elif self.__flower_name.lower() == "jasmine":
            if self.__stock_available < 40:
                return True
            else:
                return False
        else:
            return False
        
    
    # Setter methods
    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
    # Getter Methods
    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available
    
## Writing the program in lamen terms

"""
validate flowers():
if flower name is jasmine or rose or Orchid, return true else false

validate stock(quantity):
accept the quantity required.
if stock is available return True, Else false

sell_flower(quantity):


"""
## Slightly different approach. It run into errors. The code needs some work.

class Flower:
    flower = {'orchid':15, 'rose': 25, 'jasmine': 40}
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
    
    # Setter Methods
    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
    
    # Getter Methods
    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available
    
    def validate_flower(self):
        if (self.__flower_name).lower() in Flower.flower.keys():
            return True 
        else:
            False
    def validate_stock(self,required_amount):
        if self.__stock_available > required_amount:
            return True
        else:
            return False
    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity
    def check_level(self):
        if any(Flower.flower.keys()) == self.__flower_name.lower():
            if self.__stock_available < Flower.flower[self.__flower_name]:
                return True
            else:
                return False
    



