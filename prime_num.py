nums =range (2, 100)
def prime_num(num):
    for x in range (2, int(num ** 0.5) + 1):
     if (num%x)==0:
      return False
    return True

primes = filter(prime_num, nums)

print(list(primes))