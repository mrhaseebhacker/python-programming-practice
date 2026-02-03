light = "pink"

if (light == "green"):
    print("go")
elif(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("Look")
else:
    print("light is broken")

    print("End code")
#grading system
marks = int(input("Enter your marks:"))
if(marks >= 90):
    print("Your grade is A")
elif(marks >= 80 and marks < 90):
    print("Your grade is B")
elif(marks >= 70 and marks < 80):
    print("Your grade is C")
else:
    print("Your grade is D")
#greatest of three number    
number1 = int(input("Enter first number:")) 
number2 = int(input("Enter second number:"))
number3 = int(input("Enter third number:"))

if (number1 > number2 and number1 > number3):
    print("First number is greater")
elif(number2 > number1 and number2 > number1):
    print("Second number is greater")
else:
    print("Third number is greater")    
#multiple of 7    
number = int(input("Enter number:"))
if(number%7==0):
    print("Number is multiple of Seven")
else:
    print("Number is not multiple of Seven")
