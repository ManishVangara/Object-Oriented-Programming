"""
Write a python program to find out if a given classroom is present in the left wing of a university building. Implement the class, Classroom given below.

Class Diagram:

    Classroom
+ classroom_list -> static
+ search_classroom(class_room) -> static

Method/Attribute description:

classroom_list: Static list which store the name of the class rooms in the left wing
search_classroom(class_room): Static method which search for the given class room in the classroom_list. If found, return "Found". Else, return -1
Note: Perform case insensitive string comparison 

For testing:

Invoke search_classroom(class_room) static method on class, Classroom by passing the name of the class room to be searched
Display appropriate message based on the return value of search_classroom(class_room)
"""

# class Classroom():
#     classroom_list = []
#     x = []
#     for i in classroom_list:
#         x.append(i.lower())
#     classroom_list = x
#     def search_classroom(class_room):
#         if class_room.lower() in (Classroom.classroom_list):
#             return "Found"
#         else:
#             return -1
        
# Classroom.classroom_list = [7, 1, 3, 4, 5, 9, "G10"]
# print(Classroom.search_classroom("g10"))

# # x = ['G015', 'G066', 'L123', 'L135', 'L143', 'L13']
# # classroom_list = []
# # for i in x:
# #     classroom_list.append(i.lower())
# #     print(classroom_list)

class Classroom():
    classroom_list = []

    @staticmethod
    def search_classroom(class_room):
        if class_room.upper() in Classroom.classroom_list:
            return "Found"
        else:
            return -1



