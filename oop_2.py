# class Student:
#     def __init__(self, name):
#      self.name = name

# s1 = Student("Haseeb")
# print(s1.name)        
# del s1
# print(s1.name)

# class Account:
#    def __init__(self,acc_no,acc_pass):
#        self.acc_no = acc_no
#        self.__acc_pass = acc_pass

#    def reset_pass(self):
#        print(self.__acc_pass)    

# acc1 = Account("12345", "abcd") 
# print(acc1.acc_no)
# print(acc1.reset_pass())      

# inheritance 
# class Car:
#     def start(self):
#         print("Car Started")

#     def stop(self):
#         print("Car Stopped")

# class Toyota(Car):
#     def __init__(self,brand):
#         # self.name = name
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type
# car1 =Fortuner("diesel")  
# car1.start()                          


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def ShowNum(self):
        print(self.real, "i", self.imag, "j")

num1 = Complex(2, 3)
num1.ShowNum()       