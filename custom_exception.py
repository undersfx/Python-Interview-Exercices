class NotMyName(Exception):
	def __init__(self,*args,**kwargs):
		Exception.__init__(self,*args,**kwargs)

def TestaNome(nome):
	if nome.lower() != 'thiago':
		raise NotMyName
	else:
		return True

while True:
	nome = input('Qual o meu nome ?\n')

	if TestaNome(nome):
		print('Sucesso!')
		break