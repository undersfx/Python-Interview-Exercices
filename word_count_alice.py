"""
Count the number of occurrences of the string 'alice' in the book "Alice in Wonderland" (alice.txt)

Tests:
>>> text = "banana banana banana"
>>> word = 'banana'
>>> count_words(text, word)
3

>>> text = "a aba baba abababa aba"
>>> word = 'aba'
>>> count_words(text, word)
2

>>> count_words("a", "")
-1

>>> count_words("", "a")
-1

>>> count_words("", "")
-1
"""


from string import punctuation


WORD = 'alice'

def count_words(text, word):
        # Normaliza o texto o convertendo para minusculo
        text = text.lower()

        # Normaliza a  pontuação substituindo por ' '
        for x in punctuation:
                text = text.replace(x, ' ')

        # Quebra palavrras em uma list
        text = text.split()

        if not text or not word: return -1

        # Dicionário de contagem
        result_dict = {}

        for s in text:
                # Procura por contagem de palavras, caso não encontre retorna 0 + 1
                result_dict[s] = result_dict.get(s, 0) + 1

        return result_dict[word]


if __name__ == "__main__":
        #Abre arquivo alice.txt em alice
        with open('alice.txt', encoding="utf8") as alice:
                # Carrega o conteúdo do arquivo
                texto = alice.read()
                count = count_words(texto, WORD)

                # Mostra o total somado correspondente ao indice esperado (WORD)
                print('A palavra "'+ WORD + '" aparece %s vezes.' % count)
