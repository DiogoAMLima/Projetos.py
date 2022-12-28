import random
from sty import fg


def generate_rgb():
    red = random.randint(0, 256)  # Gerando um número para código RGB
    green = random.randint(0, 256)  # Gerando um número para código RGB
    blue = random.randint(0, 256)  # Gerando um número para código RGB
    return red, green, blue  # Retornando o código gerado


# print(red, green, blue)  # Visualizando os números aleatórios (código RGB)


def generate_color(red, green, blue):
    return fg(red, green, blue)  # Usando fg da library sty (paletas de cores para os códigos)


esc = int(input('Informe quantas vezes deseja ver uma nova cor: '))
a = float(input('\nInfomre um valor: '))
b = float(input('\nInfomre outro valor: '))
print()

for i in range(0, esc):
    red, green, blue = generate_rgb()  # Atribuindo os valores gerados a função
    colour = generate_color(red, green, blue)  # Varíavel para nova função que usa a library sty
    print(colour, "Gerando cores automaticamente")

print()

for i in range(0, esc):
    red, green, blue = generate_rgb()
    colour = generate_color(red, green, blue)
    print(colour, f'A soma entre {a} e {b} é: {a+b:.2f}')  # Soma dos valores escolhidos com cores aleatórias
