# Print the numbers 1 to n

# Basic idea --> (i)  Using Extra variable/Parameter
#                (ii) Without Extra Variable/Parameter
                
# (i)  Using Extra Variable/Parameter

#  (My Method)

# basic idea --> defining an extra variable with 1 and increasing it and decreasing n till n becomes 1

def incresing(n,a):
    print(a)
    if n == 1:
        return
    
    incresing(n-1, a+1)
    return

n=int(input("Enter The number : "))

incresing(n,1)

# or 
#(Vedio Method)
# basic idea --> defining extra varible with 1 and increasing it till it is equal to n

def incresing(x,n):
    if x>n:
        return
    print(x)
    
    incresing(x+1, n)
    return

n=int(input("Enter The number : "))

incresing(1,n)

# (ii)  Without Using Extra Variable / Parameter

# basic idea --> By printing Number after the Recursion call
def increaseing(n):
    if n == 0:
        return
    increaseing(n-1)
    print(n) 
    return

n=int(input("Enter The number : "))

increaseing(n)