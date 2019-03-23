x = [1, 2, 3, 4, 5]
y = ['um', 'dois', 'tres', 'quatro', 'cinco']

# Normal Way
# d = {}
# for i, v in enumerate(x):
#     d[v] = y[i]

# Pythonic Way
d = {k:v for k, v in zip(x, y)}

print(d)
