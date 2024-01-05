#!/usr/bin/python3
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in "qe":
        continue
    print("{0}".format(i), end="")
