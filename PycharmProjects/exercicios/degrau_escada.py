HD = float(input("Informe a altura do degrau de uma escada: "))
HF = float(input("Informe a altura que a pessoa queira alcançar subindo esta escada: "))

qntdD = HF / HD
print(f'Esta pessoa deverá subir: ' "{:.2f}".format(qntdD), "degraus")
