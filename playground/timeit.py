import timeit

def list_for():
    lista = []
    for n in range(1000):
        lista.append(n)
    return lista

def list_comp():
    lista = [n for n in range(1000)]
    return lista

print('list_for tooks {} secs.'.format(timeit.timeit(list_for, number=100000)))

print('list_comp tooks {} secs.'.format(timeit.timeit(list_comp, number=100000)))