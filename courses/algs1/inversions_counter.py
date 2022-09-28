#!/usr/bin/env python


# An input A. Calculate the number of inversions of the array.
# Inversion: a pair of of numbers in A with indices i and j, so
# that A[i] > A[j] (for out of order = not in increasing order)

# Consider ranking algorithms. Evaluating ranking similarity,
# perhaps as in collaborative ranking. Collaborative filtering.

# Max inversions in array size n: n(n-1)/2
# If the array is ordered, there are 0 inversions.

# Conceptual subdivision for algorithmic opt:
# left inversions: i,j <= n/2
# right inversions: i,j >= n/2
# split inversions: i <= n/2 < = j

# B, C, D, are sorted verions of the input array. D being sorted is a
# byproduct of the alg
# x, y, z, are the number of inversions counted by that recursive call

# sort_and_count(A, n)
#   if n = 1
#     return 0
#   else
#       B, x = sort_and_count(first half of A, n/2)
#       C, y = sort_and_count(second half of A, n/2)
#       D, z = merge_and_count_split_inversions(B, C, n)
#
#   return x + y + z

# merge_and_count_split_inversions(B, C, n)
#   split_inversions
#   D = empty array
#   while B and C
#       If B[0] < C[0]
#           pop B[0] to D
#       else
#           pop C[0] to D
#           split_inversions += size of B
#
#   Concatenate the rest of B or C
#   return D, split_inversions

# O(n) for merge
# O(n) for counting the number of inversions
# counting split inversions is O(n) + O(n) = O(n) overall
# Counting total inversions is O(n log(n))