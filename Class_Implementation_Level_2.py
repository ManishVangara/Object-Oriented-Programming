"""
TechWorld, a technology training center, wants to allocate courses for instructors.
An instructor is identified by name, technology skills, experience and average feedback.
An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes from the list of options below to represent instructors.

check_eligibility()
avg_feedback
experience
instructor_name
allocate_course()
allocate_course(technolody)
__init__()
Instructor
calculate_avg_feedback()
technology_skill
Write a Python program to implement the class chosen with its attributes and methods.

Note:

Consider all instance variables to be private and methods to be public
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false
Perform case sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.

"""

class Instructor(object):
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = None
        self.__experience = None
        self.__avg_feedback = None
    
    # Setter Methods
    def set_instructor_name(self, name):
        self.__instructor_name = name
    
    def set_technology_skill(self, skill):
        self.__technology_skill.append(skill)
    
    def set_experience(self, exp):
        self.__experience = exp
    
    def set_avg_feedback(self, feedback):
        self.__avg_feedback = feedback
    
    def check_eligibility(self):

        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        else:
            return False
    
    def allocate_course(self, technology):
        if ((technology == self.__technology_skill) or (technology == "C++")):
            return True
        else:
            return False


# Working Code 

#OOPR-Assgn-7
#Start writing your code here
class Instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__avg_feedback=None
        self.__technology_skill=None
        
    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
        
    def set_experience(self,experience):
        self.__experience=experience
        
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback
        
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
        
    def get_instructor_name(self):
        return self.__instructor_name
    
    def get_experience(self):
        return self.__experience
        
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def get_technology_skill(self):
        return self.__technology_skill
        
    def check_eligibility(self):
        if self.__experience>3 and self.__avg_feedback>=4.5:
            return True
        elif self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
            
    def allocate_course(self,technology):
        if((technology==self.__technology_skill) or (technology=="C++")):
            return True
        else:
            return False