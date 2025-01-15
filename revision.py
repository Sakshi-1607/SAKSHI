################################  IF ELSE  ############################################

#                            PRINT STUDENT GRADE
"""
marks = int(input("Enter your marks: "))
if marks >= 90 :
    print("Grade A PASS")
elif marks >= 70 and marks < 90:
    print("Grade B PASS")
elif marks >= 50 and marks < 70:
    print("Grade C PASS")
else:
    print(" FAIL")

#                           PRINT AGE CATOGERY
age = int(input("Enter your age: "))
if age < 18:
    print("minor age")
elif age >=18 and age <60:            
    print("major age")
else :
    print("senior age")

#                           VOTE ELIGIBILITY
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")

################################################################################################
#                          CLASS FUNCTION
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.salary = 50000
    def display_info(self):
        print(f"name: {self.name}, Age: {self.age},Salary: {self.salary}")
    def calculate_bonus(self):
        return self.salary
    def get_salary(self):
        return self.salary
    def display_bonus(self):
        bonus = self.calculate_bonus()
        print(f"Bonus for {self.name}: {bonus}")
employee = Employee("sakshi",19)
print(employee.name)
employee.display_info()
print(employee.age)
try:
    print(employee.salary)
except ArithmeticError as e:
    print (e)

print(employee.get_salary())
employee.display_bonus()

#                                          CAR CLASS
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} is now running.")

    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    def car_info(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Camry", 2022)
my_car.car_info()
my_car.start()
my_car.stop()"""

#                                  BANKING SYSTEM
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. Current balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. Current balance: {self.balance}")
#         else:
#             print("Insufficient funds!")

#     def check_balance(self):
#         print(f"Current balance: {self.balance}")

# account = BankAccount("SAKSHI SINGH", 500)
# account.deposit(200)
# account.withdraw(100)
# account.check_balance()



# class Student:
#     def _init_(self, name, roll_number, marks):
#         self.__name = name
#         self.__roll_number = roll_number
#         self.__marks = marks

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_roll_number(self):
#         return self.__roll_number

#     def set_roll_number(self, roll_number):
#         self.__roll_number = roll_number

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         self.__marks = marks

# def display_student_info(self):
#         print(f"Name: {self.__name}")
#         print(f"Roll Number: {self.__roll_number}")
#         print(f"Marks: {self.__marks}")

# student1=Student("sakshi singh", 101 , 85)
# print("Before updating:")
# student1.display_student_info()

# student1.set_marks(90)
# print("\nAfter updating:")
# print(f"Marks:{student1.get_marks()}")
# student1.display_student_info()



# class Student():
#     def __init__(self,Name,Rollnumber,Marks):
#         self.__Name=Name
#         self.__Rollnumber=Rollnumber
#         self.__Marks=Marks

#     def get_Name(self):
#             return self.__Name 
#     def set_Name(self,Name):
#             self.__Name = Name
#     def get_Rollnumber(self):
#             return self.__Rollnumber
#     def set_Rollnumber(self,Position):
#             self.__Rollnumber = Position
#     def get_Marks(self):
#             return self.__Marks
#     def set_Marks(self,Marks):
#             self.__Marks = Marks
        
# def display_info():
#         Name= input("Enter the Student name: ")
#         Rollnumber =int(input("Enter the Rollnumber: "))
#         Marks = float(input("Enter the Marks: "))
#         return Student(Name, Rollnumber, Marks)

# x=display_info()
# print(f"Student Name: {x.get_Name()}")
# print(f"Roll Number: {x.get_Rollnumber()}")
# print(f"Marks: {x.get_Marks()}")



# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.__name=name
#         self.__roll_number=roll_number
#         self.__marks=marks

#     def get_name(self):
#         return self.__name
#     def get_roll_number(self):
#         return self.__roll_number
#     def get_marks(self):
#         return self.__marks
#     def set_name(self, name):
#         self.__name = name
#     def set_roll_number(self, roll_number):
#         self.__roll_number = roll_number
#     def set_price(self, marks):
#         self.__marks = marks


# def NSTI():
#         Name = input("Enter the Name: ")
#         Roll_number = int(input("Enter the Roll Number: "))
#         Marks = int(input("Enter the Marks: "))
#         return Student(Name, Roll_number, Marks)

# x= NSTI() 
# print(f"Name:{x.get_name()}")
# print(f"Roll Number:{x.get_roll_number()}")
# print(f"Marks:{x.get_marks()}")

# The dot (.) matches any character except a newline.
# Here, a.b matches acb because the dot matches any character between a and b.
import re
pattern = r"a.b"
test_string = "acb"
match = re.search(pattern,test_string)
if match:
    print("Match found:",match.group())
else:
    print("No Match")


import re
pattern = r"^Hello"
test_string = "Hello World"
match = re.search(pattern,test_string)
if match:
    print("Match found:",match.group())
else:
    print("No Match")

import re
pattern = r"World$"
test_string = "Hello World"
match = re.search(pattern,test_string)
if match:
    print("Match found:",match.group())
else:
    print("No Match")

import re
pattern = r"ab*c"
test_string = "abc"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"ab+c"
test_string = "abbc"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"ab?c"
test_string = "abc"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"[aeiou]"
test_string = "hello"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"cat|dog"
test_string = "I have a cat."
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"(ab)+"
test_string = "ababab"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"a{0,4}"
test_string = "aaab"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r"\."
test_string = "Hello. World"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

import re
pattern = r'\bsakshi\b'
test_string= "my name is sakshi singh sakshi sakshi rajput"
match=re.findall(pattern,test_string)
# print (match)
if match:
    print("Match found:", match)
else:
    print("No match")

import re
pattern = r"^(a|b)\d{2,4}\.com$"
test_string = "b1234.com"
match = re.search(pattern, test_string)
if match:
    print("Match found:", match.group())
else:
    print("No match")