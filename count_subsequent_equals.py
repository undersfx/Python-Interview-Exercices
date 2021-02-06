"""
Write a function that converts the input to the output:

Input: "aaaabbbcca"
Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

Test:
>>> count_subsequent_equals("aaaabbbcca")
[('a', 4), ('b', 3), ('c', 2), ('a', 1)]

>>> count_subsequent_equals("")
[]

>>> count_subsequent_equals("a")
[('a', 1)]
"""

def count_subsequent_equals(text):
    """
    Converts the input into a list of equal subsequent characters

    :text: str
    :return: List[Tuple[str, int]]
    """
    result = []
    prev_char = text[:1]
    count = 0

    for char in text:
        if prev_char == char:
            count += 1
            continue
        else:
            result.append((prev_char, count))
            count = 1

        prev_char = char

    if count > 0:
        result.append((char, count))

    return result