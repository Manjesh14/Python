# Problem : 

# Basic Idea : Use the concepts of Maze Path and PreInPost

# minimum number of ways will be == (2 ^n) - 1  where n is the number of disks

def tower(n,s,h,d):
    if n==0 :
        return
    tower(n-1,s,d,h)
    print(s,"-->",d)
    tower(n-1,h,s,d)
    return

n=int(input("Enter the number of disks : "))

tower(n,"A","B","C")
