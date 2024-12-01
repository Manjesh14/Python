# Make a Function which calculates 'a' raised to the power 'b' using recursion

# Basic idea --> a^b = a*a^(b-1)

def power(a,b):
    if (b == 0):
        return 1
    
    ans=a * power(a,b-1)
    return ans

a = int(input("Enter the base : "))

b = int(input("Enter the power : "))

a_raised_to_b=power(a,b)

print(a_raised_to_b)