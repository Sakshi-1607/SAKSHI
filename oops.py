# class ai:
#     institute="NSTI"

#     def __init__(self,name,age,address):
#         self.name= name
#         self.age= age
#         self.address= address

# students=ai("Sakshi",30,"BIHAR")

# print(students.name)
# print(students.age)
# print(students.address)
# print(f'{students.name},{students.age},{students.address}')


# class book:
#     Author_name="Sakshi singh"

#     def __init__(self,Author_name,book_name,pub_year,price):
#         self.Author_name=Author_name
#         self.book_name= book_name
#         self.pub_year= pub_year
#         self.price= price

# library1=book("sakshi singh","Ekkigai",2024,1000)
# library2=book("sakshi singh","Python",2000,500)
# library3=book("sakshi singh","computer",2024,300)
# library4=book("sakshi singh","programming",1999,500)
# library5=book("sakshi singh","coding",1998,450)


# print(f'{library1.Author_name},{library1.book_name},{library1.pub_year},{library1.price}')
# print(f'{library2.Author_name},{library2.book_name},{library2.pub_year},{library2.price}')
# print(f'{library3.Author_name},{library3.book_name},{library3.pub_year},{library3.price}')
# print(f'{library4.Author_name},{library4.book_name},{library4.pub_year},{library4.price}')
# print(f'{library5.Author_name},{library5.book_name},{library5.pub_year},{library5.price}')

# class car:
#     a="Vehicle"
#     b="car"

#     def xyz(self):
#         print("Hello :",self.a)
#         print("Hello :",self.b)

#     def abc(self):
#         print("All the vehicles")

# x=car()
# print(f"{x.a},{x.b}")
# print(x.a)
# print(x.b)
# x.xyz()
# x.abc()


# class calculation:
#     a=45
#     b=40

#     def Add(self):
#         x=self.a+self.b
#         print("Addition is:",x)
    
#     def sub(self):
#         y=self.a-self.b
#         print("Subtraction is:",y)

# math=calculation()
# math.Add()
# math.sub()

# class wallet:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def add_money(self,money):
#         if money>0:
#             self.balance +=money
#             print(f'Money added :{money} to {self.balance}')
#         else:
#             print("Enter a valid amount. ")

#     def spend(self,money):
#         if money > self.balance:
#             print("insufficient balance.")
#         else:
#             original_balance=self.balance
#             self.balance -= money
#             print(f'Spend Amount {money} from wallet {original_balance} remaining balance :{self.balance}')

#     def check(self):
#         print(f'{self.name} balance is {self.balance}')

# x=wallet("sakshi",100)
# y=wallet("saumya",500)

# x.add_money(50)
# y.add_money(100)
# x.spend(20)
# y.spend(30)
# x.check()
# y.check()


# class flipkart:
#     def __init__(self,name,item,balance):
#         self.name=name
#         self.item=item
#         self.balance=balance
    
#     def product_price(self,money,item):
#         if money <0:
#             print("Insufficient Balance.")
#         else:
#             original_balance=self.balance
#             self.balance-=money
#             print(f'purchase {item} with Rs {original_balance} and remaining balance: {self.balance}')

#     def info(self):
#         print(f'customer_name: {self.name} ,item name: {self.item}, item_price:  {self.balance}')

# x=flipkart("sakshi","copy",50)


# x.product_price(250,"copy")
# x.info()

# class Amazon:
#     def __init__(self):
#         self.card = []
#     def Adding_items(self,item_name,price):
#         self.card.append({'item':item_name,'price':price})

#     def remove_item(self,item_name):
#         self.card=[item for item in self.card if item['item']!=item_name]

#     def display_info(self):
#         if not self.card:
#             print("your card is empty.")
#         else:
#             print("shopping card contents:")
#             for item in self.card:
#                 print(f"product name: {item} price: {price} rupees")

#     def calculate_total(self):
#         total = sum()


# card=Amazon()
# card.add_item("Laptop", 1000, 1)
# card.add_item("Mouse", 25, 2)
# card.add_item("Keyboard", 50, 1)
# card.display_cart()
# card.remove_item("Mouse")
# card.display_cart()
# total_cost = card.calculate_total()
# print(f"Total cost: ${total_cost}")


# class Flipkart:
#     def __init__(self,name):
#         self.name=name
#         self.item=[]

#     def add_item(self,i_name,price):
#         self.item.append({'name':i_name,'price':price})
#         print(f'Added {i_name} to list with price {price}')

    # def remove(self,i_name):
    #     for item in self.item:
    #         if item['name']==i_name:
    #             self.item.remove(item)
    #             print(f'Removed {i_name}')
    #             return
    #     print(f'{i_name} not found')

#     def display(self):
#         if self.item:
#             print(f'Cart for {self.name}')
#             for item in self.item:
#                 print(f'{item["name"]} : {item["price"]}')
#         else:
#             print("cart is empty:")

# x=Flipkart("sakshi")
# x.add_item("Laptop", 50000)
# x.display()



class Flipkard:
    def __init__(self,name):
        self.name=name
        self.item=[]

    def add_item(self,item_name,price):
        self.item.append({'name':item_name,'price':price})
        print(f'Added {item_name} to list with price {price}')

    def display(self):
        if self.item:
            print(f'card for{self.name}')
            for item in self.item:
                print(f'{item["name"]} : {item["price"]}')
        else:
                print("card is empty:")

x=Flipkard("sakshi")
x.add_item("Laptop",50000)
x.display()





