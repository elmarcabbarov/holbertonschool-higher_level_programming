#!/usr/bin/python3
for i in range(1,100):
    if i < 10:
        print("0"+str(i), end =",")
    elif i == 99:
        print(str(i))
    else:
        print(str(i), end=",")
