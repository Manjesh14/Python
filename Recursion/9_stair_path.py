# The problem is How many ways are there to climb stairs of n steps to get upto nth stair and the allowed cases are one can take 1 or 2 steps at a time

# basic idea ==> split the big problem into the smaller programs

def stair(n):
    if n == 1 or n == 2:  #if you want to go through 1 step there will bw only one way
                        #if you want to go through 2 steps there will bw only two way
        return n
    
    return stair(n-1)+stair(n-2) #Considering The you are at the final stair and you want to go to first stair
#                                you can come one step down or 2 step down

n = int(input("Enter the number : "))

NoOfWays=stair(n)

print("Number of ways : ", NoOfWays)


# Final Summary : we are reducing the problem by redducing the number of steps

