"""
Given an array of integers arr, and three integers a, b and c.
You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

1. 0 <= i < j < k < arr.length
2. |arr[i] - arr[j]| <= a
3. |arr[j] - arr[k]| <= b
4. |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.

Return the number of good triplets.

Constraints:
3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000

Tests:
>>> arr = [3,0,1,1,9,7]
>>> a = 7
>>> b = 2
>>> c = 3
>>> count_good_triplets(arr, a, b, c)
4

>>> arr = [1,1,2,2,3]
>>> a = 0
>>> b = 0
>>> c = 1
>>> count_good_triplets(arr, a, b, c)
0
"""

from typing import List


def count_good_triplets(arr: List[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if abs(arr[i] - arr[j]) <= a \
                and abs(arr[j] - arr[k]) <= b \
                and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count
