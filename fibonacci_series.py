a = 0 
b = 1
for i in range(20):
    print(a)
    temp= a
    a = b
    b = temp + b
# print((lambda x,y: x+y)(1,2))
