from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

janela = Tk()

lista_cor = ['#FAF1F3', '#3970FA', '#3fb5a3', '#ff0000', '#DACB0F', '#FFA500', '#000000', '#836FFF', '#FF00FF',
             '#8B4513', '#008000']

voto, voto2, voto3, voto4, voto5, voto6, voto7, voto8, voto9, voto10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


def verificar_voto():
    global voto
    voto += 1
    label.config(text=f"{voto}")
    if voto >= 10:
        messagebox.showinfo(title='Ten', message=f'Luffy has {voto} votes')


def verificar_voto2():
    global voto2
    voto2 += 1
    label2.config(text=f"{voto2}")
    if voto2 >= 10:
        messagebox.showinfo(title='Ten', message=f'Zoro has {voto2} votes')


def verificar_voto3():
    global voto3
    voto3 += 1
    label3.config(text=f"{voto3}")
    if voto3 >= 10:
        messagebox.showinfo(title='Ten', message=f'Sanji has {voto3} votes')


def verificar_voto4():
    global voto4
    voto4 += 1
    label4.config(text=f"{voto4}")
    if voto4 >= 10:
        messagebox.showinfo(title='Ten', message=f'Nami has {voto4} votes')


def verificar_voto5():
    global voto5
    voto5 += 1
    label5.config(text=f"{voto5}")
    if voto5 >= 10:
        messagebox.showinfo(title='Ten', message=f'Usopp has {voto5} votes')


def verificar_voto6():
    global voto6
    voto6 += 1
    label6.config(text=f"{voto6}")
    if voto6 >= 10:
        messagebox.showinfo(title='Ten', message=f'Chopper has {voto6} votes')


def verificar_voto7():
    global voto7
    voto7 += 1
    label7.config(text=f"{voto7}")
    if voto7 >= 10:
        messagebox.showinfo(title='Ten', message=f'Robin has {voto7} votes')


def verificar_voto8():
    global voto8
    voto8 += 1
    label8.config(text=f"{voto8}")
    if voto8 >= 10:
        messagebox.showinfo(title='Ten', message=f'Franky has {voto8} votes')


def verificar_voto9():
    global voto9
    voto9 += 1
    label9.config(text=f"{voto9}")
    if voto9 >= 10:
        messagebox.showinfo(title='Ten', message=f'Brook has {voto9} votes')


def verificar_voto10():
    global voto10
    voto10 += 1
    label10.config(text=f"{voto10}")
    if voto10 >= 10:
        messagebox.showinfo(title='Ten', message=f'Jinbe has {voto10} votes')


janela.title('Votação')
janela.geometry('900x600')
janela.configure(background=lista_cor[0])
janela.resizable(width=FALSE, height=FALSE)

Button(janela, text='Luffy', background=lista_cor[0], foreground=lista_cor[3], anchor=W, command=verificar_voto).place(x=78, y=145, width=40, height=30)
img = ImageTk.PhotoImage(Image.open("img/Luffy.jpg"))
Label(image=img).place(x=40, y=50)
Button(janela, text='Zoro', background=lista_cor[0], foreground=lista_cor[10], anchor=W, command=verificar_voto2).place(x=240, y=145, width=35, height=30)
img2 = ImageTk.PhotoImage(Image.open("img/Zoro.jpg"))
Label(image=img2).place(x=215, y=50)
Button(janela, text='Sanji', background=lista_cor[0], foreground=lista_cor[4], anchor=W, command=verificar_voto3).place(x=400, y=145, width=40, height=30)
img3 = ImageTk.PhotoImage(Image.open("img/Sanji.jpg"))
Label(image=img3).place(x=370, y=50)
Button(janela, text='Nami', background=lista_cor[0], foreground=lista_cor[5], anchor=W, command=verificar_voto4).place(x=560, y=145, width=40, height=30)
img4 = ImageTk.PhotoImage(Image.open("img/Nami.jpg"))
Label(image=img4).place(x=535, y=50)
Button(janela, text='Usopp', background=lista_cor[0], foreground=lista_cor[6], anchor=W, command=verificar_voto5).place(x=730, y=145, width=45, height=30)
img5 = ImageTk.PhotoImage(Image.open("img/Usopp.jpg"))
Label(image=img5).place(x=700, y=50)
Button(janela, text='Chopper', background=lista_cor[0], foreground=lista_cor[7], anchor=W, command=verificar_voto6).place(x=62, y=500, width=55, height=30)
img6 = ImageTk.PhotoImage(Image.open("img/Tony Tony Chopper.jpg"))
Label(image=img6).place(x=45, y=410)
Button(janela, text='Robin', background=lista_cor[0], foreground=lista_cor[8], anchor=W, command=verificar_voto7).place(x=228, y=500, width=45, height=30)
img7 = ImageTk.PhotoImage(Image.open("img/Nico Robin.jpg"))
Label(image=img7).place(x=210, y=410)
Button(janela, text='Franky', background=lista_cor[0], foreground=lista_cor[2], anchor=W, command=verificar_voto8).place(x=390, y=500, width=45, height=30)
img8 = ImageTk.PhotoImage(Image.open("img/Franky.jpg"))
Label(image=img8).place(x=375, y=410)
Button(janela, text='Brook', background=lista_cor[0], foreground=lista_cor[9], anchor=W, command=verificar_voto9).place(x=563, y=500, width=45, height=30)
img9 = ImageTk.PhotoImage(Image.open("img/Brook.jpg"))
Label(image=img9).place(x=535, y=410)
Button(janela, text='Jinbe', background=lista_cor[0], foreground=lista_cor[1], anchor=W, command=verificar_voto10).place(x=740, y=500, width=40, height=30)
img10 = ImageTk.PhotoImage(Image.open("img/Jinbe.jpg"))
Label(image=img10).place(x=710, y=410)

Label(janela, text=' Clique em algum botão e vote em um personagem', background=lista_cor[5], foreground=lista_cor[1], anchor=W).place(x=285, y=260, width=280, height=50)

label = Label(janela, text=f'{voto}', foreground=lista_cor[3])
label.place(x=90, y=25)

label2 = Label(janela, text=f'{voto2}', foreground=lista_cor[10])
label2.place(x=255, y=25)

label3 = Label(janela, text=f'{voto3}', foreground=lista_cor[4])
label3.place(x=415, y=25)

label4 = Label(janela, text=f'{voto4}', foreground=lista_cor[5])
label4.place(x=580, y=25)

label5 = Label(janela, text=f'{voto5}', foreground=lista_cor[6])
label5.place(x=745, y=25)

label6 = Label(janela, text=f'{voto6}', foreground=lista_cor[7])
label6.place(x=82, y=385)

label7 = Label(janela, text=f'{voto7}', foreground=lista_cor[8])
label7.place(x=250, y=385)

label8 = Label(janela, text=f'{voto8}', foreground=lista_cor[2])
label8.place(x=411, y=385)

label9 = Label(janela, text=f'{voto9}', foreground=lista_cor[9])
label9.place(x=580, y=385)

label10 = Label(janela, text=f'{voto10}', foreground=lista_cor[1])
label10.place(x=752, y=385)

janela.mainloop()
