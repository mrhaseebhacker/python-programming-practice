# solution one (using exponentiation)
num = int(input("Enter a number :"))
sr = num **(1/2)
print("Square of number is :", sr)

#solution two (using math module)
import math
num = int(input("Enter a number :"))
sr = math.sqrt(num)
print("Square of number is :", sr)