# Problem :- Print the number first decreasing till 1 and increasing till the n

# basic idea --> Use the print(n) before and after the Recursive Call




def incdec(n):
    if n == 0:
        return
    print(n)
    incdec(n-1)
    print(n) 
    return

n=int(input("Enter The number : "))

incdec(n)