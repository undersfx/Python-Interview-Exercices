"""
Given a signed 32-bit integer x, return x with its digits reversed.

If reversing x causes the value to go outside the signed 32-bit
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers.

Doctests:
>>> reverse(123)
321

>>> reverse(-123)
-321

>>> reverse(120)
21

>>> reverse(0)
0


Constraints:
-231 <= x <= 231 - 1
"""


def reverse_naive(x: int) -> int:
    num = str(x)
    if num[0] == '-':
        num = int('-' + num[:0:-1])
    else:
        num = int(num[::-1])

    if num.bit_length() > 31:
        return 0
    else:
        return num


def reverse(x: int) -> int:
    num = abs(x)
    pop = 0
    push = 0
    while num != 0:
        pop = num % 10
        num //= 10
        push = (push * 10) + pop

    return push if x > 0 else int(push/-1)
