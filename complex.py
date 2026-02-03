class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def ShowNum(self):
        print(self.real, "i", "+",  self.imag, "j")


    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)     

num1 = Complex(2, 3)
num1.ShowNum() 
num2 = Complex(5, 6)
num2.ShowNum()

num3 = num1 + num2 
# num3 = num1.add(num2)
num3.ShowNum()

num3 = num1 - num2
num3.ShowNum()