(input("\n\033[35mAperte alguma tecla para as perguntas aparecerem...\033[m "))

# Declarando as variáveis

pergunta = 1

while pergunta != 0:  # Looping, só termina quando o usuário digitar zero
    global resposta_2, resposta_3, resposta_4  # Inicializando as variáveis como globais para usar 
    # dentro do looping sem precisar declarar fora do looping com algum valor
    print("\n\033[33m1 - Informe a ordem de entrada dos tripulantes do chapéu de palha!\n")
    print("2 - Número do episódio da primeira aparição do Gear 1?\n")
    print("3 - Em que episódio Sabo retorna?\n")
    print("4 - Número do episódio da primeira aparição do Barba negra?\033[m")
    pergunta = int(input("\nInforme o número da pergunta que quer responder ou digite 0 para sair: "))
    if pergunta == 0:  # Condicional
        print("\n\033[32mAté a próxima...\033[m")
    elif pergunta == 1:  # Condicional
        resposta = str(input("\n1 - Informe a ordem de entrada dos tripulantes do chapéu de palha: "))
        if resposta == 'Luffy, Zoro, Nami, Usopp, Sanji, Chopper, Robin, Franky, Brook, Jinbe':  # Condicional
            print("\n\033[34mResposta certa!\033[m")
        elif resposta != 'Luffy, Zoro, Nami, Usopp, Sanji, Chopper, Robin, Franky, Brook, Jinbe':  # Condicional
            print("\n\033[31mResposta errada!\033[m")
    elif pergunta == 2:  # Condicional
        try:  # Tratamento de erros
            resposta_2 = int(input("\n2 - Número do episódio da primeira aparição do Gear 1? "))
        except ValueError:
            print('\n\033[36mVocê digitou um número real, digite um número inteiro...\033[m')
        if resposta_2 == 272:  # Condicional
            print("\n\033[34mResposta certa!\033[m")
        elif resposta_2 != 272:  # Condicional
            print("\n\033[31mResposta errada!\033[m")
    elif pergunta == 3:  # Condicional
        try:  # Tratamento de erros
            resposta_3 = int(input("\n3 - Em que episódio Sabo retorna? "))
        except ValueError:
            print('\n\033[36mVocê digitou um número real, digite um número inteiro...\033[m')
        if resposta_3 == 663:  # Condicional
            print("\n\033[34mResposta certa!\033[m")
        elif resposta_3 != 663:  # Condicional
            print("\n\033[31mResposta errada!\033[m")
    elif pergunta == 4:  # Condicional
        try:  # Tratamento de erros
            resposta_4 = int(input("\n4 - Número do episódio da primeira aparição do Barba negra? "))
        except ValueError:
            print('\n\033[36mVocê digitou um número real, digite um número inteiro...\033[m')
        if resposta_4 == 131:  # Condicional
            print("\n\033[34mResposta certa!\033[m")
        elif resposta_4 != 131:  # Condicional
            print("\n\033[31mResposta errada!\033[m")
    elif pergunta >= 5 or pergunta <= -1:
        print("\n\033[31mNúmero incorreto, tente outra vez...\033[m")
