numbers = []
number1 = int(input("Enter number 1:"))
number2 = int(input("Enter number 2:"))
number3 = int(input("Enter number 3:"))
number4 = int(input("Enter number 4:"))
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.sort()
largest_number = numbers[-1]
print("Largest number is:",largest_number)