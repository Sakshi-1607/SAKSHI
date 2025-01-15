# Task-1 Write a Python function to add a new book to the library. The book details should include title, author, and publication year. The details should be stored in a file called books.txt.
# Task -2 Write a function to search for a book by title in the books.txt file.
# Task-3 Write a function to display all books in the library from the books.txt file.
# Task-4  Write a function to delete a book from the books.txt file by its title.
# Task-5 Implement a system where users can borrow a book. Write a function that marks a book as borrowed in the books.txt file. Create a new file borrowed_books.txt to track borrowed books.
# Task-6 Write a function that marks a book as returned, updating both books.txt and borrowed_books.txt files.
# Task-7 Write a main program loop to manage the library system, allowing users to choose actions from a menu.

import os
def menu():
    print("1. Add new book")
    print("2. search book")
    print("3. view book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return book")
    print("7. Exit")

def add_new_book(filename):
    try:
        with open(filename, 'a') as file:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            pub_year=input("Enter the pub_year of the book: ")
            book=f'{title},{author},{pub_year}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error occurred: {e}')        

def search_book(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                search=input("Enter the book name: ") 
                with open(filename,"r") as file:
                    books=file.readlines()  
                    found=False
                    for book in books:
                        title,author,pub_year=book.strip().split(",")
                        if title==search:
                            print("found book below")
                            print(f"title-{title}")
                            print(f"Author-{author}")
                            print(f"Pub_year-{pub_year}")
                            found=True
                            break
                    if not found:
                        print("Book not found")    
        else:
            print("Inventory not found")    
    except Exception as e:
        print(f"An Error occurred: {e}")

def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open (filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        title,author,pub_year=book.strip().split(",")
                        print(f'Title: {title},Author: {author},Pub_year: {pub_year}')
                else:
                    print("Inventory is empty")
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
                        title,author,pub_year=book.strip().split(",")
                        if title==title1:
                            print(f"Delete-{title},{author},{pub_year}")
                            found==True
                        else:
                            file.write(book)
            if not found:
                print("Book not found")
            else:
                print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")

def borrow_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the book name: ")
            with open(filename,"r") as file:
                books=file.readlines()
            with open(filename,"w") as file:
                found=False
                for book in books:
                        title,author,pub_year=book.strip().split(",")
                        if title==title1:
                            print(f"Borrow-{title},{author},{pub_year}")
                            with open("Borrowed_book.txt","a")as borrowed_file:
                                borrowed_file.write(f"{title},{author},{pub_year}\n")
                            found==True
                        else:
                            file.write(book)
            if not found:
                print("Book borrow")
            else:
                print("Invelantory book not found")
    except Exception as e:
        print(f"An Error occurred: {e}")

def return_book(filename):
    try:
        borrowed_filename="Borrowed_book.txt"
        if os.path.exists(filename) and os.path.exists(borrowed_filename):
            title1=input("Enter the book name: ")
            with open(borrowed_filename,"r") as borrowed_file:
                borrowed_books=borrowed_file.readlines()
            with open(filename,"r") as borrowed_file:
                found=False
                with open(borrowed_filename,"w")as borrowed_file:
                    for book in borrowed_books:
                     title,author,pub_year=book.strip().split(",")
                    if title==title1:
                        print(f"Return-{title},{author},{pub_year}")
                        with open(filename,"a")as file_append:
                            file_append.write(f"{title},{author},{pub_year}")
                        found==True
                    else:
                        borrowed_file.write(book)
        if not found:
            print("Book Return")
        else:
            print("Inventory book not found")
    except Exception as e:
        print(f"An Error occured; {e}")     

def main():
    filename="books.txt"
    while True:
        menu()
        choice=(input("Enter your choice: "))
        if choice=="1":
            add_new_book(filename)
        elif choice=="2":
            search_book(filename)
        elif choice=="3":
            view_inventory(filename)
        elif choice=="4":
            delete_book(filename)
        elif choice=="5":
            borrow_book(filename)
        elif choice=="6":
            return_book(filename)
            print("code execute")
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()
  

