from palavras import (frances_A, portugues_A, frances_B, portugues_B, frances_C, portugues_C, frances_D, portugues_D,
                      frances_E, portugues_E, frances_F, portugues_F, frances_G, portugues_G, frances_H, portugues_H,
                      frances_I, portugues_I, frances_J, portugues_J, frances_K, portugues_K, frances_L, portugues_L,
                      frances_M, portugues_M, frances_N, portugues_N, frances_O, portugues_O, frances_P, portugues_P,
                      frances_Q, portugues_Q, frances_R, portugues_R, frances_S, portugues_S, frances_T, portugues_T,
                      frances_U, portugues_U, frances_V, portugues_V, frances_W, portugues_W, frances_X, portugues_X,
                      frances_Y, portugues_Y, frances_Z, portugues_Z)
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter
from tkinter import *
from tkinter import messagebox, ttk
from gtts import gTTS
import os
import gtts
from playsound import playsound

window = Tk()
window.title('Window')
window.geometry('790x680')

window.resizable(False, False)


lista_cor = ['#FAF1F3', '#3970FA', '#3fb5a3', '#ff0000', '#DACB0F', '#EF4135', '#000000', '#836FFF', '#FF00FF',
             '#8B4513', '#008000', '#1C1C1C', '#A9A9A9', '#483D8B', '#0000CD', '#4682B4', '#708090', '#ADD8E6',
             '#008B8B', '#228B22', '#808000', '#D2691E', '#0055A4', '#8B0000', '#FFFF00', '#A52A2A', '#FFFFFF']

lista_nomes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

lista_qntd = [len(frances_A), len(frances_B), len(frances_C), len(frances_D), len(frances_E), len(frances_F),
              len(frances_G), len(frances_H), len(frances_I), len(frances_J), len(frances_K), len(frances_L),
              len(frances_M), len(frances_N), len(frances_O), len(frances_P), len(frances_Q), len(frances_R),
              len(frances_S), len(frances_T), len(frances_U), len(frances_V), len(frances_W), len(frances_X),
              len(frances_Y), len(frances_Z)]

window.configure(background=lista_cor[1])

pontos = 0

(indice, indice2, indice3, indice4, indice5, indice6, indice7, indice8, indice9, indice10, indice11, indice12, indice13,
 indice14, indice15, indice16, indice17, indice18, indice19, indice20, indice21, indice22, indice23, indice24, indice25,
 indice26) = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1


def selecionar_resposta(_):
    global indice
    item = opcoes.get()
    indice = frances_A.index(item)
    # print(indice)
    exibicao.config(text=f"{item}")
    return indice


def selecionar_resposta2(_):
    global indice2
    item2 = opcoes2.get()
    indice2 = frances_B.index(item2)
    # print(indice2)
    exibicao.config(text=f"{item2}")
    return indice2


def selecionar_resposta3(_):
    global indice3
    item3 = opcoes3.get()
    indice3 = frances_C.index(item3)
    # print(indice3)
    exibicao.config(text=f"{item3}")
    return indice3


def selecionar_resposta4(_):
    global indice4
    item4 = opcoes4.get()
    indice4 = frances_D.index(item4)
    # print(indice4)
    exibicao.config(text=f"{item4}")
    return indice4


def selecionar_resposta5(_):
    global indice5
    item5 = opcoes5.get()
    indice5 = frances_E.index(item5)
    # print(indice5)
    exibicao.config(text=f"{item5}")
    return indice5


def selecionar_resposta6(_):
    global indice6
    item6 = opcoes6.get()
    indice6 = frances_F.index(item6)
    # print(indice6)
    exibicao.config(text=f"{item6}")
    return indice6


def selecionar_resposta7(_):
    global indice7
    item7 = opcoes7.get()
    indice7 = frances_G.index(item7)
    # print(indice7)
    exibicao.config(text=f"{item7}")
    return indice7


def selecionar_resposta8(_):
    global indice8
    item8 = opcoes8.get()
    indice8 = frances_H.index(item8)
    # print(indice8)
    exibicao.config(text=f"{item8}")
    return indice8


def selecionar_resposta9(_):
    global indice9
    item9 = opcoes9.get()
    indice9 = frances_I.index(item9)
    # print(indice9)
    exibicao.config(text=f"{item9}")
    return indice9


