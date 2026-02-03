print("1: Addition\n2:Subtraction\n3:Multiplication\n4:Division")
choice = int (input("Enter 1, 2, 3 or 4: "))
if choice==1:
    print("Addition")
    first_number = int (input ("Enter first number : "))
    second_number = int (input ("Enter second number : "))
    result = (first_number) + (second_number)
    print("Result :" , result)
elif choice==2:
    print("Subtraction")
    first_number = int (input ("Enter first number : "))
    second_number = int (input ("Enter second number : "))
    result = (first_number) - (second_number)
    print("Result :" , result)
elif choice==3:
    print("Multiplication")
    first_number = int (input ("Enter first number : "))
    second_number = int (input ("Enter second number : "))
    result = (first_number) * (second_number)
    print("Result :" , result)
elif choice == 4:
    print("Division")
    first_number = int (input ("Enter first number : "))
    second_number = int (input ("Enter second number : "))
    result = (first_number) / (second_number)
    print("Result :" , result)
else:
    print("Invalid input")
    


