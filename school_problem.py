def countStudents(students, sandwiches):
    from collections import Counter

    count = Counter(students)  # Count how many students want 0s and 1s

    for s in sandwiches:
        if count[s] > 0:
            count[s] -= 1  # One student takes the sandwich
        else:
            # No student wants the current sandwich
            break

    return count[0] + count[1]  # Remaining students who couldn't eat

students = [1,1,0,0]
sandwiches = [0,1,0,1]
# print(countStudents(students, sandwiches))  # Output: 0
a = '9'
b = '4'
print(a*b)