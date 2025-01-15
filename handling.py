# file =open("sakshi.txt","r")
# content=file.read()
# print(content)


# with open("sakshi.txt","r") as file:
#     content=file.read()
#     print(content)

# with open("sakshi.txt","r") as file:
#     for line in file:
#         print(line)


# with open("sakshi.txt","r") as file:
#     file.readlines()
#     content=file.read()
#     print(content)


# with open("sakshi.txt","w") as file:
#     file.write("Hello , My name is saumya")

# with open ("sakshi.txt","a") as file:
#     file.write("\n This is my another line")

# with open("sakshi.txt","r") as file:
#     file.read(5)
#     file.read(8)
#     file.seek(5)
#     print(file.read())
#     print(file.tell())

# try:
#     with open("sakshi.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("code executed")

# import os
# if os.path.exists("sakshi.txt"):
#     os.remove("sakshi.txt")
#     print("File  is deleted")
# else:
#     print("File not found")


#write a program that reads content from one file and writes it to another file
# def copy_file(source_file, destination_file):
#     try:
#         # Open the source file in read mode
#         with open(source_file, 'r') as src:
#             content = src.read()
        
#         # Open the destination file in write mode
#         with open(destination_file, 'w') as dest:
#             dest.write(content)
        
#         print(f"Content successfully copied from '{source_file}' to '{destination_file}'.")
#     except FileNotFoundError:
#         print(f"Error: The file '{source_file}' does not exist.")
#     except IOError as e:
#         print(f"An IOError occurred: {e}")

# Example usage
# source = input("Enter the source file name: ")
# destination = input("Enter the destination file name: ")

# copy_file(source, destination)
import os
def menu():
    print("NSTI Book store")
    print("1. Add new book")
    print("2. View books")
    print("3. search for book")
    print("4. Delete Book")
    print("5. Exit")
def add_new_book(filename):
    try:
        with open(filename, 'a') as file:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            price=input("Enter the price of the book: ")
            book=f'{title},{author},{price}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error occurred: {e}')
    
def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open (filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        title,author,price=book.strip().split(",")
                        print(f'Title: {title},Author: {author},Price: {price}')
                else:
                    print("Inventory is empty")
        else:
            print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")
def search_book(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                search=input("Enter the book name: ") 
                with open(filename,"r") as file:
                    books=file.readlines()  
                    found=False
                    for book in books:
                        title,author,price=book.strip().split(",")
                        if title==search:
                            print("found book below")
                            print(f"title-{title}")
                            print(f"Author-{author}")
                            print(f"Price-{price}")
                            found=True
                            break
                    if not found:
                        print("Book not found")
        else:
            print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")

def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the book name: ")
            with open(filename,"r") as file:
                books=file.readlines()
            with open(filename,"w") as file:
                found=False
                for book in books:
                        title,author,price=book.strip().split(",")
                        if title==title1:
                            print(f"Delete-{title},{author},{price}")
                            found==True
                        else:
                            file.write(book)
            if not found:
                print("Book not found")
            else:
                print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")

def main():
    filename="xyz.py"
    while True:
        menu()
        choice=(input("Enter your choice: "))
        if choice=="1":
            add_new_book(filename)
        elif choice=="2":
            view_inventory(filename)
        elif choice=="3":
            search_book(filename)
            print("Existing the code")
        elif choice=="4":
            delete_book(filename)
            print("Existing the code")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
