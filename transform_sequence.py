"""
Em matemática existe uma sequência de inteiros que seria algo assim:

1, 11, 21, 1211, 111221, 312211, 13112221... e assim por diante

Essa progressão se forma como se os números fossem lidos em voz alta.
Por exemplo, na sequência 112, o número 1 aparece duas vezes (dois 1)
e o número 2 aparece uma vez (um 2), assim poderia ser lido: 2112.

A sequência é gerada iterativamente, usando o valor gerado como base
para criar o próximo número.

Neste desafio você vai implementar o método que recebe um valor base
e um número multiplicador e aplica a lógica da sequência tantas vezes
quanto indicado pelo multiplicador. Por exemplo:

sequência base inicial: 11223
multiplicador: 2

Aplicando o algoritmo:
11223
212213
1211221113
Retorno: 1211221113

Doctest:
>>> transform_seq(1, 3)
'1211'

>>> transform_seq(11223, 2)
'1211221113'
"""


def transform_seq(s, m):
    def _transform_seq(s, m):
        if m == 0:
            return s

        multiplier = 1
        previous = s[0]
        result = ''

        for char in s[1:]:
            if previous == char:
                multiplier += 1
                continue
            else:
                result += f'{multiplier}{previous}'
                multiplier = 1
            previous = char

        result += f'{multiplier}{previous}'

        return _transform_seq(result, m - 1)

    return _transform_seq(str(s), m)
