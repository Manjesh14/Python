# Calculating the nth fibonacci number 

# basic idea ==> fibonacci Number will be equal to nth fibo= (n-1)th fibo + (n-2)th fibo

# fibonacci Number : 0   1   1   2   3   5   8   13
# term               1st 2nd 3rd 4th 5th 6th 7th 8th

def fibo(n):                    # Basically here n means nth term not the value
    if n == 1 or n==2:          # But atlast when 2nd and 1st term called we give the values of that terms
        
        return n-1
    
    return fibo(n-1) + fibo(n-2)  # same as a = fibo(n-1 ) + fibo(n-2)
                                #   return a
                                
n = int(input("Enter the number : "))
ans= fibo(n)
print(ans)