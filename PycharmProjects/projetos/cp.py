(input("Aperte alguma tecla para as perguntas aparecerem... "))

pergunta = 1
resposta = ''
resposta_2 = ''
resposta_3 = ''
resposta_4 = ''

valor1 = 'Luffy, Zoro, Nami, Usopp, Sanji, Chopper, Robin, Franky, Brook, Jinbe'
valor2 = 272
valor3 = 663
valor4 = 131


while pergunta != 0:
    print("1 - Informe a ordem de entrada dos tripulantes do chapéu de palha!\n")
    print("2 - Número do episódio da primeira aparição do Gear 1?\n")
    print("3 - Em que episódio Sabo retorna?\n")
    print("4 - Número do episódio da primeira aparição do Barba negra?\n")
    pergunta = int(input("Informe o número da pergunta que quer responder ou digite 0 para sair: "))
    if pergunta == 0:
        print("Até a próxima...")
    if pergunta == 1:
        print("1 - Informe a ordem de entrada dos tripulantes do chapéu de palha!")
        resposta: str = str(input())
        if resposta == valor1:
            print("Resposta certa!\n")
        if resposta != valor1:
            print("Resposta errada!\n")
    if pergunta == 2:
        print("2 - Número do episódio da primeira aparição do Gear 1?")
        try:
            resposta_2: int = int(input())
        except ValueError:
            print('Você digitou um número real, digite um número inteiro...')
        if resposta_2 == valor2:
            print("Resposta certa!\n")
        if resposta_2 != valor2:
            print("Resposta errada!\n")
    if pergunta == 3:
        print("3 - Em que episódio Sabo retorna?")
        try:
            resposta_3: int = int(input())
        except ValueError:
            print('Você digitou um número real, digite um número inteiro...')
        if resposta_3 == valor3:
            print("Resposta certa!\n")
        if resposta_3 != valor3:
            print("Resposta errada!\n")
    if pergunta == 4:
        print("4 - Número do episódio da primeira aparição do Barba negra?")
        try:
            resposta_4: int = int(input())
        except ValueError:
            print('Você digitou um número real, digite um número inteiro...')
        if resposta_4 == valor4:
            print("Resposta certa!\n")
        if resposta_4 != valor4:
            print("Resposta errada!\n")
    elif pergunta >= 5:
        print("Número incorreto, tente outra vez...")
    elif pergunta <= -1:
        print("Número incorreto, tente outra vez...")
