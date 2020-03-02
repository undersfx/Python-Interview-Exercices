'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

Tests:

>>> nums = [1,3,4,2,2]
>>> find_duplicates(nums)
2

>>> nums = [3,1,3,4,2]
>>> find_duplicates(nums)
3
'''

def find_duplicates(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    pointer = nums[0]

    while pointer != tortoise:
        pointer = nums[pointer]
        tortoise = nums[tortoise]

    return pointer
