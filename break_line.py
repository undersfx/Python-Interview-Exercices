"""
    Read from file and print lines shorter than n (n=40).
"""

import fileinput


def main(s, n=40):
    linhas = []
    k = 0

    string_quebrada = s.split(' ')

    for palavra in string_quebrada:
        if not linhas:
            linhas.append(string_quebrada[0])
            continue

        if len(linhas[k]) + len(palavra) < n:
            linhas[k] += ' ' + palavra
        else:
            k += 1
            linhas.append(palavra)

    print("\n".join(linhas))


if __name__ == "__main__":
    texto = ''
    for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
        texto += line

    # Test
    # with open('alice.txt', encoding='UTF-8') as f:
    #     texto = f.read()

    main(texto)
