
# CLOSUSRE FOR MULTIPLIER

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
factor = int(input().strip())
x = int(input().strip()) 
multiplier = make_multiplier(factor)
print(multiplier(x))