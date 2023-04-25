class Mobile():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def __str__(self):
        return '<--->'

mob1 = Mobile("Apple", 10000)
mob2 = Mobile("Samsung", 9000)
mob3 = Mobile("Sony", 8000)
mob4 = Mobile("Motorola", 7000)
mob5 = Mobile("Xiaomi", 6000)

list_of_mobiles = [mob1, mob2, mob3, mob4, mob5]

for mobile in list_of_mobiles:
    print(mobile.brand ,mobile.price)


# # Example to interpret the action/working in the above code.
# x = [5, 2]
# y = [4, 3]
# z = [3, 4]
# a = [2, 5]

# list_of = [x, y, z, a]

# for i in list_of:
#     print(i[0], "--->>",i[1])