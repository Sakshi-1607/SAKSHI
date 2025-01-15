# class A:
#     def abc(self):
#         print("This is A")

# class B(A):
#     def xyz(self):
#         print("This is b.")

# class C(A):
#     def www(self):
#         print("This is c.")

# class D(A):
#     def qwe(self):
#         print("This is D.")

# class E(B,C,D):
#     pass

# x=E()
# x.qwe()
# x.abc()
# x.xyz()

####################################################################################

# class NSTI:
#     def __init__(self,lunch):
#         self.lunch=lunch

# class Lab:
#     def __init__(self,lab):
#         self.lab=lab

# class AI(NSTI,Lab):
#     def __init__(self,lunch,lab,computer):
#         NSTI.__init__(self,lunch)
#         Lab.__init__(self,lab)
#         self.computer=computer

#     def disp(self):
#         print(f'Lunch: {self.lunch},lab: {self.lab},Computer: {self.computer}')

# x=AI("Roti sabji"," ADIT Lab" ," HP")
# x.disp()
    
######################################################################################

#Question 1: Create a Specialist class that inherits from two parent classes, Doctor and Surgeon. 
#The Doctor class should have a method diagnose that prints "Diagnosing the patient",
#and the Surgeon class should have a method operate that prints "Performing surgery".
#The Specialist class should have a constructor that initializes the specialist's name and specialty, 
#and a method display_info that prints the name and specialty.

# class Doctor:
#     def Diagnose(self):
#         print("Diagnosing the patient")

# class Surgeon:
#     def operate(self):
#         print("Performing surgery")

# class Specialist(Doctor,Surgeon):
#     def __init__(self, name,specialty):
#         self.name = name
#         self.specialty = specialty

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Speciality: {self.specialty}")

# specialist = Specialist("Dr.Abhishek","surgeon")
# specialist.display_info()

#Question 2: Create an OnlineCourse class that inherits from two parent classes, CourseContent and InteractiveTools. 
# The CourseContent class should have a method provide_materials that prints "Providing course materials", 
# and the InteractiveTools class should have a method facilitate_interaction that prints "Facilitating student interaction with tools". 
# The OnlineCourse class should have a constructor that initializes the course name and a method display_info that prints the course name. 
# Additionally, write a method start_course that prints "Starting the course".

# class Course_Content:
#     def Provide_materials(self):
#         print("Providing Course Materials")

# class interactivetool:
#     def facilitate_ineraction(self):
#         print("Facilitating student interaction with tools")

# class OnlineCourse(Course_Content,interactivetool):
#     def __init__(self,course_name):
#         self.course_name=course_name
#     def display_info(self):
#         print(f"Course Name : {self.course_name}")
#     def start_course(self):
#         print("Starting the Course")

# course=OnlineCourse("AI")   
# course.display_info()  
# course.Provide_materials()
# course.facilitate_ineraction()   

#Question 3: Create a Drone class that inherits from two parent classes, FlyingMechanism and Camera. 
# The FlyingMechanism class should have a method fly that prints "Drone is flying", 
# and the Camera class should have a method take_photo that prints "Taking a photo". 
# The Drone class should have a constructor that initializes the drone's model and a method display_info that prints the model. 
# Additionally, write a method perform_actions that calls the methods from both parent classes.

class FlyingMechanism:
    def fly(self):
        print("Drone is Flying")

class camera:
    def Take_photo(self):
        print("Taking a photo")

class Drone(FlyingMechanism,camera):
    def __init__(self,dronemodel):
        self.drone_model=dronemodel
    def display_info(self):
        print(f"Drone Model: {self.drone_model}")
    def perform_action(self):
        self.fly(),self.Take_photo()

x=Drone("DJI Mini4")
x.display_info()   
x.perform_action()
    
        