"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.
For example:

Given:
>>> s = "the sky is blue"
>>> reverse_words(s)
'blue is sky the'
"""

def reverse_words(string):
    word_list = string.split()
    return ' '.join(reversed(word_list))


# How to reduce space complexity

from collections import deque

def reverse_words_generator(string):
    """
    >>> s = "the sky is blue"
    >>> list(reverse_words_generator(s))
    ['blue', 'is', 'sky', 'the']
    """
    palavra = deque()

    for letra in reversed(string):
        if letra == ' ':
            yield ''.join(palavra)
            palavra.clear()
        else:
            palavra.appendleft(letra)

    yield ''.join(palavra)