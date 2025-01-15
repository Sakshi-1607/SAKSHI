class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.salary = 50000
    def display_info(self):
        print(f"name: {self.name}, Age: {self.age},Salary: {self.salary}")
    def calculate_bonus(self):
        return self.salary
    def get_salary(self):
        return self.salary
    def display_bonus(self):
        bonus = self.calculate_bonus()
        print(f"Bonus for {self.name}: {bonus}")
employee = Employee("sakshi",19)
print(employee.name)
employee.display_info()
print(employee.age)
try:
    print(employee.salary)
except ArithmeticError as e:
    print (e)

print(employee.get_salary())
employee.display_bonus()





