# Basic idea --> use PreInPost

def zigzag(n):
    
    if n==0:
        return
    
    print(n, end=" ")
    zigzag(n-1)
    print(n, end=" ")
    zigzag(n-1)
    print(n, end=" ")
    return

n=int(input("Enter the number : "))

zigzag(n)
