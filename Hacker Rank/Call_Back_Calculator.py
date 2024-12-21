
# CALL BACK CALCULATOR

import math
import os
import random
import re
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def specialop(a, b):
    return max(a, b)

def calculate(a, b, operation):
    callbacks = {'add': add, 'subtract': sub, 'max': specialop}
    callback = callbacks.get(operation.lower(), specialop)
    
    return callback(a, b)


a = int(input().strip())  
b = int(input().strip())
op = input().strip() 

print(calculate(a, b, op))