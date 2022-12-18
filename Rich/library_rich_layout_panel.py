from rich.layout import Layout
from rich import print as print
from rich.panel import Panel

# Layout:

escolha = str(input('Escolha o nome do app: ')).upper()
criador = str(input('\nInforme o nome do criador: '))
cor = str(input('\nEscolha uma cor em inglês: '))
cor2 = str(input('\nEscolha outra cor em inglês: '))
texto = 'on ' + cor
painel = str(input('\nInforme o nome do painel 1: '))
painel2 = str(input('\nInforme o nome do painel 2: '))

layout = Layout()  # Inicializando o layout
layout.split_column(
    Layout(Panel(f'{escolha}', style=f'{texto}'), ratio=3),  # Ratio: Percentual de quanto vai estar ocupando no painel
    Layout(name='Cima', ratio=2),  # Ratio: Percentual de quanto vai estar ocupando no layout
    Layout(name='Baixo', ratio=2),  # Ratio: Percentual de quanto vai estar ocupando no layout
    Layout(Panel(f'Criador: {criador}', style=f'{cor2}'), ratio=3),  # Ratio:  Percentual de quanto vai estar ocupando no painel
)

layout['Cima'].split_row(  # Separando o em dois painéis
    Layout(Panel(f'{painel}')),
    Layout(Panel(f'{painel2}')),
)

print(layout)
