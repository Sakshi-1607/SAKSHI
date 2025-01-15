                  #DATE--18/12/24

# Task 1: Define a class Student with attributes name and roll_number. Create an object of this class and print its attributes.
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_info(self):
        print(f"Name: {self.name},Roll_number:{self.rollno}")

school= student("sakshi",1)
school.display_info()

# Task 2: Define a class Rectangle with attributes length and width. Add a method area to calculate the area of the rectangle. Create an object and call the method.

class rectangle:
    def __init__(self,length,width):
        self.length= length
        self.width=width
    def Area(self):
        x=self.length*self.width
        print("Area of rect: ",x)

math=rectangle(7,6)
math.Area()

#Task 3: Define a class Circle with a method circumference to calculate the circumference and another method area to calculate the area. Use π = 3.14.

class circle:
    def __init__(self,radius):
        self.radius= radius
    def circumference(self):
        x=2*3.13*self.radius
        print("circumference of circle: ",x)
    def Area(self):
        y=3.14*self.radius*self.radius
        print("Area of circle",y)

math=circle(6)
math.circumference()
math.Area()

# Task 4: Define a class Employee with a class attribute company_name and instance attributes name and salary. Print both class and instance attributes.

class Employee:
    def __init__(self,company_name,name,salary):
        self.company_name=company_name
        self.name=name
        self.salary=salary

branch=Employee("Edunet","sakshi",50000)
print(f'{branch.company_name},{branch.name},{branch.salary}')

#Task 5: Create a base class Animal with a method sound. Create a derived class Dog that overrides the sound method. Call the method from an object of Dog.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
dog = Dog()
dog.sound()

#Task 6: Create a class Book with attributes title and author. Add a method is_same_author that compares the authors of two book objects.


class book:
    Author_name="Sakshi singh"

    def __init__(self,title,author):
        self.title=title
        self.author= author

    def compare(self,sec_book):
        if self.author == sec_book.author:
            return True
        else:
            return False

Book1=book("python","sakshi singh")
Book2=book("coding","sakshi singh")
Book3=book("programming","saumya singh")


print(Book1.compare(Book2))
print(Book1.compare(Book3))



