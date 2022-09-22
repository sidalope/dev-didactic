#!/usr/bin/env python

# Merge Sort pseudo:
# Recursively sort 1st half of the input
# Recursively sort 2nd half of the input
# Merge two sorted sublists into one

# Because the base case of the sort is always going to be found in
# the same place relative to the size of the input, can't space be
# saved by avoiding recursion?

from collections import deque

def merge_sort(list_in):
    """Sort two lists of integers in ascending order (n log(n))"""
    if len(list_in) > 1:
        # Would it save time to assign the midpoint to a variable,
        # and either way, would it be preferable to save memory?
        first_half = list_in[:int(len(list_in)/2)]
        second_half = list_in[int(len(list_in)/2):]
        # Optimize time and mem by not assigning the lists any space?

        # Turn to double ended queue only for optimized popping index 0
        first_half = deque(merge_sort(first_half))
        second_half = deque(merge_sort(second_half))

        list_out = []
        while second_half:
            if first_half:
                if first_half[0] < second_half[0]:
                    list_out.append(first_half.popleft())
                else:
                    list_out.append(second_half.popleft())
            else:
                list_out.append(second_half.popleft())
        while first_half:
            list_out.append(first_half.popleft())
    else:
        # Base case
        return list_in

    return list_out


if __name__ == "__main__":
    unsorted = [int(x) for x in input("A list of integers separated by spaces: ").split(" ") if x]
    print(merge_sort(unsorted))
