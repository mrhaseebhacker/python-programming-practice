num = int(input("Enter a number :"))

if num <= 1:
        print("Number is not a prime")
else:        
    for i in range(2,int(num ** 0.5) + 1):
       if num % i == 0:
          print("Number is not a prime")
          break
       else:
         print("Number is prime")    