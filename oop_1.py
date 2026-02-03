# class Student:
#     # for those things which are common we make them class attributes 
#     college_name = "Punjab College"
#     name = "Haseeb"
#     def __init__(self,name,marks):
#         self.name = name #object attribute > class attributse
#         self.marks= marks

# s1 = Student("Haseeb :", 80)
# print(s1.name, s1.marks)

# s2 = Student("Yashfa :", 90)
# print(s2.name, s2.marks)
# print(s2.college_name)
# print(Student.college_name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     brand = "rollsroyce"
# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Student:
#     # for those things which are common we make them class attributes 
#     college_name = "Punjab College"

#     def __init__(self,name,marks):
#         self.name = name #object attribute > class attributse
#         self.marks= marks
        

#     def welcome(self):
#         print("Welcome student,",self.name)

#     def get_marks(self):
#         return self.marks    

# s1 = Student("Haseeb",80)   
# s1.welcome() 
# print(s1.get_marks())    

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def ave(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print(self.name,"Your Score is:", sum/3)

# s1= Student("Haseeb",[99,98,97])
# s1.ave()
# s1.name = "Ahmad"
# s1.ave()

# class Car:
#     def __init__(self):
#      self.acc = False
#      self.brk = False
#      self.clutch = False

#     def start(self):
#      self.acc = True
#      self.brk = True
#      self.clutch = True
#      print("Car Started")
        
# car1 = Car()
# car1.start()        


class Account:
  def __init__(self,bal,acc):
     self.account_no = acc
     self.balance = bal

  def debit(self,amount):
     self.balance -=amount
     print(amount, "Amount was debitd")
     print("Total balance :",self.get_balance())

  def credit(self,amount):
     self.balance +=amount
     print(amount, "Amount was credit")
     print("Total balance :",self.get_balance())  

  def get_balance(self): 
     return self.balance  

account1 = Account(10000,12345)
account1.credit(1000)
account1.debit(500)