#!/usr/bin/python3
def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        asc = ord(str[i])
        if asc >= 97 and asc <= 122:
            upper = asc - 32
            tmp[i] = chr(upper)
    print("{}".format(("").join(tmp)))
