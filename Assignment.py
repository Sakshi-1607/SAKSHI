#ASSIGNMENT
#	1.PYTHON KEYWORDS AND IDENTIFIERS
#	Identify the invalid identifier from the following: my_var, _myVar, 2var, my-var.
#  2var is in valid
#	List 5 Python keywords that cannot be used as identifiers.
# print , true ,  , while , for , break

#    2.PYTHON PRINT FUNCTION
#	Write a program to print "Welcome to Python Programming!".
#print("welcome to python programming!")


#	Use the print() function to display:
#	Your name.
#	Your favorite number.
#print("Sakshi Singh Rajput")
#print("favourite numberis=7")

#    3.PYTHON VARIABLE
#	Assign the value 25 to a variable and print it.
#variable=25
#print(variable)

#	Swap two variables without using a temporary variable
# a = 50
# b = 60
# a, b = b, a
# print("a=",a, "b=", b)

#  	Assign three values to three variables in a single line.
# a, b, c = 1, 2, 3
# print("a=",a, "b=", b,"c=",c)

#    4. PYTHON DATA TYPES
#	Determine the data type of the following values:
#	10 , 10.5 , "Hello" , True
# first = 10
# second = 10.5
# third = "Hello"
# fourth = True
# print(type(first))
# print(type(second))
# print(type(third))
# print(type(fourth))

#    Check if a variable is of type string
# x ="SAKSHI"
# if type(x) == str:
#     print("x is a string")
# else:
#     print("x is not a string")

#    5. PYTHON NUMBER
#Add two integers.
# a=20
# b=34
# c=a+b
# print(c) 

# find remainder
# a=25
# b=4
# c=a%b
# print(c)

#square of a number using an operator
#num = 5
#square = num ** 2
#print("The square of", num,"is",square)

#    6. PYTHON STRINGS
#	 Create a string and print its length
# my_string ="Sakshi singh Rajput"
# length = len(my_string)
# print("The length of the string is:", length)

#	Write a program to slice a string: Extract "World" from "Hello World".
# my_string = "Hello World"
# sliced_string = my_string[6:]
# print("Extracted string:",sliced_string)

#	Convert the string "python programming" to uppercase
# my_string = "python programming"
# uppercase_string = my_string.upper()
# print(uppercase_string)
 
# 	Concatenate two strings: "Hello" and "Python".
# str1 = "Hello"
# str2 = "python"
# result = str1 +" "+ str2
# print(result)

#	Use an escape character to print He said, "Python is fun!".
#print("he said\"python is fun!\"")

#   7.PYTHON LISTS
#	Create a list with 5 elements and print the third element.
# my_list = [10, 20, 30, 40, 50]
# print(my_list[2])

#	Replace the second element in the list [1, 2, 3, 4, 5] with 10.
# my_list = [1, 2, 3, 4, 5]
# my_list[1]=10
# print(my_list)

#	Add a new item to the end of the list [10, 20, 30].
# my_list = [10, 20, 30]
# my_list.append(40)
# print(my_list)

#	Remove the element 20 from the list [10, 20, 30].
# my_list = [10, 20, 30]
# my_list.remove (20)
# print(my_list)

#	Sort the list [5, 1, 8, 3] in ascending order
# my_list = [5, 1, 8, 3]
# my_list.sort()
# print(my_list)

#    8. PYTHON OPERATORS
# Addition
# a = 10
# b = 5
# result = a + b
# print("Addition:, result")

# #subtration
# result = a-b
# print("subtraction:",result)

# #multiplication
# result = a * b
# print("Multiplication:",result)

# #Division
# result = a / b
# print("Division:, result")

# #Floor Division
# result = a // b
# print("Floor Division:", result)

# #modulus
# result = a % b
# print("Modulus:", result)

# #Exponentiation
# result = a ** b
# print("exponential:", result)

