movies = []
movie1 = input("Enter first movie name:")
movie2 = input("Enter second movie name:")
movie3 = input("Enter third movie name:")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

list1 = ["1,2,3,2,1"]
user_input= input("Enter a string:")
if (user_input == list1):
    print("String is palindrome")
else:
    print("String is not a palindrome")
list1 = []
data = eval(input("Enter data:"))
list1.append(data)
print(list1)
list1 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if (copy_list1 == list1):
    print("Palindrome")
else:
    print("Not palindrome")

tuple1 = ("c", "d", "a", "a", "b", "b", "a")
 
print(tuple1.count("a"))   



list = [1,2,3,4,3,2,]
unique_lisrt = []
for i in list:
    if i not in unique_lisrt:
        unique_lisrt.append(i)
        print(unique_lisrt)

