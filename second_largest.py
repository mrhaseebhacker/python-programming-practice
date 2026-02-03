# list = [1,4,6,7,8,9]
# list.sort()
# second_largest = list[-2]
# print(second_largest)

# numbers = [1,4,6,7,8,9]
# unique_numbers = sorted(set(numbers))
# if len(unique_numbers) < 2:
#     print("No second largest number")
# else:
#     print("Second largest number :",unique_numbers[-2])


numbers = [1,4,6,7,8,9]
first = float("-inf")
second = float("-inf")
if len(numbers) < 2:
    print("No second largest")
else:
 for num in numbers:
    if num > first:
            second = first
            first = num
    elif num > second and second!= first:
         second = num
if second == float('-inf'):
    print("No second largest")         
else:
    print("Second largest :", second)
