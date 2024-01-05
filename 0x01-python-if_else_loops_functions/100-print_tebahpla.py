#!/usr/bin/python3
output = ""
upper = False

for char in range(ord('z'), ord('a') - 1, -1):
    if upper:
        output += chr(char).upper()
    else:
        output += chr(char).lower()
    upper = not upper

print("{}".format(output), end="")
