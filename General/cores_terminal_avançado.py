print('------------------------------------------CORES TERMINAL AVANÇADO------------------------------------------\n')
videogame = 'Playstation 4'
valor = float(input('Informe o valor do Playstation 4: '))
opcoes = {'finalizar': '\033[m', 'Roxo': '\033[35m', 'Vermelho': '\033[31m', 'Cinza': '\033[37m', 'Branco': '\033[30m'}
print("O {}{}{} está em Cinza e temos o seu valor em Vermelho: {}{:.2f}{}"
      .format(opcoes['Cinza'], videogame, opcoes['finalizar'],
              opcoes['Vermelho'], valor, opcoes['finalizar']))
print('\n')

print('-------------------------------------------------------------------------------------------------------------')
