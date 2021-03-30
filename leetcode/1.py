"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

You can return the answer in any order.

Doctests:
>>> nums = [2,7,11,15]
>>> target = 9
>>> two_sum(nums, target)
[0, 1]

>>> nums = [3,2,4]
>>> target = 6
>>> two_sum(nums, target)
[1, 2]

>>> nums = [3,3]
>>> target = 6
>>> two_sum(nums, target)
[0, 1]


Constraints:
- 2 <= nums.length <= 103
- 109 <= nums[i] <= 109
- 109 <= target <= 109
- Only one valid answer exists.


Implementation:
Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


def two_sum_naive(nums: List[int], target: int) -> List[int]:
    for i, value in enumerate(nums):
        search = target - value
        if search in nums[i + 1:]:
            j = nums.index(search, i + 1)
            return [i, j]


def two_sum(nums: List[int], target: int) -> List[int]:
    complement = dict()
    for i, value in enumerate(nums):
        if value in complement.keys():
            return [complement[value], i]
        search = target - value
        complement[search] = i
