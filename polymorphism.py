

class A:
    def x(self):
        return "Hello"
    
class B:
    def x(self):
        return "Hyy"
    
def z(q):
    return q.x()

r=A()
t=B()

print(z(r))
print(z(t))

######################################################################################
#              using inheritance

class Maths:
    def area (self):
        pass
    def perimeter(self):
        pass
class Rectangle(Maths):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l + self.b)
    
class square(Maths):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a * self.a
    def perimeter(self):
        return 4*(self.a)
    
class circle(Maths):
    def __init__(self,pie,r):
        self.pie=pie
        self.r=r
    def area(self):
        return self.pie* self.r*self.r
    def circumference(self):
        return 2*self.pie*self.r

x=[Rectangle(5,6),square(4)]
y=[circle(3.14,4)]

for result in x:
    print(result.area())
for result in x:
    print(result.perimeter())
for result in y:
    print(result.circumference())

####################################################################################

# from abc import ABC,abstractmethod

class NSTI(ABC):
    @abstractmethod
    def xyz(self):
        pass

class AI(NSTI):
    def xyz(self):
        return "Artificial Intelligence"
    
class CHNM(NSTI):
    def xyz(self):
        return "Computer Hardworking , Networking and maintanance"
    
x=[AI(),CHNM()]
for result in x:
    print(result.xyz())

#############################################################################################################################

# Demonstrates calculating the area of different shapes using Abstract Class
# from abc import ABC,abstractmethod

class shapes(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    
class Square(ABC):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    
class circle(ABC):
    def __init__(self,pie,radius):
        self.pie=pie
        self.radius=radius

    def area(self):
        return self.pie*self.radius*self.radius
    
class triangle(ABC):
    def __init__(self,base,height):
        self.base=base
        self.height=height

   
x=[Rectangle(7,5),Square(5)]
y=[circle(3.14,5)]
z=[triangle(6,5)]
for result in x:
    print(result.area())

##################################################################################################################################

#Write a code for Abstract class where you are building a restaurant ordering system. 
#The menu includes main courses, beverages, and desserts. Each item has a different preparation time and pricing model.
from abc import ABC,abstractmethod

class resturant:
    @abstractmethod
    def food(self):
        pass
class main_courses:
    def __init__(self,name,time,price):
        self.name=name
        self.time=time
        self.price=price

    def food(self):
        return f"Main Course: {self.name}, Time: {self.time}, Price: {self.price}"

class beverages(ABC):
    def __init__(self,name,time,price):
            self.name=name
            self.time=time
            self.price=price

    def food(self):
        return f"Beverages: {self.name}, Time: {self.time}, Price: {self.price}"
    
class desserts(ABC):
    def __init__(self,name,time,price):
        self.name=name
        self.time=time
        self.price=price

    def food(self):
        return f"Deserts : {self.name}, Time: {self.time}, Price: {self.price}"
    
x=[main_courses("Paneer and Naan","20 min",250)]    
y=[beverages("Coffee","7 min",150)]
z=[desserts("Ice-cream","5 min",150)]
for result in x:
    print(result.food())

for result in y:
    print(result.food())

for result in z:
    print(result.food())