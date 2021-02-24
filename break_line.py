"""
    - Read from a text file (alice.txt) and print lines in a lenght of N.

    - No word should be broken in different lines, this means, If the n-th is
    in the middle of a word, the complete word should be printed in the same line.
"""

def break_lines(string, n=40, strip_original_linebreaks=True):
    '''
    >>> break_lines('asdf asdf', 6)
    asdf asdf

    >>> break_lines('asdf asdf', 4)
    asdf
    asdf

    >>> break_lines('a s d f', 1)
    a
    s
    d
    f
    '''

    linhas = []
    k = 0

    if strip_original_linebreaks:
        string = string.replace('\n', ' ')

    string_quebrada = string.split(' ')

    for palavra in string_quebrada:
        if not linhas:
            linhas.append(string_quebrada[0])
            continue

        if len(linhas[k]) + 1 < n:
            linhas[k] += ' ' + palavra
        else:
            k += 1
            linhas.append(palavra)

    print("\n".join(linhas))


if __name__ == "__main__":
    with open('alice.txt', encoding='UTF-8') as f:
        texto = f.read()

    break_lines(texto, 40)
