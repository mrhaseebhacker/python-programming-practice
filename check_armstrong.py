n = int(input("Enter a number :"))
order = len(str(n))

sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    cube = digit** order
    sum += cube
    temp //=10
if sum == n:
    print("It is an armstrong")
else:
    print("It is not an armstrong")

