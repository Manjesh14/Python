# in a given maze you have to go from (1,1) to (n,m) only by moving right and down

# Basic idea --> instead of going from (1,1) to (n,m) go from (n,m) to (1,1) just change the numbering of maze

def maze(n,m):
    rightways = 0
    downways = 0
    if n == 1 and m == 1:
        return 1
    
    if n == 1:  # cannot go down
        rightways += maze(n,m-1)
    
    if m == 1:  # cannot go right
        downways += maze(n-1,m)
    
    if n > 1 and m > 1:
        rightways += maze(n,m-1)
        downways += maze(n-1,m)
    
    total_ways = rightways+downways 
    return total_ways
        
        
    
n= int(input("Enter the number of rows : "))
m=int(input("Enter the number of coloumn : "))

ways = maze(n,m)
print(ways)