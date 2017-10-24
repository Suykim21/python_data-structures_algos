# Find prime numbers
def is_prime_v1(n):
    if n == 1:
        return False

    for d in range(2, n):
        if n% d == 0:
            return False
    return True

# optimization
import math

def is_prime_v2(n):
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


# optimization

def is_prime_v3(n):
    if n == 1:
        return False

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n% 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True
    

