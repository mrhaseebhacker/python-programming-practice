# number1 = int(input("Enter first:"))
# number2 = int(input("Enter second:"))

# if (number1 >= number2):
#     print("True")
# else:
#     print("False")
# print(number1>=number2)
# if (number1%2 ==0):
#     print("Numner is Even")
# else:
#     print("Number is Odd")
number = int(input("Enter number:"))
fact =1
for i in range(1, number+1 ):
    fact *=i
print(f"Factorial of {number} is {fact}")
