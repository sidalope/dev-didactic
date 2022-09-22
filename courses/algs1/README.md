Divide and Conquer, Sorting and Searching, and Randomized Algorithms

https://www.coursera.org/learn/algorithms-divide-conquer#syllabus

[Mathematics for Computer Science (by Eric Lehman and Tom Leighton)](https://www.cs.princeton.edu/courses/archive/fall06/cos341/handouts/mathcs.pdf)


karatsuba and simple recursive int multiplication

Merge sort
- exemplar of the divide and conquer paradigm

merge sort with vs without duplicates
without (ascending):
- divide the array in two and recursively sort
- populate the output array with the minimum from the beginning of either A or B

(recall the recursion tree visualisation)

6n * log2 (n) + 6n
(based on a psudocode analysis of work done, and when n is a power of 2)
(This is O(log), no?)
so, n * log (n)

Guiding Principles:
- Worst case analysis (opposed to average case and benchmark analyses)
- Partially disregarding constant and lower order factors
    - (Constant factors are frequently dependent or implementation (aside from not scaling significantly))
- Asymptotic analysis

Asymptotic analysis
It’s coarse enough to suppress certai details : constant factors and lower-order terms.
(See lectures for the full formal definition)
Big O: T(n) = O(f(n)) ~ Upper bound (above n0)
Omega: T(n) = Ω(f(n)) ~ Lower bound (above n0)
Theta: T(n) = Θ(f(n)) ~ equivalence
Little o notation is for a strictly less than relation, i.e. no n0

