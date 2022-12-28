import sqlite3

nome = str(input('Informe o nome do banco de dados: '))

nomedb = nome + ".db"

conexao = sqlite3.connect(f"{nomedb}")  # Inicializando:
# Você pode escolher o nome para iniciar mas os comandos abaixo não conseguem utilizar a varíavel,
# então antes de iniciar, coloque os nomes abaixo no lugar de "teams"

# Cursor Object:
cursor = conexao.cursor()

cursor.execute("create table teams (goals integer, name text, city text)")  # Comandos para criar a tabela

print()

# Base de dados:

lista_times = [
    (3, "Flamengo", "Rio de Janeiro"),
    (1, "Vasco", "Rio de Janeiro"),
    (3, "Santos", "São Paulo"),
    (1, "Corinthias", "São Paulo"),
    (3, "Grêmio", "Rio Grande do Sul"),
    (2, "Internacional", "Rio Grande do Sul"),
    (2, "Cruzeiro", "Minas Gerais"),
    (1, "Atlético-MG", "Minas Gerais"),
]

# Colocando no BD:
cursor.executemany("insert into teams values (?,?,?)", lista_times)

# print linhas da base de dados:
for row in cursor.execute(f"select * from teams"):
    print(f'\033[31m{row}\033[m')

# print linhas específicas:
print()
filtro = str(input('Informe o nome de uma cidade dos times acima: '))
cursor.execute("select * from teams where city=:c", {"c": f"{filtro}"})
teams_search = cursor.fetchall()
print(teams_search)

# Nova tabela:

cursor.execute("create table cidades (city text, capital text)")
cursor.execute("insert into cidades values (?,?)", ("Rio Grande do Sul", "Porto Alegre"))
cursor.execute("select * from cidades where city=:c", {"c": "Rio Grande do Sul"})
capital_search = cursor.fetchall()
print(capital_search)

# Manipulando database:
print()
for i in teams_search:
    ajuste = [capital_search[0][1] if value == capital_search[0][0] else value for value in i]
    print(ajuste)

conexao.close()  # Finalizando
