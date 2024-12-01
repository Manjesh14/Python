# Print the numbers n - 1

# Basic idea --> print(n) and then calling (n-1)

def decreasing(n):
    
    print(n)
    
    if n == 1:
        return
    
    decreasing(n-1)
    return         # In Python no need of the Return

    
n=int(input("Enter The Number : "))

decreasing(n)

# Do The Experiment of interchanging the print(n) and Base Case
#Expected shit :
#        1 will not be printed

