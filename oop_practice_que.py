class Student:
    def __init__(self, name = "", roll_no=0, marks=0):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def set_data(self, name, roll_no, marks,):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_data(self):

        print(f"Name : {self.name}, Roll_no : {self.roll_no}, Marks : {self.marks}") 

s1 = Student()
s1.set_data("Haseeb",19,95)
s1.get_data()





       
        