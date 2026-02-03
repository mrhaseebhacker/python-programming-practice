# class A:
#     vara = "Welcome to class A"

# class B:
#     varb = "Welcome to class B"

# class C(A,B):
#     varc = "Welcome to class C"    

# c1 = C()
# print(c1.varc)
# print(c1.vara)
# print(c1.varb)


# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod    
#     def start():
#         print("Car Started")


#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class Toyota(Car):
#     def __init__(self,name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 =Toyota("diesel", "Electric")  
# print(car1.type) 
# print(car1.name)    

# class Person:
#     name = "Ahmad"

#     def changeName(self, name):
#         self.__class__.name = "Haseeb"

# p1 = Person()
# p1.changeName("Haseeb")
# print(p1.name)
# print(Person.name)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) /3) + "%"    
    @property
    def percentage(self):
       return str((self.phy + self.chem + self.math) /3) + "%"     
stu1 = Student(98,97,96)
# print(stu1.percentage)
stu1.phy = 70

print(stu1.percentage)