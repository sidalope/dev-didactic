#!/usr/bin/env python

# Karatsuba multiplication:
# In the example 1234 * 5678; a = 12, b = 34, c = 56, d = 78.
# 1: Recursively compute ac
# 2: Recursively compute bd
# 3: Recursively compute (a+b)(c+d)
# 4: (a+b)(c+d) - ac - bd
# 5: ac * 10^(2 * the length of longest multiple / 2)
#       + step 4 * 10^(the length of longest multiple / 2)
#       + bd

# For a much clearer explanation of why step 5, check:
# https://iq.opengenus.org/karatsuba-algorithm/
# hint: remember, if x and y can be divided into two numbers like on
# line 4 above, x * y = (a * 10^m + b) * (c * 10^m + d)

# Base case is multiplying one digit by another integer.
# If the first or second number is a digit, return their product.
# If neither is, split it them in two, and do a full karatsuba.

# This implementation doesn't currently work for ints of varying length

from math import floor

def karatsuba(i, j):
    """Recursively multiply two integers"""
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
