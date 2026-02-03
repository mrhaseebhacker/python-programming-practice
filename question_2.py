# input = input("Enter numbers separated by spaces :")

# integers = []
# for val in input.split():
#  integers.append(int(val))


nums = [1, 2, 0]

positive_nums = []

for num in nums:
    if num > 0:
        positive_nums.append(num)

positive_nums.sort()

smallest =1

for num in positive_nums:
    if num == smallest:
        smallest += 1
print("Smallest integer is :", smallest)
    