def selecionar_resposta10(_):
    global indice10
    item10 = opcoes10.get()
    indice10 = frances_J.index(item10)
    # print(indice10)
    exibicao.config(text=f"{item10}")
    return indice10


def selecionar_resposta11(_):
    global indice11
    item11 = opcoes11.get()
    indice11 = frances_K.index(item11)
    # print(indice11)
    exibicao.config(text=f"{item11}")
    return indice11


def selecionar_resposta12(_):
    global indice12
    item12 = opcoes12.get()
    indice12 = frances_L.index(item12)
    # print(indice12)
    exibicao.config(text=f"{item12}")
    return indice12


def selecionar_resposta13(_):
    global indice13
    item13 = opcoes13.get()
    indice13 = frances_M.index(item13)
    # print(indice13)
    exibicao.config(text=f"{item13}")
    return indice13


def selecionar_resposta14(_):
    global indice14
    item14 = opcoes14.get()
    indice14 = frances_N.index(item14)
    # print(indice14)
    exibicao.config(text=f"{item14}")
    return indice14


def selecionar_resposta15(_):
    global indice15
    item15 = opcoes15.get()
    indice15 = frances_O.index(item15)
    # print(indice15)
    exibicao.config(text=f"{item15}")
    return indice15


def selecionar_resposta16(_):
    global indice16
    item16 = opcoes16.get()
    indice16 = frances_P.index(item16)
    # print(indice16)
    exibicao.config(text=f"{item16}")
    return indice16


def selecionar_resposta17(_):
    global indice17
    item17 = opcoes17.get()
    indice17 = frances_Q.index(item17)
    # print(indice17)
    exibicao.config(text=f"{item17}")
    return indice17


def selecionar_resposta18(_):
    global indice18
    item18 = opcoes18.get()
    indice18 = frances_R.index(item18)
    # print(indice18)
    exibicao.config(text=f"{item18}")
    return indice18


def selecionar_resposta19(_):
    global indice19
    item19 = opcoes19.get()
    indice19 = frances_S.index(item19)
    # print(indice19)
    exibicao.config(text=f"{item19}")
    return indice19


def selecionar_resposta20(_):
    global indice20
    item20 = opcoes20.get()
    indice20 = frances_T.index(item20)
    # print(indice20)
    exibicao.config(text=f"{item20}")
    return indice20


def selecionar_resposta21(_):
    global indice21
    item21 = opcoes21.get()
    indice21 = frances_U.index(item21)
    # print(indice21)
    exibicao.config(text=f"{item21}")
    return indice21


def selecionar_resposta22(_):
    global indice22
    item22 = opcoes22.get()
    indice22 = frances_V.index(item22)
    # print(indice22)
    exibicao.config(text=f"{item22}")
    return indice22


def selecionar_resposta23(_):
    global indice23
    item23 = opcoes23.get()
    indice23 = frances_W.index(item23)
    # print(indice23)
    exibicao.config(text=f"{item23}")
    return indice23


def selecionar_resposta24(_):
    global indice24
    item24 = opcoes24.get()
    indice24 = frances_X.index(item24)
    # print(indice24)
    exibicao.config(text=f"{item24}")
    return indice24


def selecionar_resposta25(_):
    global indice25
    item25 = opcoes25.get()
    indice25 = frances_Y.index(item25)
    # print(indice25)
    exibicao.config(text=f"{item25}")
    return indice25


def selecionar_resposta26(_):
    global indice26
    item26 = opcoes26.get()
    indice26 = frances_Z.index(item26)
    # print(indice26)
    exibicao.config(text=f"{item26}")
    return indice26


def grafico():
    plt.bar(lista_nomes, lista_qntd, color=lista_cor, label='Quantidade de palavras por letras', width=0.75)
    plt.grid(False)
    plt.title('GRÁFICO', color=lista_cor[5])
    plt.legend()
    plt.show()


def pontuacao():
    # messagebox.showinfo(title='POINTS', message=f'You have {pontos} points')
    res_window = customtkinter.CTk()
    res_window.geometry('170x110')
    res_window.resizable(False, False)
    customtkinter.set_appearance_mode("Dark")
    customtkinter.CTkLabel(master=res_window, text=f'YOU HAVE {pontos} POINT(S)', width=30, height=15,
                           fg_color=lista_cor[3], corner_radius=10).place(x=15, y=30)
    res_window.mainloop()


