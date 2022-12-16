from rich.table import Table
from rich import print as print
from rich.console import Console

# Tabelas:

# Iniciando o console: 
console = Console()

cor = str(input('Escolha uma cor em inglês para a coluna Movie: '))
cor2 = str(input('\nEscolha uma cor em inglês para a coluna Release date: '))
cor3 = str(input('\nEscolha uma cor em inglês para a coluna Box office: '))


i = 0

table = Table(title='Filmes Favoritos')
table.add_column('Name', justify='left', style=f'{cor}')
table.add_column('Release Date ', style=f'{cor2}')
table.add_column('Box Office', style=f'{cor3}')

for i in range(4):
    movie = str(input('\nInforme o nome do filme: '))
    release_date = int(input('\nInforme a data de lançamento: '))
    box_office = float(input('\nInforme o faturamento do filme: '))
    table.add_row(f'{movie}', f'{release_date}', f'R$ {box_office}')

console.print(table)
