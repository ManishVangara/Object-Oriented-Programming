"""
Problem Statement
In the Athlete class given below, 

make all the attributes private and
add the necessary accessor and mutator methods
Represent Maria, the runner and make her run.

"""

class Athlete(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    
    def set_name(self,name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    
    def running(self):
        if self.__gender == "girl":
            print("150mtr running")
        else:
            print("200mtr running")

Runner = Athlete("Maria", "girl")
Runner.running()
Runner.set_name("Manish")
Runner.set_gender("")
Runner.running()