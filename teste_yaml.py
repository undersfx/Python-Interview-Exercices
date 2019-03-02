import yaml

with open('teste_yaml.yml', mode='r') as f:
    dados = yaml.load(f.read())

print(type(dados))
print(dados)
