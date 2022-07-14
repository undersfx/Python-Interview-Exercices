"""
    Given a tuple of objects and a tuple of their respective names.
    Return a dictionary with the mapping of objects to names.
"""

x = (1, 2, 3, 4, 5)
y = ('um', 'dois', 'tres', 'quatro', 'cinco')

# Normal Way
# d = {}
# for i, v in enumerate(x):
#     d[v] = y[i]

# Pythonic Way
d = {k:v for k, v in zip(x, y)}

print(d) # {1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco'}
