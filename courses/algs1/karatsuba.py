#!/usr/bin/env python

from math import floor
# 1 = Recursively compute ac
# 2 = Recursively compute bd
# 3 = Recursively compute (a+b)(c+d)
# 3 - (1 + 2)

i = 5678
j = 12343465

def karatsuba(i, j):
    """Recursively multiply two integers"""
#     # Base case is multiplying two digits
#     # If the first number is a digit, and the second is also, return their product
#     # If either is not, split it into two, and do a full karatsuba

    if i < 10 or j < 10:
        return i * j
    else:
        i = str(i)
        midpoint = floor(len(i)/2)
        a = int(i[:midpoint])
        b = int(i[midpoint:])

        j = str(j)
        midpoint = floor(len(j)/2)
        c = int(j[:midpoint])
        d = int(j[midpoint:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    # Remember Gauss' trick
    g_trick = karatsuba(a+b, c+d) - ac - bd

    # m/2 is the offset for returning the base in ac
    m = max(len(str(i)),len(str(j)))
    m2 = m / 2

    return ac * 10**(2*m2) + g_trick * 10**m2 + bd


if __name__ == "__main__":
    i = int(input("First integer: "))
    j = int(input("Second integer: "))
    print(karatsuba(i, j))





        # i = str(i)
        # midpoint = floor(len(i)/2)
        # out = karatsuba(int(i[:midpoint]), int(i[midpoint:]))
        # print(f"out i: {out}")
        # print(f'{int(j[:midpoint])} * {int(j[midpoint:])}')

        # if j > 9:
        #     j = str(j)
        #     midpoint = floor(len(j)/2)
        #     out = karatsuba(int(j[:midpoint]), int(j[midpoint:]))
        #     print(f"out j: {out}")
        #     print(f'{int(j[:midpoint])} * {int(j[midpoint:])}')
        #     return out
        # print(f"i: {i}")
        # return i