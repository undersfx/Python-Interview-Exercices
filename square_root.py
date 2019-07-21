"""
Square Root the hard way
"""


def find_square_root(x):

    """Calculates the square root of a value x"""
    
    precision = 10 ** -5

    # Choose two numbers in a way that sqrt(x) belongs to the interval
    s = 0
    e = int(x)
  
    # Find the root
    while (e - s) > precision:
        # Find the middle
        m = (e + s) / 2

        if m**2 > int(x):
            e = m
        else:
            s = m

    return m
    

inputs = []

for i in range(0, 11):
    value = input()
    inputs.append(value)

for value in inputs:
    square_root = find_square_root(value)
    print('%.3f' % square_root)
