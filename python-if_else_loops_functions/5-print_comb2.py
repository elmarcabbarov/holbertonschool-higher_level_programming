#!/usr/bin/python3
for i in range(0,100):
    if i < 99:
        if i < 10:
            i="0"+str(i)
        else:
            i=str(i)
        print(i, end =", ")
    elif i == 99:
        print(str(i))
