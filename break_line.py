"""
    CLI that breaks a line longer than 40 characters on the next word.
"""

import fileinput

texto = ''

def quebra_linha(texto, n=40):
    proximo_espaco = texto[n:].split(' ', 1)
    linha = texto[:n] + proximo_espaco[0]
    resto = proximo_espaco[1]

    # Ignore original line breaks
    # resto = texto[n:].split()
    # linha = texto[:n] + resto[0]
    # resto = ' '.join(resto[1:])

    return linha, resto

for line in fileinput.input():
    texto += line

while True:
    if len(texto) < 40:
        print(texto)
        break

    linha, resto = quebra_linha(texto)
    print(linha)
    texto = resto