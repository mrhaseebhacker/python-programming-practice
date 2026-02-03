def reverse_integer(n):
    reversed_num = 0
    negative = n < 0  # Check if the number is negative
    n = abs(n)  # Work with the absolute value
    
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Append it to the reversed number
        n //= 10  # Remove the last digit from the original number
        if reversed_num > 2**31 - 1:
            return 0

    return -reversed_num if negative else reversed_num  # Restore the sign if needed

# Example usage
# num = -123
# print(reverse_integer(num))  # Output: -321
print(reverse_integer(-123))