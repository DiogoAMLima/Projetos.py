# Probabilidade:

# Fórmula: P(A) = n(A) / n(S)

# Exemplo 1:

# Qual é a probabilidade de se obter cara no lançamento de uma moeda?

# Espaço Amostral S = {Ca, Co} n(S) = 2
# Seja A o evento “aparecer cara”, então, A é dado por: A = {Ca} e n(A) = 1
# Logo, P(A) = n(A)/n(S) P(A) = ½ = 0,5 ou 50%.

# Interação com o usuário:

dado = [1, 2, 3, 4, 5, 6]
p = 0
dado_num = int(input('Escolha um número do espaço amostral: {1, 2, 3, 4, 5, 6}: '))
if dado_num in dado:
    print('Valor aceito')
    p = 1 / 6
    print(f'A chance desse valor sair é aproximadamente: {p:.2f}')
else:
    print('Este valor não existe no espaço amostral...')

print('\n')

# Dois dados:

espaco_amostral = 36  # (espaço amostral com dois dados)

# Qual a chance de em um lançamento de dois dados aparecer pelo menos um núemro 5?

# Temos as combinações dos dados [{1,5} {2,5} {3,5} {4,5} {5,1} {5,2} {5,3} {5,4} {5,5} {5,6} {6,5}] = 11

p2 = 11 / espaco_amostral
print(f'A probabilidade é de aproximadamente: {p2:.2f}')

print('\n')

# Pergunta ao usuário:

print('Numa urna existem 100 bolas distribuidas a seguir:\n')
print('Cor e N° de bolas: ')
print('Azul:      40')
print('Vermelha:  30')
print('Laranja:   20')
print('Verde:     10')
print('Total:     100\n')

# Qual a probabilidade de retirarmos da caixa uma bola azul ou verde?

print('\033[31mA seguir, a fórmula para o cálculo...\033[m\n')
print('\033[32mP = (Número de bolas azuis + Números de bolas verdes) / espaço amostral = 100\033[m\n')
resp = int(input('Qual a probabilidade de retirarmos da caixa uma bola azul ou verde? '))
if resp == 50:
    print(f'Parabéns você acertou!!! A resposta é \033[34m{resp}%\033[m')
else:
    print('\n\033[35mQue pena, tente novamente...\033[m')
