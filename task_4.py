def permute(s, answer):
    if len(s) == 0:
        print(answer, end=", ")
        return
    for i in range(len(s)):
        ch = s[i]
        left = s[:i]
        right = s[i+1:]
        rest = left + right
        permute(rest, answer + ch)

word = "DOG"
perms = []

# Collect permutations
def collect_permutations(s, answer):
    if len(s) == 0:
        perms.append(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        collect_permutations(rest, answer + ch)

collect_permutations(word, "")
perms.sort()
print(", ".join(perms))
