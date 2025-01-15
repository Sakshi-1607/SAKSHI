
# age = int(input("Enter your age: "))
# if age < 18:
#     print("minor age")
# elif age >=18 and age <60:            
#     print("major age")
# else :
#     print("senior age")

#         print student grade 
# marks = int(input("Enter your marks: "))
# if marks >= 90 :
#     print("Grade A PASS")
# elif marks >= 70 and marks < 90:
#     print("Grade B PASS")
# elif marks >= 50 and marks < 70:
#     print("Grade C PASS")
# else:
#     print(" FAIL")

# my_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for my_list in my_lists:
#     print(my_list)

#         print multiplication
# num = int(input("Enter the multiplication: "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

#        map use to change string into integer
# x = list(map(int(input("Enter the numbers: "))))
# total = 0
# for sum in x:
#     total += sum
#     print("sum is:",total)    

#         print even number
# n = int(input("Enter the number: "))
# for i in range(2,n+1,2): #start, stop, step
#     print(i)

#         print odd number
# n = int(input("Enter the number: "))
# for i in range(1,n+1,2): #start, stop, step
#     print(i)

# print factorial
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1): 
#     fact = fact * i
#     print(fact)

# def sakshi():
#     print("Hello AI class")

# sakshi()

# def abc(num1,num2):
#     sum=num1+num2
#     print("sum is:",sum)

# abc(10,20)

# def xyz(num):
#     result=num*num
#     return result 
# square=xyz(11)  
# print(square)  

#def add(a,b):
#    return a+b

#def sub(a,b):
#    return a-b

# X=10
# Y=6

#print("Adding numbers",add(X,Y))

# def keywrd(myname,college):
#     print(f"my name is {myname} and my college is {college}")

# keywrd(myname="sakshi",college="NSTI")

# def sum1(*numb):
#     return sum(numb)

# print(sum1(1,2,3,4,5,6,7,8,9))
# print(sum1(32,45,22))

# Positional Arguments
#def abc(num1,num2):
#     sum=num1+num2
#     print("sum is:",sum)


# Keyword Arguments
#def keywrd(myname,college):
#     print(f"my name is {myname} and my college is {college}")

# keywrd(myname="sakshi",college="NSTI")

# Default Arguments
# Variable-Length Arguments
# def sum1(*numb):
#     return sum(numb)

# print(sum1(1,2,3,4,5,6,7,8,9))
# print(sum1(32,45,22)) 

#Local and Global variable
# x=10 #global variable
# def abc():
#     x=20 #local variable
#     print(x)
# abc()
# print(x)
#keyword only Function
# def xyz(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# xyz(name="sakshi",age=20,college="nsti",city="Bihar")

#import value
# from math import pi
# print(pi)

# import math as m
# print(m.pi)

#import squareroot of a numper
# import math
# print(math.sqrt(9))
# print(math.pi)
# print(math.factorial(5))
# print(math.sin(45))
# print(math.cos(90))


# import sys
# built=sys.builtin_module_names
# print(built)
# for module in built:
#     print(module)

# import cmath
# print(cmath.pi)
# print(cmath.sin(45))
# print(cmath.cos(90))

# import datetime
# now=datetime.datetime.now()
# print(now)
 
#print date time yeas(string time)
# import datetime
# now=datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# def add(a,b):
#    return a+b
