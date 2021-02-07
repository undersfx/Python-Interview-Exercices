"""
Square Root the hard way

Tests:

>>> find_square_root(0)
0
>>> find_square_root(1)
0.9999923706054688
>>> find_square_root(2)
1.4142074584960938
>>> find_square_root(3)
1.732046127319336
>>> find_square_root(4)
2.0000076293945312
>>> find_square_root(5)
2.2360706329345703
>>> find_square_root(6)
2.4494876861572266
>>> find_square_root(7)
2.645754814147949
>>> find_square_root(8)
2.8284225463867188
>>> find_square_root(9)
2.999997138977051
>>> find_square_root(10)
3.1622791290283203
"""


def find_square_root(x):
    """Calculates the square root of a value x"""
    PRECISION = 10 ** -5

    # Choose two numbers in a way that sqrt(x) belongs to the interval
    s = 0
    e = int(x)
    m = 0

    # Calculation to find the square root
    while (e - s) > PRECISION:
        # Find the middle
        m = (e + s) / 2

        if m**2 > int(x):
            e = m
        else:
            s = m

    return m

if __name__ == "__main__":
    inputs = []

    for i in range(0, 65):
        inputs.append(i)

    for value in inputs:
        square_root = find_square_root(value)
        print('Square Root for % is equal to %.3f' % (value, square_root))