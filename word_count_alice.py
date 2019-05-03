#Importa lib de string para utilizar as pontuações
import string

WORD = 'alice'

#Abre arquivo alice.txt em alice
with open('alice.txt', encoding="utf8") as alice:

        # Carrega o conteúdo do arquivo
        texto = alice.read()

        # Normaliza o texto o convertendo para minusculo
        texto = texto.lower()

        # Normaliza a  pontuação substituindo por ' '
        for x in string.punctuation:
                texto = texto.replace(x, ' ')

        # Quebra palavrras em uma list
        texto = texto.split()

        # Dicionário de contagem
        d = {}

        for palavra in texto:
                # Procura por contagem de palavras, caso não encontre retorna 0 + 1
                d[palavra] = d.get(palavra, 0) + 1

# Mostra o total somado correspondente ao indice esperado (WORD)
print('A palavra "'+ WORD + '" aparece %s vezes.' %d[WORD])


