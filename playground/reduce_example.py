import functools

lista = ['p', 'y', 't', 'h', 'o', 'n']

def concatena(x, y):
    string = x + y
    print('Concatenando {} com {}.'.format(x, y))
    return string

# string = functools.reduce(lambda x,y: x + y, lista)
string = functools.reduce(concatena, lista)

print('Resultado: {}'.format(string))
