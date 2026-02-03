numbers = [1,25,7,6.8,9]
num = float(input("Enter a number :"))

found = False

for i in range (len(numbers)):
    if num == numbers[i] :
        print("Number found at", i)
        found = True
        break
if not found:
        print("Number not found")
