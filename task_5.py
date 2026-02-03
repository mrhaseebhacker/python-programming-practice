word = "MISSISSIPPI"

word = word.upper()

checked = []  

print("Character frequencies:")

for i in range(len(word)):
    ch = word[i]
    if ch not in checked: 
        count = 0
        for j in range(len(word)):
            if word[j] == ch:
                count += 1
        print(ch, "=", count, end=", ")
        checked.append(ch)
