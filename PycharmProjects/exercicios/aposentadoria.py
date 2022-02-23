idade = int(input("Informe a idade do trabalhador: "))
tpsvc = int(input("Informe o tempo de serviço do trabalhador: "))

if idade >= 65:
    print("É possível se aposentar pela idade")
if tpsvc >= 30:
    print("É possível se aposentar pelo tempo de contribuição")
if idade >= 60 and tpsvc >= 25:
    print("É possível se aposentar tanto por idade quanto por tempo de contribuição")
else:
    print("Não é possível se aposentar nem pela idade nem pelo tempo de contribuição...")