def ouvir_palavra():
    resposta2 = resEntry2.get()
    language = 'fr'
    speech = gTTS(text=resposta2, lang=language, slow=True)
    print(resposta2)
    speech.save("text_speech.mp3")
    os.system("text_speech.mp3")


def confirmar():
    global pontos
    resposta = resEntry.get()
    if (resposta == portugues_A[indice] or resposta == portugues_B[indice2] or resposta == portugues_C[indice3]
        or resposta == portugues_D[indice4] or resposta == portugues_E[indice5]
        or resposta == portugues_F[indice6] or resposta == portugues_G[indice7]
        or resposta == portugues_H[indice8] or resposta == portugues_I[indice9]
        or resposta == portugues_J[indice10] or resposta == portugues_K[indice11]
        or resposta == portugues_L[indice12] or resposta == portugues_M[indice13]
        or resposta == portugues_N[indice14] or resposta == portugues_O[indice15]
        or resposta == portugues_P[indice16] or resposta == portugues_Q[indice17]
        or resposta == portugues_R[indice18] or resposta == portugues_S[indice19]
        or resposta == portugues_T[indice20] or resposta == portugues_U[indice21]
        or resposta == portugues_V[indice22] or resposta == portugues_W[indice23]
        or resposta == portugues_X[indice24] or resposta == portugues_Y[indice25]
        or resposta == portugues_Z[indice26]):
        pontos += 1
        messagebox.showinfo(title='CONGRATS', message='CONGRATULATIONS, YOU EARNED 1 POINT')
    else:
        pontos -= 1
        messagebox.showinfo(title='TOO BAD', message='TOO BAD, YOU LOST 1 POINT')


opcoes = ttk.Combobox(window, values=frances_A)
opcoes.bind("<<ComboboxSelected>>", selecionar_resposta)
opcoes.set("--------------------------")
opcoes.place(x=20, y=20)

opcoes2 = ttk.Combobox(window, values=frances_B)
opcoes2.bind("<<ComboboxSelected>>", selecionar_resposta2)
opcoes2.set("--------------------------")
opcoes2.place(x=170, y=20)

opcoes3 = ttk.Combobox(window, values=frances_C)
opcoes3.bind("<<ComboboxSelected>>", selecionar_resposta3)
opcoes3.set("--------------------------")
opcoes3.place(x=320, y=20)

opcoes4 = ttk.Combobox(window, values=frances_D)
opcoes4.bind("<<ComboboxSelected>>", selecionar_resposta4)
opcoes4.set("--------------------------")
opcoes4.place(x=470, y=20)

opcoes5 = ttk.Combobox(window, values=frances_E)
opcoes5.bind("<<ComboboxSelected>>", selecionar_resposta5)
opcoes5.set("--------------------------")
opcoes5.place(x=620, y=20)

opcoes6 = ttk.Combobox(window, values=frances_F)
opcoes6.bind("<<ComboboxSelected>>", selecionar_resposta6)
opcoes6.set("--------------------------")
opcoes6.place(x=20, y=50)

opcoes7 = ttk.Combobox(window, values=frances_G)
opcoes7.bind("<<ComboboxSelected>>", selecionar_resposta7)
opcoes7.set("--------------------------")
opcoes7.place(x=170, y=50)

opcoes8 = ttk.Combobox(window, values=frances_H)
opcoes8.bind("<<ComboboxSelected>>", selecionar_resposta8)
opcoes8.set("--------------------------")
opcoes8.place(x=320, y=50)

opcoes9 = ttk.Combobox(window, values=frances_I)
opcoes9.bind("<<ComboboxSelected>>", selecionar_resposta9)
opcoes9.set("--------------------------")
opcoes9.place(x=470, y=50)

opcoes10 = ttk.Combobox(window, values=frances_J)
opcoes10.bind("<<ComboboxSelected>>", selecionar_resposta10)
opcoes10.set("--------------------------")
opcoes10.place(x=620, y=50)

opcoes11 = ttk.Combobox(window, values=frances_K)
opcoes11.bind("<<ComboboxSelected>>", selecionar_resposta11)
opcoes11.set("--------------------------")
opcoes11.place(x=20, y=80)

opcoes12 = ttk.Combobox(window, values=frances_L)
opcoes12.bind("<<ComboboxSelected>>", selecionar_resposta12)
opcoes12.set("--------------------------")
opcoes12.place(x=170, y=80)

