# it is a concept

def pip(n):
    
    if n==0:
        return
    
    print("pre",n)
    pip(n-1)
    print("In",n)
    pip(n-1)
    print("Post",n)
    return

n=int(input("Enter the number : "))

pip(n)
