from tkinter import *

votos_char, votos_char2, votos_char3 = 0, 0, 0  # Declarando as variáveis


def verificar_voto():
    global votos_char, votos_char2, votos_char3  # Declarando como globais para utilização dentor da função
    if nome.get() in lista:
        print(f'\n\033[31m{nome.get()} recebeu um voto!!!\033[m\n')  # Pegando o resultado do nome com o .get()
        print('\033[97m—\033[m' * 27)
        if nome.get() == character:
            global votos_char
            votos_char += 1
        elif nome.get() == character2:
            global votos_char2
            votos_char2 += 1
        elif nome.get() == character3:
            global votos_char3
            votos_char3 += 1
        else:
            print('Este personagem não foi escolhido...')
        print(f'\033[32mTotal de votos em {character}\033[m: \033[35m{votos_char}\033[m\n'
              f'\033[33mTotal de votos em {character2}\033[m: \033[35m{votos_char2}\033[m\n'
              f'\033[34mTotal de votos em {character3}\033[m: \033[35m{votos_char3}\033[m')
        print('\033[97m—\033[m' * 27)


janela = Tk()  # Inicializando

cor = '#FAF1F3'
cor2 = '#3970FA'
cor3 = '#05191D'

# Personagens:

character = str(input('Informe o nome do personagem: '))
character2 = str(input('Informe o nome de outro personagem: '))
character3 = str(input('Informe o nome de mais um personagem: '))

lista = [f'{character}', f'{character2}', f'{character3}']

titulo = str(input('\nInforme o título da janela: '))

janela.title(f'{titulo}')  # Título

altura = int(input('\nInfome a altura da janela: '))
largura = int(input('Informe a largura da janela: '))

janela.geometry(f'{altura}x{largura}')  # Dimensões

janela.configure(background=cor)  # Cor de Fundo

Label(janela, text='Digite em que você irá votar: ', background=cor, foreground=cor2, anchor=W).place(x=10, y=10,
                                                                                                      width=300,
                                                                                                      height=20)

nome = Entry(janela)  # Espaço para digitar
nome.place(x=10, y=30, width=200, height=20)

Label(janela, text=f'{character}', background=cor, foreground=cor3, anchor=W).place(x=10, y=60, width=300, height=20)
Label(janela, text=f'{character2}', background=cor, foreground=cor3, anchor=W).place(x=10, y=90, width=300, height=20)
Label(janela, text=f'{character3}', background=cor, foreground=cor3, anchor=W).place(x=10, y=120, width=300, height=20)


# Podemos usar o Text no lugar do Entry se quisermos colocar mais de uma linha (multilinha)

# Botão:

bt = Button(janela, text="Votar", command=verificar_voto)
bt.place(x=200, y=260, width=100, height=20)

janela.mainloop()  # Mostrando a janela
