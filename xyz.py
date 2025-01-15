# ekkigai,sakshi ,2000
# ekkigai,sakshi,10000
# Ekkigai,sakshi,2000


def menu():
    print("Contact Managment System")
    print("1.Load Contact")
    print("2.save Contact")
    print("3.Add contact")
    print("4.View all contact")
    print("5.Update contact")
    print("6.Delete Contact")
    print("7.Exit")

def load_contact(filename):
    try:
        with open(filename,'a')as file:
            contact1=int(input("Enter first number"))
            contact2=int(input("Enter second number"))
            contact3=int(input("Enter third number"))
            contact=f'{contact1}{contact2}{contact3}\n'
            file.write(contact)
            contact("contact added successfully")
    except Exception as e:
        print(f'An error occured: {e}')

# def save_contact(filename):
#     try:
#         with open(filename)

def main():
    filename="xyz.py"
    while True:
        menu()
        choice=(input("Enter your choice: "))
        if choice=="1":
            load_contact(filename)
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()

