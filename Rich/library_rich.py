from rich import print as print


x = float(input('\nInforme o valor de x: '))
y = float(input('Informe o valor de y: '))

print(f'\nA soma de {x} + {y} é [red]{x + y}[/]')

print(f'\nA subtração de {x} - {y} é [green]{x - y}[/]')

nome = str(input('\nInforme um nome: '))

print(f'\nO nome digitado em negrito: [bold]{nome}[/]')
print(f'\nO nome digitado em sublinhado: [underline]{nome}[/]')
