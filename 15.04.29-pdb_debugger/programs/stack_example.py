#!/usr/bin/env python

def main():
    a = 10
    b = 55
    result = abs_a_minus_b(a,b)
    print("The absolute value of {0}-{1} is {2}".format(a,b,result))


def abs_a_minus_b(x,y):
    if x > y:
        z = x - y
    else:
        z = y - x
    return z


if __name__ == '__main__':
    main()
