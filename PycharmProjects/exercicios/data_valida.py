dia = int(input("Informe um dia de um mês qualquer: "))
mes = int(input("Informe um mês de um ano qualquer: "))
ano = int(input("Informe um ano: "))

anoB = 0

data = f'A data digitada é {dia}/{mes}/{ano}'
print(data)

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Ano bissexto")
    print("Fevereiro pode ter 29 dias")
    anoB = ano
else:
    print("Ano comum")
if 1 <= mes <= 12:
    print("Mês válido")
    if mes == 2:
        print("Fevereiro só vai até o dia 28, exceto que o ano seja bissexto...")
    if mes == 2 and anoB == ano and dia == 29:
        print("Fevereiro pode ter o dia 29 ")
else:
    print("Mês inválido")
if 0 <= dia > 32:
    print("Dia inválido")
