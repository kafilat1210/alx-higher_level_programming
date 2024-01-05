#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as mod1
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, mod1.add(a, b)))
    print("{} - {} = {}".format(a, b, mod1.sub(a, b)))
    print("{} * {} = {}".format(a, b, mod1.mul(a, b)))
    print("{} / {} = {}".format(a, b, mod1.div(a, b)))
