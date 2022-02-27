idade = int(input("Informe a sua idade: "))

ano_nas = 2022 - idade

pergunta = str(input("Você já fez aniversário? (sim ou nao) "))
if pergunta == 'nao':
    ano_nas = ano_nas - 1
    print(f'Você nasceu em {ano_nas}')
elif pergunta == 'sim':
    ano_nas = 2022 - idade
    print(f'Você nasceu em {ano_nas}')
else:
    print("Resposta inválida...")
