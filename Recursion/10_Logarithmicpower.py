## Make a Function which calculates 'a' raised to the power 'b' using recursion

#basic Idea --> a^b == a^b/2 * a^b/2

def power(a,b):
    if b % 2 != 0:
        if b == 1 :
            return a
        return a*power(a,b//2)*power(a,b//2)   # Note that we have to use the floor division to ensure the resultant b to be integer 
                                                # if b is floating value then the a to the power floating value is irrelevant
                                                
    if b % 2 == 0:
        if b == 1 :
            return a
        return power(a,b//2)*power(a,b//2)
    return

a = int(input("Enter the base : "))

b = int(input("Enter the power : "))

a_raised_to_b=power(a,b)

print(a_raised_to_b)