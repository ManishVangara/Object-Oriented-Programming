class Charger(object):
    def __init__(self, input_cable, output_cable, color=None):
        self.input_cable = input_cable
        self.output_cable = output_cable
        self.color = color
        self.price = 0
    
    def __str__(self):
        return "Input: " + str(self.input_cable) + "\nOutput: " + str(self.output_cable) + "\nColor: " + str(self.color)
    # Getters
    def get_input_cable(self):
        return self.input_cable
    def get_output_cable(self):
        return self.output_cable
    def get_color(self):
        return self.color
    def get_price(self):
        return self.price
    # Setters
    def set_input_cable(self, input_cable):
        self.input_cable = input_cable
    def set_output_cable(self, output_cable):
        self.output_cable = output_cable
    def set_color(self, color):
        self.color = color
    def set_price(self, price):
        self.price = price
    
    # Behaviours (Methods)
    def sale(self,discount=0):
        sale_price = self.price - self.price * discount/100
        return sale_price
    
    def get_all_values(self):
        values_list = [self.get_input_cable(), self.get_output_cable(), self.get_color(), self.get_price()]
        return values_list

    # Output: Find out why?
    # [<bound method Charger.get_input_cable of <__main__.Charger object at 0x1030b4e10>>, <bound method Charger.get_output_cable of <__main__.Charger object at 0x1030b4e10>>, <bound method Charger.get_color of <__main__.Charger object at 0x1030b4e10>>, 600]

C1 = Charger("C type", "B type", "Black")
C2 = Charger("USB", "C type", "White")
C1.set_price(600)
C2.set_price(1300)

print(C1.get_price())
print(C2.get_price())
print(C1.sale(50))
print(C2.sale(10))
print(C2.sale())
print(C1.get_all_values())
print(C2.get_all_values())






        