opcoes13 = ttk.Combobox(window, values=frances_M)
opcoes13.bind("<<ComboboxSelected>>", selecionar_resposta13)
opcoes13.set("--------------------------")
opcoes13.place(x=320, y=80)

opcoes14 = ttk.Combobox(window, values=frances_N)
opcoes14.bind("<<ComboboxSelected>>", selecionar_resposta14)
opcoes14.set("--------------------------")
opcoes14.place(x=470, y=80)

opcoes15 = ttk.Combobox(window, values=frances_O)
opcoes15.bind("<<ComboboxSelected>>", selecionar_resposta15)
opcoes15.set("--------------------------")
opcoes15.place(x=620, y=80)

opcoes16 = ttk.Combobox(window, values=frances_P)
opcoes16.bind("<<ComboboxSelected>>", selecionar_resposta16)
opcoes16.set("--------------------------")
opcoes16.place(x=20, y=110)

opcoes17 = ttk.Combobox(window, values=frances_Q)
opcoes17.bind("<<ComboboxSelected>>", selecionar_resposta17)
opcoes17.set("--------------------------")
opcoes17.place(x=170, y=110)

opcoes18 = ttk.Combobox(window, values=frances_R)
opcoes18.bind("<<ComboboxSelected>>", selecionar_resposta18)
opcoes18.set("--------------------------")
opcoes18.place(x=320, y=110)

opcoes19 = ttk.Combobox(window, values=frances_S)
opcoes19.bind("<<ComboboxSelected>>", selecionar_resposta19)
opcoes19.set("--------------------------")
opcoes19.place(x=470, y=110)

opcoes20 = ttk.Combobox(window, values=frances_T)
opcoes20.bind("<<ComboboxSelected>>", selecionar_resposta20)
opcoes20.set("--------------------------")
opcoes20.place(x=620, y=110)

opcoes21 = ttk.Combobox(window, values=frances_U)
opcoes21.bind("<<ComboboxSelected>>", selecionar_resposta21)
opcoes21.set("--------------------------")
opcoes21.place(x=20, y=140)

opcoes22 = ttk.Combobox(window, values=frances_V)
opcoes22.bind("<<ComboboxSelected>>", selecionar_resposta22)
opcoes22.set("--------------------------")
opcoes22.place(x=170, y=140)

opcoes23 = ttk.Combobox(window, values=frances_W)
opcoes23.bind("<<ComboboxSelected>>", selecionar_resposta23)
opcoes23.set("--------------------------")
opcoes23.place(x=320, y=140)

opcoes24 = ttk.Combobox(window, values=frances_X)
opcoes24.bind("<<ComboboxSelected>>", selecionar_resposta24)
opcoes24.set("--------------------------")
opcoes24.place(x=470, y=140)

opcoes25 = ttk.Combobox(window, values=frances_Y)
opcoes25.bind("<<ComboboxSelected>>", selecionar_resposta25)
opcoes25.set("--------------------------")
opcoes25.place(x=620, y=140)

opcoes26 = ttk.Combobox(window, values=frances_Z)
opcoes26.bind("<<ComboboxSelected>>", selecionar_resposta26)
opcoes26.set("--------------------------")
opcoes26.place(x=20, y=170)

exibicao = tk.Label(window, text="None")
exibicao.place(x=380, y=260)

Label(window, text='INFORME A TRADUÇÃO DA PALAVRA ESCOLHIDA', background=lista_cor[7], anchor=W).place(x=260, y=315)
Label(window, text='INFORME UMA PALAVRA / FRASE EM FRANCÊS', background=lista_cor[13], anchor=W).place(x=270, y=490)

resValue = StringVar()
resEntry = Entry(window, textvariable=resValue, width=30, bd=3, font=20)

resValue2 = StringVar()
resEntry2 = Entry(window, textvariable=resValue2, width=30, bd=3, font=20)

resEntry.place(x=260, y=360)

resEntry2.place(x=260, y=540)

Button(window, text='CONFIRMAR', background=lista_cor[26], command=confirmar).place(x=355, y=410)

Button(window, text='PONTUAÇÃO', background=lista_cor[22], command=pontuacao).place(x=255, y=410)

Button(window, text='GRÁFICO BAR', background=lista_cor[3], command=grafico).place(x=455, y=410)

Button(window, text='OUVIR PALAVRA', background=lista_cor[2], command=ouvir_palavra).place(x=340, y=600)

window.mainloop()
