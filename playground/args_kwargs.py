# Conteúdo: https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

# ARGS

'''
Uma número de variáveis de argumentos posicionais que podem ser especificadas
Deve usar qualquer identificador, mas args é convencional
args é uma tupla de 0 ou mais objetos
'''
def func(arg1, *args):
	print(args)
	print(type(args))

func(1, 2, 3, 4)

# Output
# (2, 3, 4)
# <class 'tuple'>


# KWARGS

'''
Use **kwargs no final
Deve usar qualquer identificador, mas kwargs é convencional
kwargs é um dicionário de strings para valores
As chaves do kwargs são os nomes dos argumentos
'''

def foo(arg1, **kwargs):
	print(kwargs)
	print(type(kwargs))

foo(1,two=2, three=3)

# Output
# {'two': 2, 'three': 3}
# <class 'dict'>