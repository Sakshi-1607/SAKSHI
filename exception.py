# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Number can't be divisible by zero")

# result=10/0
# print(result)

# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Number can't be divisible by zero")
# else:
#     print("The result is:", result)
# finally:
#     print("It will print regardless of whether the issue is raised or not")


# def check_age(age):
#     if age<18:
#         raise ValueError("Age must be 18")
#     return "You are allowed to vote"
# try:
#     result= check_age(18)
#     print(result)
# except ValueError as ve:
#     print(ve)                             

# try:
#     num=int(input("Enter the number:"))
#     result=10/num
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Number can't be divisible by zero")
# else:
#     print(result)
# finally:
#     print("Done")

# class GasKhatamError(Exception):
#     pass
# class TeapowderKhatam(Exception):
#     pass
# class unexpectedGuestError(Exception):
#     pass
# def prepare_tea()
#     try:






