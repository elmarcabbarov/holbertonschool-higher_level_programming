#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nfd = int(str(number)[-1:]) * (-1)
else:
    nfd = int(str(number)[-1:])

if nfd > 5:
    print("Last digit of " + str(number) + " is " + str(nfd) +
          " and is greater than 5")
elif nfd < 6 and nfd != 0:
    print("Last digit of " + str(number) + " is " + str(nfd) +
          " and is less than 6 and not 0")
else:
    print("Last digit of " + str(number) + " is " + str(nfd) +
          " and is 0")
