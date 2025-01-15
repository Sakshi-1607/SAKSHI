# First we'll have to import module from the Abstract base class Library

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(Vehicle): #concreatclass
#     def start(self):
#         print("Hello BMW ")
#     def stop(self):
#         print("Good Bye")

# x= Bike()
# x.start()
# x.stop()


# from abc import ABC, abstractmethod
# class NSTI(ABC):
#     @abstractmethod
#     def Admission(self):
#         pass
    
#     @abstractmethod
#     def farewell(self):
#         pass

# class student(NSTI):
#     def Admission(self):
#         print("Sucessfully join NSTI")

#     def Farewell(self):
#         print("sucesfully complete course")

# Hyd=student()
# Hyd.Admission()
# Hyd.Farewell()

# from abc import ABC, abstractmethod
# class math(ABC):
#     @abstractmethod
#     def Area(self):
#         pass
#     @abstractmethod
#     def Perimeter(self):
#         pass

# class square(math):
#     def __init__(self,side):






###     .........BANKING SYSTEM.........
from abc import ABC, abstractmethod
class saving_account(ABC):

    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def creadit(self):
        pass
    @abstractmethod
    def check_balance(self):
        pass

class deposit(saving_account):
    def __init__(self,amount):
        if amount > 0:
            self.amount += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive.")

class creadit(saving_account):
    def __init__(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Creadited {amount}")
        else:
            print("Insufficient funds or invalid amount.")

class CheckingAccount(saving_account):
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
    

bank=deposit()
bank=creadit()



########################################################################################################################


#TASK-1:- Create an abstract class Shape with an abstract method area().
# Implement two subclasses, Circle and Rectangle, that inherit from Shape and calculate the area based on their respective formulas.
# Write a program to calculate and print the area of a circle with radius 5 and a rectangle with width 4 and height 6.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,Length, Breadth):
        self.Length = Length
        self.Breadth = Breadth

    def area(self):
        return self.Length * self.Breadth

circle = Circle(5)  
rectangle = Rectangle(4, 6)  

print(f"Area of the circle: {circle.area()}")
print(f"Area of the rectangle: {rectangle.area()}")

# Task 2 :-Create an abstract class Employee with the following abstract methods:
# calculate_salary(): Calculate the employee's salary.
# get_details(): Print details of the employee.
# Implement two subclasses, FullTimeEmployee and PartTimeEmployee, with their own salary calculation logic.
# Write a program to demonstrate these classes.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
    @abstractmethod
    def get_details(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def get_details(self):
        return (f"Full-Time Employee: {self.name}/nPosition: {self.position}\nSalary: {self.calculate_salary()}")

class PartTimeEmployee(Employee):
    def __init__(self, name, position, hourly_rate, hours_worked):
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_details(self):
        return(f"Part-Time Employee: {self.name}\nPosition: {self.position}\nSalary: {self.calculate_salary()}")

full_time_employee = FullTimeEmployee("Sakshi singh", "AI develpoer", 75000)
part_time_employee = PartTimeEmployee("Saumya singh", "Tutor", 2,4) 

# Create an abstract class Animal with abstract methods sound() and move().
# Implement subclasses Dog and Bird, where:
# Dog defines sound as "bark" and move as "walk."
# Bird defines sound as "chirp" and move as "fly."

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "bark"
    def move(self):
        return "Walk"
    
class Bird(Animal):
    def sound(self):
        return "chirp"
    def move(self):
        return "fly"

dog=Dog()
bird=Bird()
print(f"Dog sound: {dog.sound()}")
print(f"Dog movement: {dog.move()}")
print(f"Bird sound: {bird.sound()}")
print(f"Bird movement: {bird.move()}")

# Create an abstract class Appliance with methods turn_on() and turn_off().
# Implement a Fan and a Light class, where:
# Fan prints "Fan is turned on" and "Fan is turned off."
# Light prints "Light is turned on" and "Light is turned off."
# Write a program to turn on and turn off both a fan and a light

from abc import ABC , abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print( "Fan is turned on")
    def turn_off(self):
        print("Fan is turned off.")
    
class Light(Appliance):
    def turn_on(self):
        print( "Light is turned on")
    def turn_off(self):
        print( "Light is turned off.")

fan=Fan()
light=Light()       
fan.turn_on()
fan.turn_off()
light.turn_on()
light.turn_off()






