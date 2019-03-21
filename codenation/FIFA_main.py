# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv

# Parse do arquivo CSV
with open('FIFA_data.csv', encoding='utf-8') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	# Lista de OrderedDicts que será usada nos calculos
	lista = [line for line in csv_reader]

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
	# set_nationality = set()

	# for line in lista:
	# 	set_nationality.add(line['nationality'])

	# Comprehension:
	set_nationality = {line['nationality'] for line in lista}

	return len(set_nationality)

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
	# set_club = set()

	# for line in lista:
	# 	set_club.add(line['club'])

	# Comprehension:
	set_club = {line['club'] for line in lista}

	return len(set_club)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
	# names = []
	
	# i = 0

	# while i < 20:
	# 	names.append(lista[i]['full_name'])
	# 	i += 1

	# Comprehension:
	names = [name['full_name'] for name in lista[:20]]

	return names

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
	orden_by_wage = sorted(lista, key=lambda x: float(x['eur_wage']), reverse=True)

	# top10 = []
	# for player in orden_by_wage[0:10]:
	# 	top10.append(player['full_name'])

	# Comprehension:
	top10 = [player['full_name'] for player in orden_by_wage[0:10]]

	return top10

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
	orden_by_age = sorted(lista, key=lambda x: float(x['age']), reverse=True)

	# top10 = []
	# for player in orden_by_age[0:10]:
	# 	top10.append(player['full_name'])

	# Comprehension:
	top10 = [player['full_name'] for player in orden_by_age[0:10]]

	return top10

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
	idades = {}

	for line in lista:
		if int(line['age']) not in idades.keys():
			idades[int(line['age'])] = 1
		else:
			idades[int(line['age'])] += 1

	return idades

# DEBUG:
if __name__ == '__main__':
	print(q_1())
	print(q_2())
	print(q_3())
	print(q_4())
	print(q_5())
	print(q_6())
