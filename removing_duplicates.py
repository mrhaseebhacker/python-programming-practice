dup = ["a", "b", "c", "d", "c", "d", "b", "a"]
unique = (set(dup))
print(unique)

dup = ["a", "b", "c", "d", "c", "d", "b", "a"]
unique_list = []
for item in dup:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)