"""
Given two binary strings a and b, return their sum as a binary string.

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

>>> a = "11"
>>> b = "1"
>>> add_binary(a, b)
'100'

>>> a = "1010"
>>> b = "1011"
>>> add_binary(a, b)
'10101'
"""


def add_binary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    carry = 0
    result = ''

    for i in range(max_len)[::-1]:
        soma = int(a[i]) + int(b[i]) + carry
        result += str(soma % 2)
        carry = soma//2
    if carry == 1:
        result += '1'
    return result[::-1]


def add_binary_with_int(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
