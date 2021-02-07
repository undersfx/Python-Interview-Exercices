'''
    Encontrar sequencia de 3 números N (n = interiro positivo entre 0 e 9)
'''

SECRET = (9, 2, 3)

# Without generator:

# Non-Pythonic possible solution for extra loops
# secret_found = False

# for s1 in range(10):
#     if secret_found:
#         break
#     for s2 in range(10):
#         if secret_found:
#             break
#         for s3 in range(10):
#             if (s1, s2, s3) == SECRET:
#                 print('Found secret: {}'.format((s1, s2, s3)))
#                 secret_found = True
#                 break
#             print(s1, s2, s3)

# With generator:

def sequence_generator():
    for x in range(10):
        for y in range(10):
            for z in range(10):
                yield (x, y, z)

for (s1, s2, s3) in sequence_generator():
    print(f'Testing {s1, s2, s3}')
    if (s1, s2, s3) == SECRET:
        print('Found secret: {}'.format((s1, s2, s3)))
        break