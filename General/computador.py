# Declarando as variáveis na mesma linha:
contador_total, contador_pro_1, contador_pro_2, contador_pro_3, contador_pro_4 = 0, 0, 0, 0, 0

while True:  # Lopping
    # Mostrando menu
    print("\033[36m1 - Troca de Monitor.")
    print("2 - Troca da Placa-Mãe.")
    print("3 - Troca de fios, teclados ou mouses.")
    print("4 - Limpeza completa do PC.\033[m")
    try:  # Tratamento de erros
        defeito = int(input("\nInforme o número do serviço que deseja: "))
        if defeito == 1:
            contador_pro_1 = contador_pro_1 + 1  # Incremento da quantidade
        elif defeito == 2:
            contador_pro_2 = contador_pro_2 + 1  # Incremento da quantidade
        elif defeito == 3:
            contador_pro_3 = contador_pro_3 + 1  # Incremento da quantidade
        elif defeito == 4:
            contador_pro_4 = contador_pro_4 + 1  # Incremento da quantidade
        contador_total = contador_total + 1
        if defeito >= 5 or defeito <= -1:  
            # Se for maior que 5 ou menor igual a -1, o código informa que não existe serviço para estas opções
            print("\n\033[31mNão existe serviço para este número. Tente outra vez...\033[m")
            contador_total = contador_total - 1
        try:
            # Cáluco da porcentagem
            p1 = contador_pro_1 / contador_total * 100.0
            p2 = contador_pro_2 / contador_total * 100.0
            p3 = contador_pro_3 / contador_total * 100.0
            p4 = contador_pro_4 / contador_total * 100.0
            print("\nSituação                         Quantidade(s)    Precentual")
            print(f"1 - Troca de Monitor                  \033[32m{contador_pro_1}\033[m           \033[34m{p1:.2f}%\033[m")
            print(f"2 - Troca de Placa-Mãe                \033[32m{contador_pro_2}\033[m           \033[34m{p2:.2f}%\033[m")
            print(f"3 - Troca de fios, teclados ou mouses \033[32m{contador_pro_3}\033[m           \033[34m{p3:.2f}%\033[m")
            print(f"4 - Limpeza completa do PC            \033[32m{contador_pro_4}\033[m           \033[34m{p4:.2f}%\033[m")
            print(f"\nQuantidade de serviços: \033[33m{contador_total}\033[m\n")
        except ZeroDivisionError:
            print('\n\033[31mNão é permitido divisão por 0...\033[m')
    except ValueError:
        print('\n\033[31mValor inválido!\033[m\n')
    esc = str(input('Deseja continuar? [S/N] ')).upper()
    if esc in 'N':
        print('\n\033[32mAté a próxima!\033[m')
        break
    else:
        print()
        pass
