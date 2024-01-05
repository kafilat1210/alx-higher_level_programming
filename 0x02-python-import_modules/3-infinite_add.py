#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    _sum = 0
    for i in range(1, length):
        _sum += int(sys.argv[i])
    print(_sum)