#  	Write a program to compare two numbers and print the larger one.
# num1 = (input("first number:"))
# num2 = (input("second number:"))
# if num1 > num2:
#     print(f"The larger number is:{num1}")
# elif num2 > num1:
#     print(f"The larger number is:{num2}")
# else:
#     print("Both number are equal.")

#    combine logical operators to check if a number is greater than 10 and less than 20 
# num =float(input("Enter a number: "))
# if num > 10 and num < 20:
#    print(f"The number {num} is greater than 10 and less than 20.")
# else:
#    print("The num ",num, "is NOT in the range (10, 20).")

#   9.PYTHON BOOLEANS
#   write a program that True if a number is even,and False otherwise.
# num = int(input("enter a number:"))
# is_even = num % 2 ==0
# print("The number ",num, "is even ",is_even)

#   use the bool()function to check the trust value of an empty list.
# empty_list = [2,5,7,9]
# result = bool(empty_list)
# print("The trust value of an empty list is:",result)

#   10.INPUT AND OUTPUT
#write a program that asks for the user's name and prints a greeting.
# name = input("Enter your name: ")
# print ("Hello", name, " welcome")

#    Take two number as input from the user and display their sum.
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# sum_result = num1 + num2
# print("sum of ",num1 , " and ",num2, " is : ",sum_result)

#would you like me to continue generating exercises up to 100? if so, should i include advanced topics, or focus on basic concepts?

#    11.PYTHON VARIABLES
#assign a float value to a variable and print it.
# num = 5.7
# print("The float value is:", num)

#    Assign the result of 10 + 20 to a variable and display it.
# num1 = 10
# num2 = 20
# result = ( num1 + num2 )
# print(result)

#create a program to demonstrate the use of both local and global variables.

#    12.PYTHON TYPE CONSERVATION
#    convert an integer to a float and print it.
# num = 10
# float_num = float(num)
# print("The float value is:" ,float_num)

#    convert a string "123" to an integer and add 10 to it.
# str_num = "123"
# int_num = int(str_num)
# result = int_num + 10
# print("The result after adding 10 is:", result)

#    write a program to check the type of input given by the user.

#    13.PYTHON STRINGS
#    find the index of first occurrence of the character"o" in "Hello world".
# text = "Hello world"
# index_of_o = text.index('o')
# print("The index of the first occurrence of'o' is:", index_of_o)

#    Replace "world" with "python" in "Hello world"
# my_word = "Hello world"
# new_word = my_word.replace("world","python")
# print(new_word)

#    reverse the string
# text = "INDIA"
# reversed_text = text[::-1]
# print("The reversed string is:", reversed_text)

#    count the number of vowel in a string.
# text = "sakshi Singh Rajput"
# vowels = "aeiouAEIOU"
# vowel_count = 0
# for char in text:
#     if char in vowels:
#         vowel_count += 1
# print("The number of vowel in the string is:", vowel_count)

#    check whether the string "Madam" is a palindrome.
# text = "madam"
# text_lower = text.lower()
# if text_lower == text_lower[::-1]:
#     print(madam is a palindrome.")
# else:
#     print(madam is not a polindrome.")

#   14.PYTHON LIST
#   create a list with element of differnt data types.
#my_list = [42, "NSTI", 4.5, True, None]

#   Write a program to find the sum of all numeric elements in a list.

#   Remove all occurrences of the number 5 from the list[5,10,15,5,20]
# input_list = [5, 10, 15, 5, 20]
# output_list = [x for x in input_list if x != 5]
# print("List after removing all occurrences of 5:", output_list)

#    create a nested list and access the innermost element.

#   write a program to merge two lists.
# list1 = [7, 5, 8, 3]
# list2 = [1, 9, 2, 5]
# merged_list = list1 + list2
# print("merged list:", merged_list)

#   15.PYTHON TUPLES
#   create a tuple with 4 elements and print the second element.
# my_tuple = (10, 20, 30, 40)
# element = (my_tuple)
# print("second element is:",my_tuple[1])

#   Convert the tuple (1, 2, 3, 4) into a list.
# my_tuple = (1, 2, 3, 4)
# my_list = list(my_tuple)
# print(my_list)

