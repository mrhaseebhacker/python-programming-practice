# nums = [1, 3, 4, 7, 5]
# target = 6
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print("Target found at Indices:", i,j)
def two_sum(nums, target):
    num_dic = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dic:
            return [num_dic[complement], i]
        num_dic[num] = i
    return []

nums = [2, 7, 5]
target = 9
print(two_sum(nums, target))
