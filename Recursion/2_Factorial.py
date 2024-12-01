# Finding Factorial Using Recursion

# Basic idea n! = n * (n-1)!

def Factorial(n):
    if n == 0 or n == 1 :
        return 1
    fact = n * Factorial(n-1)
    return fact

n=int(input("Enter the number : "))

fact = Factorial(n)

print(f"The Factorial of {n} is = {fact}")
