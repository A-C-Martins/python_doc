#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ldigit = int(repr(number)[-1])

if ldigit > 5:
    print(f"last digit of {number} is {ldigit} and is greater than 5")
elif ldigit == 0:
    print(f"last digit of {number} is {ldigit} and is 0")
elif ldigit < 6 and ldigit != 0:
    print(f"last digit of {number} is {ldigit} and is less than 6 and not 0")