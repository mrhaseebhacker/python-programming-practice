# count = 1
# while count <= 5:
#     print(count)
#     count +=1
# in stopping condtiion we use while loop 
# count = 100
# while count >=1:
#     print(count)
#     count -=1
# n = int(input("Enter number:"))
# i = 1
# while i <=10:
#     print(i * n)
#     i +=1    

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# indx = 0
# while indx < len(nums):
#     print(nums[indx])
#     indx +=1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int (input("Enter number:"))
# i = 0
# while i < len(nums):
#     if (nums [i] == x):
#         print("Found at Idx:", i)
#         break
#     else:
#         print("Finding")
#     i += 1   

# i = 0
# while i <= 5:
#     if (i % 2==0):
#         i +=1
#         continue #to skip the current iteration
#     print(i)
#     i +=1   

# list = [1, 2, 3, 4, 5]
# for nums in list:
#  print(nums)
# # in traversing we use for loop
# vaeggies = ["potato", "cucumber", "tomato"]
# for el in vaeggies:
#  print(el)

# nums = [1,4,9,36,49,64,81,100]
# for el in nums:
#  print(el) 

# nums = [1,4,9,36,49,64,81,100,36]

# x = 36
# idx = 0
# for el in nums:
#     if (el == x):
#      print("found at idx",idx)
#      break
#     idx +=1
# seq = range(5)
# for i in seq:
#    print(i)


# for i in range(100,0,-1):
#  print(i)   

# n = int(input("Enter a number:"))
# for i in range(1,11):
#  print(n*i)

i = 0
sum_n = 0
while i<= 10:
    sum_n +=i
    i +=1
print("Sum of n natural numbers is :", sum_n)

n = 5
sum = 0
for i in range(1,n+1):
    sum +=i
print("Sum is :", sum)

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)

n = 5
fact = 1
i = 1
while i <=n:
    fact *=i
    i +=1
print(fact)
