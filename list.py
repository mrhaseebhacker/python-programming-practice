fruits = ["apple", "orange", "banana"]
print (fruits)# printintg list
fruits.sort()
print (fruits)
fruits [1] = "cherry"
print (fruits)# changing element

fruits.append ("mango")
print(fruits)# adding element at the end

fruits.insert(1 ,"appricot")
print(fruits)# inserting element any index

fruits.remove("apple")
print(fruits)# removing first element

fruits.pop(2)
print(fruits)# removing element by index

marks = [94.3, 87.5, 89.4, 78.6]

print(marks[1:4])# slicing in list
marks.remove(78.6)
print(marks)

student = ["Haseeb", 20, "Lahore"]

print(student)
student[0] = "Ahmad" #lists are mutable
print(student)