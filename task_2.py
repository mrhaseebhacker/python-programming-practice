Text = "ABABDABACDABABCABAB"
pattern = "ABAB"
positions = []

for i in range(len(Text) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if Text[i + j] != pattern[j]:
            match = False
            break
    if match:
        positions.append(i)

if positions:
    print("Pattern found at positions:", positions)
else:
    print("Pattern not found")
