# in a given maze you have to go from (1,1) to (n,m) only by moving right and down

# Basic idea --> divide the problem into smaller problems by movig right or down once

def maze(n,m,a,b):# n= end row ; m = end column ; a = current row ; b = current column
    rightways = 0
    downways = 0
    
    if a == n and b == m:
        return 1
    
    if a == n:
        rightways += maze(n,m,a,b+1)
          
    if b == m:
        downways += maze(n,m,a+1,b)
        
    if a < n and b < m:
        rightways += maze(n,m,a,b+1)
        downways += maze(n,m,a+1,b)
        
    
        
    total_ways = rightways+downways 
    return total_ways

n= int(input("Enter the number of rows : "))
m=int(input("Enter the number of coloumn : "))

ways = maze(n,m,1,1)
print(ways)
