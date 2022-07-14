import time

SIZE = 10000000

LIST_COMP = f'[i for i in range({SIZE})]'
GENERATOR = f'(i for i in range({SIZE}))'

def calculate_time(expr):
    print(f'\nExpression: {expr}')

    t1 = time.time()
    obj = eval(expr)

    print(f'Creation done in {time.time() - t1:.2f} secs.')

    t2 = time.time()
    for _ in obj:
        pass

    print(f'Loop done in {time.time() - t2:.2f} secs.')
    print(f'Total: {time.time() - t1:.2f} secs.')


if __name__ == '__main__':
    calculate_time(LIST_COMP)
    calculate_time(GENERATOR)
