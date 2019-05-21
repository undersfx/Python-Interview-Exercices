'''
Exercício:

- Realizar requisição de parâmetro para https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

- Parsear e escrever o retorno da APT em um arquivo answer.json; Exemplo de retorno:
{
	"numero_casas": 10,
	"token":"token_do_usuario",
	"cifrado": "texto criptografado",
	"decifrado": "aqui vai o texto decifrado",
	"resumo_criptografico": "aqui vai o resumo"
}

- Decifrar o texto no campo "cifrado" com base a criptografia de cesar;

- Criar o resumo criptográgico da string decifrada com algoritimo SHA1 e passa-lo no campo "resumo_criptografico"

- Realizar requisição post com o JSON atualizado como multipart/form-data para https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN
'''

import requests # Requisição GET e POST
import string # Letras em string.ascii_letters
import hashlib # Criar SHA1 Digest
import sys # Token como argumento pela linha de comando
import json # Parsear resposta da API
import pprint


# Validação para argumento token no linha de comando:
if len(sys.argv) > 1:
    TOKEN = sys.argv[1]
else:
    raise RuntimeError('É necessário ao menos o argumento TOKEN')

# Requisição GET a API
API_ENDPOINT = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='

r = requests.get(f'{API_ENDPOINT}{TOKEN}')

# Parsing do JSON em um dict
data = json.loads(r.text)

# Função para decifrar letras
def decifra(letra, casas):
    if (ord(letra) - casas) < 97:
        return chr(ord(letra) - casas + 26)
    else:
        return chr(ord(letra) - casas)

decifrado = ''

# Decifra a palavra do JSON
for letra in data['cifrado']:
    # if letra in 'Â':
    #     decifrado += '' #'¸'
    #     continue
    if letra in string.ascii_letters:
        decifrado += decifra(letra, data['numero_casas'])
    else:
        decifrado += letra

data['decifrado'] = decifrado

# Cria resumo criptográfico
h = hashlib.sha1()
h.update(decifrado.encode())
data['resumo_criptografico'] = h.hexdigest()

# DEBUG:
pprint.pprint(data)

# Escreve o conteúdo no arquivo JSON
json.dump(data, open('answer.json', 'w'))

# Requisição POST a API
answer = {'answer': open('answer.json', 'rb')}
r = requests.post(f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={TOKEN}', files=answer)

print(f'\nStatus Code: {r.status_code}')
pprint.pprint(r.text)