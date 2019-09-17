'''
Problem: Given a S string, count the number that each character appears.

Doctest Exemple:

>>> s = 'hue HUE br'
>>> character_repetition_count(s)
{'h': 2, 'u': 2, 'e': 2, 'b': 1, 'r': 1}

>>> s = 'hue HUE br'
>>> character_repetition_count(s, case_sensitive=True)
{'h': 1, 'u': 1, 'e': 1, 'H': 1, 'U': 1, 'E': 1, 'b': 1, 'r': 1}

>>> s = 'hue HUE br'
>>> character_repetition_count(s, case_sensitive=True, ignore_spaces=False)
{'h': 1, 'u': 1, 'e': 1, ' ': 2, 'H': 1, 'U': 1, 'E': 1, 'b': 1, 'r': 1}
'''

def character_repetition_count(string: str, case_sensitive: bool = False, ignore_spaces: bool = True) -> dict:
    '''
    Counts the number of character occurences for a given string.
    '''

    counted = {}

    if ignore_spaces:
        string = string.replace(' ', '')

    if not case_sensitive:
        string = string.lower()
    
    for char in string:
        counted[char] = counted.get(char, 0) + 1
    
    return counted

if __name__ == "__main__":
    s = 'S F X'
    print(character_repetition_count(s))
    print(character_repetition_count(s, case_sensitive=True))
    print(character_repetition_count(s, case_sensitive=True, ignore_spaces=False))