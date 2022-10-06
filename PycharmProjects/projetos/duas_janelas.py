import tkinter as tk

# Interação com o usuário:

escolha_titulo = str(input('Escolha o título da segunda janela: '))
x = int(input('Informe o valor para tamanho do eixo X: '))
y = int(input('Informe o valor para tamanho do eixo Y: '))
ix = int(input('Informe o valor para o tamanho do título no eixo X: '))
iy = int(input('Informe o valor para o tamanho do título no eixo Y: '))


def abrir_outra_janela():  # Função para criar outra janela apartir do botão da 1 janela
    segunda_janela = tk.Toplevel(padx=f'{x}', pady=f'{y}')  # Sempre que quiser múltiplas janelas, usar o tk.Toplevel()
    # Tamanho:(padx=, pady=)
    segunda_janela.title('Janela')
    label_nome = tk.Label(segunda_janela, background='green', text=f"{escolha_titulo}")
    label_nome.grid(row=0, column=0, ipadx=f'{ix}', ipady=f'{iy}')
    botao_voltar = tk.Button(segunda_janela, border=4, text='Fechar a janela 2', command=segunda_janela.destroy)
    botao_voltar.grid(row=1, column=0)


janela = tk.Tk()  # Janela principal

botao = tk.Button(janela, text='Ir para nova janela', command=abrir_outra_janela)
botao.grid(row=0, column=0)  # Botão da 1° janela

janela.mainloop()  # Começar a trabalhar a janela
