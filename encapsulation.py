# class AI:
#     def __init__(self):
#         self.name="Sakshi"

#     def disp(self):
#         print(self.name)

# x=AI()
# x.disp()
# print(x.name)

# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def disp(self):
#         print(self._trade)

# x=CTS()
# x.disp()
# print(x._trade)

# class Trainer:
#     def __init__(self):
#         self._salary="100"

#     def disp(self):
#         print(self._salary)

#         return self._salary
# x=Trainer()
# print(x.disp())


#Write a Python class with a public attribute name and a public method greet() that prints "Hello, [name]". Access both the attribute and method from outside the class.
# class python:
#     def __init__(self):
#         self.name="Hello,Sakshi"

#     def disp(self):
#         print(self.name)

# x=python()
# x.disp()

#Create a class with a protected attribute _age and a method _show_age() that prints the value of _age. Access these members directly from an object and observe the output.
# class protection:
#     def __init__(self):
#         self._age=19
#     def _show_age(self):
#         print(self._age)
# x=protection()
# x._show_age()
# x.self.age


#Create a class with a private method __secret(). Add a public method to call the private method, and demonstrate that the private method cannot be called directly from outside the class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Create a class with a private method __secret(). Add a public method to call the private method, and demonstrate that the private method cannot be called directly from outside the class.
# class private:
#     def __init__(self):
#         self.__name="sakshi"
#     def secret(self):
#         print(self.__name) 

# x=private()
# x.secret()
# x.__name()

############################################
# class Hospital:
#     def __init__(self):
#         self.__patients=[]

#     def add(self,patient):
#         self.__patients.append(patient)

#     def remove(self,patient):
#         if patient in self.__patients:
#             self.__patients.remove(patient)
#             print(f'patient{patient}removed from list')
#         else:
#             print(f'{patient} not found.')

#     def disp(self):
#         for patient in self.__patients:
#             print(patient)

# x=Hospital()

# x.add ("Vamsi")
# x.add ("aadil")
# x.add ("Deepak")
# x.remove("Deepak")
# x.disp()

# class AIPA:
#     def __init__(self):
#         self.__students=[]

#     def add(self,student):
#         self.__students.append(student)
#         print(f'{student} added in list')

#     def remove(self,student):
#         if student in self.__students:
#             self.__students.remove(student)
#             print(f'{student} remove from list')
#         else:
#             print("student not found")

#     def disp(self):
#         for student in self.__students:
#             print(student)
# x= AIPA()
# x.add ("sakshi")
# x.add ("ankit")
# x.add ("deepak")
# x.add ("Aditya")
# x.add ("vamsi")

# x.remove("vamsi")

# x.disp()

##############################################################################
                                    #    LAB--52

# class BankAccount:
#     def __init__(self, account_number, holder_name, initial_balance=0):
#         self.__account_number = account_number
#         self.__holder_name = holder_name
#         self.__balance = initial_balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance is {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.__balance}.")
#         else:
#             print("Insufficient funds or invalid amount.")

#     def get_balance(self):
#         return self.__balance
    
#     def __str__(self):
#         return(f"Account Number :{self.__account_number}\n"
#         f"Holder Name: {self.__holder_name}\n"
#         f"Balance:{self.__balance}")

# account = BankAccount("12345678","sakshi singh",1700)
# print(account)
# account.deposit(500)
# account.withdraw(200)

# print(f"Final balance: {account.get_balance()}")






# class Movie:
#     def __init__(self,id,title,price):
#         self.id=id
#         self.__title=title
#         self.__price=price

#     def s_title(self,title):
#         self.__title=title

#     def t_price(self,price):
#         if price>0:
#             self.__price=price
#         else:
#             print("Enter Price more than 0.")

#     def g_title(self):
#         return self.__title
    
#     def g_ticket(self):
#         return self.__price
    
#     def disp(self):
#         print(f'ID :{self.id}')
#         print(f'Name : {self.__title}')
#         print(f'Price :{self.__price}')

# def movie():
#         id=input("Enter id:")
#         title=input("Enter Movie Name:")
#         while True:
#             price =int(input("Enter the Price:"))
#             if 0<=999:
#                 break
#             else:
#                 print("print must more than rs.0")

#         return Movie(id,title,price)
# x=movie()   
# x.disp()
            

# Task 1 : Create a Book class to manage book information in a library. The class should have private attributes for the book title, author, and price. 
# Implement getter and setter methods for each attribute and a function to create a Book instance with user input.
class Book:
    def __init__(self,title,author,price):
        self.__title=title
        self.__author=author
        self.__price=price

    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_price(self, price):
        self.__price = price


def library():
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        price = float(input("Enter the book price: "))
        return Book(title, author, price)

x= library() 
print(f"Title:{x.get_title()}")
print(f"Author:{x.get_author()}")
print(f"Price:{x.get_price()}")

# Create an Employee class to manage employee information. The class should have private attributes for the employee name, position, and salary.
#  Implement getter and setter methods for each attribute and a function to create an Employee instance with user input.

class Employee():
    def __init__(self,Name,Position,Salary):
        self._Name=Name
        self.__Position=Position
        self.__Salary=Salary

    def get_Name(self):
            return self._Name 
    def set_Name(self,Name):
            self._Name = Name
    def get_Position(self):
            return self._Position
    def set_Position(self,Position):
            self._Position = Position
    def get_Salary(self):
            return self._Salary
    def set_Salary(self,Salary):
            self._Salary = Salary
        
def company():
        Name= input("Enter the Employee name: ")
        Position = input("Enter the position: ")
        Salary = float(input("Enter the Salary: "))
        return Employee(Name,Position,Salary)

x=company()
print(f"Employee Name: {x.get_Name()}")
print(f"Position: {x.get_Position()}")
print(f"Salary: {x.get_Salary()}")













