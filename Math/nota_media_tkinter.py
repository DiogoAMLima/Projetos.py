from tkinter import *

janela = Tk()  # Inicializando a janela

try:  # Tratamento de erros
    # Interação com o/a usuário(a) para escolhas de título, dimensões, cores e etc

    titulo = str(input('Informe o título da janela: '))

    janela.title(f"{titulo}")

    w = int(input('\nInforme a largura da tela: '))
    h = int(input('\nInforme a altura da tela: '))

    janela.geometry(f"{w}x{h}")

    style = str(input('\nInforme o estilo da fonte: '))  # (normal, bold, italic, romam)

    tamanho_fonte = str(input('\nInforme o tamanho da fonte: '))

    cor1 = str(input('\nInforme a cor em inglês para a soma: '))

    cor2 = str(input('\nInforme a cor em inglês para a média: '))

    cor3 = str(input('\nInforme a cor em inglês para a mensagem final: '))


    def Calculate_avg():  # Inicializando a função
        n = float(nota_entry.get())  # Pegando o valor da nota
        n2 = float(nota2_entry.get())  # Pegando o valor da nota2
        n3 = float(nota3_entry.get())  # Pegando o valor da not3
        s = n + n2 + n3  # Soma
        Label(text=f"{s}", font=f"arial {tamanho_fonte} {style}", fg=f"{cor1}").place(x=250, y=190)
        # Colocando o valor da soma na janela

        average = float(s / 3)  # Média
        Label(text=f"{average:.2f}", font=f"arial {tamanho_fonte} {style}", fg=f"{cor2}").place(x=250, y=230)
        # Colocando o valor da média na janela

        # Condicionais para o resultado da média

        if average > 10:
            status = "VALORES MUITO ALTOS"
        elif average >= 7:
            status = "APROVADO"
        elif average >= 5:
            status = "EM RECUPERAÇÃO"
        else:
            status = "REPROVADO"

        Label(text=f"{status}", font=f"arial {tamanho_fonte} {style}", fg=f"{cor3}").place(x=250, y=270)
        # Colocando o status na janela


    def clear():  # Inicializando a função clear que serve para limpar os valores / dados da janela
        n = float(nota_entry.get())
        n2 = float(nota2_entry.get())
        n3 = float(nota3_entry.get())
        s = n + n2 + n3
        Label(text=f"                        ", font=f"arial {tamanho_fonte} {style}", fg=f"{cor1}").place(x=250, y=190)

        average = float(s / 3)
        Label(text=f"                        ", font=f"arial {tamanho_fonte} {style}", fg=f"{cor2}").place(x=250, y=230)

        if average > 10:
            status = "                                                                                      "
        elif average >= 7:
            status = "                                                                                      "
        elif average >= 5:
            status = "                                                                                      "
        else:
            status = "                                                                                      "

        Label(text=f"{status}", font=f"arial {tamanho_fonte} {style}", fg=f"{cor3}").place(x=250, y=270)

    # Criando os textos que ficarão na janela:

    nota = Label(janela, text="Nota 1:", font="arial 11")
    nota2 = Label(janela, text="Nota 2:", font="arial 11")
    nota3 = Label(janela, text="Nota 3:", font="arial 11")
    soma = Label(janela, text="Soma:", font="arial 11")
    media = Label(janela, text="Média:", font="arial 11")
    situacao = Label(janela, text="Situação:", font="arial 11")

    # Posicionando os textos:
    nota.place(x=50, y=20)
    nota2.place(x=50, y=70)
    nota3.place(x=50, y=120)
    soma.place(x=50, y=190)
    media.place(x=50, y=230)
    situacao.place(x=50, y=270)

    # Declarando as variáveis:
    nota_value = StringVar()
    nota2_value = StringVar()
    nota3_value = StringVar()

    # Criando as entrys para notas:
    nota_entry = Entry(janela, textvariable=nota_value, font="arial 14", width=13)
    nota2_entry = Entry(janela, textvariable=nota2_value, font="arial 14", width=13)
    nota3_entry = Entry(janela, textvariable=nota3_value, font="arial 14", width=13)

    # Posicionando as entrys:
    nota_entry.place(x=250, y=20)
    nota2_entry.place(x=250, y=70)
    nota3_entry.place(x=250, y=120)

    # Criando os botões:
    Button(text="Calcular Média", font="arial 15", bg="white", bd=10, command=Calculate_avg).place(x=50, y=350)
    Button(text="Clear", font="arial 15", bg="white", bd=10, command=clear).place(x=240, y=350)
    Button(text="Exit", font="arial 15", bg="white", bd=10, width=8, command=lambda: exit()).place(x=350, y=350)

    janela.mainloop()  # Finalizando a janela

except (TypeError, ValueError):
    print('\n\033[35mTivemos um problema com o tipo de valor digitado...\033[m')
