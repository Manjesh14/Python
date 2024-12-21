# Find Angle MBC
# 15 more points to get your next star!
# Rank: 1957950|Points: 55/70
# Python
# Problem
# Submissions
# Leaderboard
# Discussions
# Editorial
# rsz_1438840048-2cf71ed69d-findangle.png  is a right triangle,  at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side .
# The second line contains the length of side .

# Constraints


# Lengths  and  are natural numbers.
# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10
# Sample Output

# 45°


from math import sqrt
from math import acos
from math import degrees

AB = int(input())
BC = int(input())

AC = sqrt(AB ** 2 + BC ** 2)

BM = AC / 2

angle = acos(BC / (2*BM))

print("{}{}".format(round(degrees(angle)), chr(176)))