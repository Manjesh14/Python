
# DECORATOR FOR VALIDATING POSITIVE NUMBER

import math

def validate_positive(func):
    def wrapper(x):
        if x < 0:
            return "Input must be a positive number"
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return math.sqrt(x)

x = float(input())
print(square_root(x))