#   write a program to unpack a tuple into individual variables.
# my_tuple = (10, 20, 30, 40)
# a, b, c, d = my_tuple
# print("a =" ,a)
# print("a =" ,b)
# print("a =" ,c)
# print("a =" ,d)

#	Check if the element 10 is present in the tuple (5, 10, 15).
# my_tuple = (5, 10, 15)
# if 10 in my_tuple :
#     print("10 is present in the tuple.")
# else:
#     print("10 is not present in the tuple.")

#    16. PYTHON DICTIONARIES
#Create a dictionary with three key-value pairs and print it
# my_dict = {"name": "Sakshi", "Trade": "AI", "Add": "Hyd"}
# print("Dictionary:", my_dict)

#    Access the value associated with the key "name" in the dictionary {"name": "John", "age": 25}.
# my_dict = {"name": "John", "age": 25}
# name_value = my_dict["name"]
# print(name_value)

#    Add a new key-value pair to the dictionary
# my_dict = {"name": "John", "age": 25}
# my_dict["city"] = "New York"
# print(my_dict)

#   Remove a key-value pair from a dictionary
# my_dict = {"name": "John", "age": 25, "city": "New York"}
# del my_dict["age"]
# print(my_dict)

#   Check whether the key "age" exists in the dictionary.
# my_dict = {"name": "John", "age": 25, "city": "New York"}
# if "age" in my_dict:
#     print("The key 'age' exists in the dictionary.")
# else:
#     print("The key 'age' does not exist in the dictionary.")

#    17.STRING
#    Write a program to reverse a string entered by the user.
# my_input = input("Enter a string: ")
# reversed_string = my_input[::-1]
# print("Reversed string:", reversed_string)

#    Ask the user to input a sentence and count the number of vowels in it.
# sentence = input("Enter a sentence: ")
# vowel_count = 0
# vowels = "aeiouAEIOU"
# for char in sentence:
#     if char in vowels:
#         vowel_count += 1
# print("Number of vowels in the sentence:", vowel_count)

#	Take two strings as input and concatenate them.
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# result = string1 + string2
# print("The concatenated string is:", result)

#	Write a Python program to check if a string is a palindrome
# my_string = "MOM"
# if my_string == my_string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#	Ask the user for their full name and print it in uppercase.
# full_name = input("Enter your full name: ")
# upper_name = full_name.upper()
# print("Your full name in uppercase is:", upper_name)

#	Write a program to replace all spaces in a sentence with underscores.
# sentence = input("Enter a sentence: ")
# replaced_sentence = sentence.replace(" ", "_")
# print("Replaced sentence:", replaced_sentence) 

# 	Input a string and find the first occurrence of the letter 'a'.  
# my_string = input("Enter a string: ")
# first_a = my_string.find("a")
# print("The first occurrence of 'a' is at index:", first_a)   

# 	Write a program to split a sentence into words and print each word on a new line.

#	Take a string as input and remove all the numbers from it

# 	Write a Python script to find the longest word in a given sentence   
#sentence = input("Enter a sentence: ")
#words = sentence.split()
#longest_word = max(words, key=len)
#print("The longest word in the sentence is:", longest_word)                                                                                                                                                                                                   

#  18. LIST
#    Write a program to find the sum of all number in list provided by the uses.
# num1 = float(input("Enter first number"))
# num2 = float(input("Enter second number"))
# result = num1 + num2
# print("sum of num is:", result)

#  20. USER INPUT
#	Write a program to take the user's age as input and print if they are eligible to vote (age >= 18).
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#	Ask the user for a temperature in Celsius and convert it to Fahrenheit.
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)

#	Take a user's birth year as input and calculate their current age.
# birth_year = int(input("Enter your birth year: "))
# current_year = 2024
# age = current_year - birth_year
# print("Your age is:", age)

#	Ask the user to input three numbers and calculate their average.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# average = (num1 + num2 + num3) / 3
# print("The average of the three numbers is:", average)

