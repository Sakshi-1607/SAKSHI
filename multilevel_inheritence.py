# class NSTI:
#     def __init__(self,ins_name,Branch):
#         self.Ins_name=ins_name
#         self.Branch=Branch

# class Trade(NSTI):
#     def __init__(self, ins_name, Branch,Trade,s_name):
#         super().__init__(ins_name, Branch)
#         self.Trade=Trade
#         self.s_name=s_name

# class Student(Trade):
#     def __init__(self, ins_name, Branch, Trade,s_name):
#         super().__init__(ins_name, Branch, Trade,s_name)

#     def disp(self):
#         print(f'Institute Name: {self.Ins_name}')
#         print(f'Branch is {self.Branch}')
#         print(f'Trade: {self.Trade}')
#         print(f'Student name : {self.s_name}')

# x=Student("NSTI","Ramanthapur","AI","Sakshi")
# x.disp()

##############################################################################

class Vehicle:
    def __init__(self,company,model):
        self.company=company
        self.model=model

class Tata(Vehicle):
    def __init__(self, Company,Model,price):
        super().__init__(Company,Model)
        self.price=price

class India(Tata):
    def __init__(self, Company, Model, price):
        super().__init__(Company, Model, price)

    def disp(self):
        print(f'Company Name: {self.company}')
        print(f'Model: {self.model}')
        print(f'Price: {self.price}')

x=India("TATA","Naxon","9.80L")
x.disp()
        
 ####################################################################################

# Task - 1
# Build a program with the following structure:

# Class Animal has a method eat() and an attribute species.
# Class Mammal inherits from Animal and adds attributes like has_hair and methods like walk().
# Class Dog inherits from Mammal and adds specific attributes like breed and methods like bark().
# Write a program to create a Dog object and demonstrate all the inherited methods.    """


class Animal:
    def _init_(self,species):
        self.species=species

    def eat(self):
        print("This Animal eats food.")

class Mammal(Animal):
    def _init_(self, species,has_hair):
        super()._init_(species)
        self.has_hair=has_hair

    def walk(self):
        print("This Mammal walk.")

class Dog(Mammal):
    def _init_(self, species, has_hair,breed):
        super()._init_(species, has_hair)
        self.breed=breed

    def bark(self):
        print("The Dog barks : woof! woof !")

dog= Dog(species="American Labrador",has_hair="Yes",breed="Labrador Retriever")

print(f'species :{dog.species}')
print(f'has _hair : {dog.has_hair}')
print(f'Breed : {dog.breed}')

# Task-2 :
# Create a multilevel inheritance:

# Class Vehicle has attributes like brand and model.
# Class Car inherits from Vehicle and adds attributes like number_of_doors and fuel_type.
# Class ElectricCar inherits from Car and adds attributes like battery_capacity and range.
# Write methods to display the details of an ElectricCar.                           


class Vehicle:
    def _init_(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def _init_(self, brand, model,numbers_of_door,fuel_type):
        super()._init_(brand, model)
        self.number_of_door=numbers_of_door
        self.fuel_type=fuel_type

class ElectriCar(Car):
    def _init_(self, brand, model, numbers_of_door, fuel_type,battery_capacity,range):
        super()._init_(brand, model, numbers_of_door, fuel_type)
        self.battery_capacity=battery_capacity
        self.range=range

    def disp(self):
        print(f'Brand of Car: {self.brand}')
        print(f'Model of Car: {self.model}')
        print(f'Number of Doors In Car: {self.number_of_door}')
        print(f'Fuel Type: {self.fuel_type}')
        print(f'Battery Capacity: {self.battery_capacity}')
        print(f'Range: {self.range}')

x=ElectriCar("TATA","NANO","FIVE","PETROL","9volt","20km/pr litre")
x.disp()


# Task -3 :Design a library management system using multilevel inheritance:

# Class Library has attributes library_name and location.
# Class Book inherits from Library and includes attributes like book_name, author, and ISBN.
# Class Borrower inherits from Book and adds attributes like borrower_name and borrow_date.
# Write a program to manage borrowers and display their borrowed book details, including library information.      """


class LIBRARY:
    def __init__(self,library_name,location):
        self.library_name=library_name
        self.location=location

class Book(LIBRARY):
    def _init_(self, library_name, location,book_name,author,pub_year):
        super()._init_(library_name, location)
        self.book_name=book_name
        self.author=author
        self.pub_year=pub_year

class Borrower(Book):
    def _init_(self, library_name, location, book_name, author, pub_year,borrower_name,borrow_date):
        super()._init_(library_name, location, book_name, author, pub_year)
        self.borrower_name=borrower_name
        self.borrow_date=borrow_date
    
    def display_borrower_details(self):
        print(f'LIBRARY NAME : {self.library_name}')
        print(f'LOCATION : {self.location}')
        print(f'BOOK NAME : {self.book_name}')
        print(f'AUTHOR : {self.author}')
        print(f'ISBN : {self.pub_year}')
        print(f'BORROWER NAME : {self.borrower_name}')
        print(f'BORROW DATE : {self.borrow_date}')

borrower=Borrower(library_name="",location="BIHAR",book_name=" DO YOU LOVE ME",author="JOHNSON GALB",ISBN="9872733426",borrower_name="KUMAR ADITYA",borrow_date="31/12/2024")

borrower.display_borrower_details()  