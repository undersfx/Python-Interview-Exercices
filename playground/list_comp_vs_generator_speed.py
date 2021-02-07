import time

tamanho = 50000000

print('Create test:\n')
start = time.time()
list_comp = [i for i in range(tamanho)]
print('{} done in {:.2f} secs.'.format(type(list_comp), time.time() - start))

start = time.time()
gen = (i for i in range(tamanho))
print('{} done in {:.2f} secs.\n'.format(type(gen), time.time() - start))

time.sleep(1)
print('Looping test:')

start = time.time()
print('Looping through list comp')

for n in list_comp:
    pass

print('Done in {:.2f} secs.'.format(time.time() - start))

start = time.time()
print('Looping through generator')

for n in gen:
    pass

print('Done in {:.2f} secs.'.format(time.time() - start))