#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0
print(f"Last digit of {number:d} is ", end="")
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10
print(f"{last:d} ", end="")
if (last < 6) and (last != 0):
    print("and is less than 6 and not 0")
if last > 5:
    print("and is greater than 5")
if last == 0:
    print("and is 0")
