print('—' * 18, '\033[31mCORES TERMINAL AVANÇADO\033[m', '—' * 18, '\n')
videogame = 'Playstation 4'
valor = float(input('Informe o valor do Playstation 4: '))
opcoes = {'finalizar': '\033[m', 'Roxo': '\033[35m', 'Vermelho': '\033[31m', 'Cinza': '\033[37m', 'Branco': '\033[30m'}
# Lista de opções acima
# Finalizar recebe apenas a última parte do código de cores
print(f"\nO {opcoes['Cinza']}{videogame}{opcoes['finalizar']} está em Cinza e temos o seu valor em Vermelho: "
      f"{opcoes['Vermelho']}{valor}{opcoes['finalizar']}\n")

print('\033[33m—\033[m' * 80)
