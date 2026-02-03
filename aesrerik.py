for i in range(1,10):    
    print(i*"*")


string = (input("Enter a string :"))
string2 = string[::-1]
print(string2)

str = input("Enter a string :")
if (str == str[::-1]):
    print("Stirng is palindrome:")
else:
    print("String is not a palindrome")