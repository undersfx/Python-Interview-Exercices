"""
Given a string s, find the length of the longest substring without repeating characters.

Doctests:
>>> length_of_longest_substring("abcabcbb")
3

>>> length_of_longest_substring("bbbbb")
1

>>> length_of_longest_substring("pwwkew")
3

>>> length_of_longest_substring("")
0

Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    used = list()
    result = 0

    for char in s:
        if char not in used:
            used.append(char)
        else:
            used = used[used.index(char) + 1:]
            used.append(char)
        
        if len(used) > result:
            result = len(used)

    return result
