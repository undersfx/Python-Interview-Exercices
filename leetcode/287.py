"""
Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

Doctests:
>>> find_duplicate([1,3,4,2,2])
2

>>> find_duplicate([3,1,3,4,2])
3

>>> find_duplicate([1,1])
1

>>> find_duplicate([1,1,2])
1
 
>>> find_duplicate([18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17])
17


Constraints:
- 2 <= n <= 3 * 104
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one 
integer which appears two or more times.
- There is only one repeated number in nums, return this repeated number.
"""


from typing import List


def find_duplicate(nums: List[int]) -> int:
    '''
    Naive approach implementation

    Time complexity : O(n)
    Space complexity : O(n)
    '''
    compare = set()
    for i in nums:
        if i not in compare:
            compare.add(i)
        else:
            return i


def find_duplicate(nums: List[int]) -> int:
    '''
    Implementation using the Floyd’s Algorithm of cycle detection (Tortoise and Hare).
    
    Time complexity : O(n)
    Space complexity : O(1)
    '''

    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    hare = nums[0]

    while hare != tortoise:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
