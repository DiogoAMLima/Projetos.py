# Dicionário operadores (items, values, keys):

# Exemplo de dicionário:

pessoa = {"Nome": "Diogo", "Idade": 24, "Sexo": "M"}

# Verificando os dados do dicionário:

print(f'\033[32m{pessoa}\033[m\n')

# Vamos adicionar mais um dado ao dict:

pessoa["Peso"] = 55

print(f'\033[33m{pessoa}\033[m\n')

# Verificando todos os dados do dicionário com o .keys():

pessoas = {"Pessoa": ['Nome: Diogo', 'Idade: 24', 'Sexo: M', 'Peso: 55'],
           "Pessoa2": ['Nome: Gabriel', 'Idade: 24', 'Sexo: M', 'Peso: 70'],
           "Pessoa3": ['Nome: João', 'Idade: 24', 'Sexo: M', 85],
           "Pessoa4": ['Nome: Júlia', 'Idade: 22', 'Sexo: F', 'Peso: 67.8']}

for chave in pessoas.keys():
    print(f'\033[34m{pessoas[chave]}\033[m')

print()

# Verificando todos os dados do dicionário com o .values():

notas = {"Nota 1": '7', "Nota 2": '5', "Nota 3": "10"}

print(f'\033[35mNotas: {notas.values()}\033[m\n')

cellphone = {"Celular": "Iphone",
             "Modelo": "8 plus",
             "Data de lançamento": "2017"}

print(f'\033[36mInformações sobre o celular: {cellphone.items()}\033[m')
