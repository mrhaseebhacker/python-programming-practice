number1 = int(input("Enter one number :"))
number2 = int(input("Enter two number :"))
number3 = int(input("Enter three number :"))

if number1 > number2 and number1 > number3:
    print("Number one is greater :", number1)
elif number2 > number1 and number2 > number3:
    print("Number two is greater :", number2)
else:
    print("Number three is greater :", number3)    
