
# PRIME GENERATOR

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def prime(limit):
    l = []
    for num in range(2,limit+1):
        if is_prime(num):
            l.append(num)
    return l
    
limit = int(input())
print(prime(limit))