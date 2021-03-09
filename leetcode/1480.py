"""
Given an array nums.

We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Tests:
>>> nums = [1,2,3,4]
>>> runningSum(nums)
[1, 3, 6, 10]

>>> nums = [1,1,1,1,1]
>>> runningSum(nums)
[1, 2, 3, 4, 5]

>>> nums = [3,1,2,10,1]
>>> runningSum(nums)
[3, 4, 6, 16, 17]
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    sum = 0
    result = []
    for value in nums:
        sum += value
        result.append(sum)
    return result
