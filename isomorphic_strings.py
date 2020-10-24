"""
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

Docstrings:
>>> is_isomorphic('egg', 'add')
True

>>> is_isomorphic('foo', 'bar')
False

>>> is_isomorphic('baba', 'bbbb')
True

>>> is_isomorphic('baba', 'abab')
True

>>> is_isomorphic('abacate', 'bbbcbte')
True

>>> is_isomorphic('abacate', 'babcbte')
True

>>> is_isomorphic('abc', 'ooo')
True

>>> is_isomorphic('a', 'ba')
False
"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    correspondencia = {}
    for letra_s, letra_t in zip(s, t):
        if letra_s != letra_t and letra_t not in correspondencia.keys():
            correspondencia[letra_t] = letra_s

    if len(correspondencia.keys()) != len(set(correspondencia.values())):
        return False

    return True
