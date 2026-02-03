# swapping using third variable
a = 10
b = 15

print("Before swapping :",a,b)

temp = a 
a = b
b = temp

print("After swapping :",a,b)

# without using third variable
a = 10
b = 15

print("Before swapping :",a,b)

a,b = b,a

print("After swapping :",a,b)