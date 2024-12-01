# print the sum of n numbers

# Basic idea --> define the variable initialise with 0 and add n to it

def sum1(n,sum):
    
    if n == 0:
        print(sum)
        return
    
    sum1(n-1,sum+n)
    
    return      # We can't return the sum because the value of sum at this stage is 0


    
n=int(input("Enter The Number : "))

sum1(n,0)


# Outcome : We can write the code inside the stopping Condition also

# Point to remember 
#               to get the term of the last cycle make use of the Stopping Condition

# Method 2
# Using Return type 

# Basic idea --> Use the same logic used for Factorial but replace the * with +

def sum2(n):
    
    if n==0 or n ==1  :
        return n
    
    sum= n + sum2(n-1)
    return sum

n=int(input("Enter The Number : "))

sum = sum2(n)

print("Sum is = ", sum)