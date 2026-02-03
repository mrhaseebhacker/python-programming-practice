# class Employee:
#     def __init__(self, role, depart, salary):
#         self.role = role
#         self.depart = depart
#         self.salary = salary

#     def show_details(self):
#         print("Role =", self.role)
#         print("Depart =", self.depart)
#         print("Salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75000")        

# engr1= Engineer("Haseeb", 40)
# engr1.show_details()     

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price    
        
ord1 = Order("lays", 20)
ord2 = Order("tea", 15) 
print(ord1 > ord2)       

