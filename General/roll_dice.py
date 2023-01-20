from tkinter import *
import random

janela = Tk()

try:
    w = int(input('Informe a largura da tela: '))
    h = int(input('\nInforme a altura da tela: '))

    janela.geometry(f"{w}x{h}")

    tlt = str(input('\nInforme o título da janela: '))

    janela.title(f"{tlt}")

    posicaoX = int(input('\nInforme o padx: '))
    posicaoY = int(input('\nInforme o pady: '))

    cor = str(input('\nInforme a cor de fundo do button em inglês: ')).strip().lower()

    cor2 = str(input('\nInforme a cor de fundo da tela em inglês: ')).strip().lower()

    label = Label(janela, text='', font=("Arial", 260))

    esc = int(input('\nInforme um número entre 1 e 3: '))


    def roll():
        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        if esc == 1:
            label.configure(text=f'{random.choice(dice)}', bg=f'{cor2}')
            label.pack()
        elif esc == 2:
            label.configure(text=f'{random.choice(dice)}{random.choice(dice)}', bg=f'{cor2}')
            label.pack()
        elif esc == 3:
            label.configure(text=f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}', bg=f'{cor2}')
            label.pack()
        else:
            print('\n\033[31mTente de novo...\033[m')


    button = Button(janela, text="Roll the dice(s)", width=40, height=5, font=10, bg=f'{cor}', bd=2, command=roll)

    button.pack(padx=posicaoX, pady=posicaoY)

    janela.mainloop()

except (TypeError, ValueError):
    print('\n\033[35mTivemos um problema com o tipo de valor digitado...\033[m')

