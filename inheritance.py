class Earth:
    def India(self):
        print("Bharat mata ki jai")

class Bihar(Earth):
    def bihar(self):
        print("East or west Bihar is best")

state=Bihar()
state.bihar()
##########################################################
class NSTI:
    def Student(self):
        print("student of NSTI Ramanthapur")

class Trade:
    def AIPA(NSTI):
        print("Welcome to our AI Lab")

x=Trade()
x.AIPA()
##########################################################
class Math:
    def addition(self,a,b):
        return a+b
    def subtr(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b
    
class calculation(Math):
    def pie():
        print("3.14")
    
math=calculation()
print("Addition", math.addition(34,20))
print("Subtraction", math.subtr(34,20))
print("Multiplication", math.multi(34,20))
print("Division", math.division(100,20))
print("print the value of pie",calculation.pie())

##########################################################
class Library:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def disp(self):
        print(f"Title : {self.title}")
        print(f"Author :{self.author}")
        print(f"Price : {self.price}")
class Book(Library):
    def __init__(self,title,author,price,year):
        super().__init__(title,author,price)
        self.year=year

    def disp2(self):
        super().disp()
        print("year :",self.year)
x=Book("NSTI","ABC",200,2004)
x.disp()

#########################################################################
#########################################################################
























