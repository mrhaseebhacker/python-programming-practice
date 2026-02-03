number = int(input("Enter non-negative number :"))
if number < 0 :
    print("The factorial for negative number is not defined ")
elif number == 0 or number == 1:
    print("The factorial for:", number, "is 1")
else:
    factorial = 1
    for i in range (1,number+1):
        factorial *=i
    print("The factorial for:",number,"is", factorial,)    