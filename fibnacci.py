a, b = 0, 1
for i in range(20):
    print(a)
    a, b = b, a + b

a = 0
b = 1
for i in range(1,10):
    c = a+b
    a = b
    b = c
    print(c)