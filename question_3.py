num = [1, 1, 0]
# print(set(num))
unique_num = []
result = []

for val in num:
    if val not in unique_num:
        unique_num.append(val)
        result.append(val)
    else:
        result.append('_')    
print(result)