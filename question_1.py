numbers = [2,7,11,6,5]

target = 9
found = False

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Indices: {i}, {j} -> values: { numbers[i]},{numbers[j]}")
        
            found = True

if not found:
    print("Target not found")
