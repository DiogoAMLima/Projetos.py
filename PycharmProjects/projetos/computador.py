contador_total = 0
contador_pro_1 = 0
contador_pro_2 = 0
contador_pro_3 = 0
contador_pro_4 = 0

identificador = int(input("Informe a identificação (diferente de Zero): "))
while identificador == 0:
    if identificador == 0:
        print('Não pode ter identificador igual a 0...')
    identificador = int(input("Informe a identificação (diferente de Zero): "))
while identificador != 0:
    print("1 - Troca de Monitor.")
    print("2 - Troca da Placa-Mãe.")
    print("3 - Troca de fios, teclados ou mouses.")
    print("4 - Limpeza completa do PC.")
    defeito = int(input("Informe o número do serviço que deseje: "))
    if defeito == 1:
        contador_pro_1 = contador_pro_1 + 1
    elif defeito == 2:
        contador_pro_2 = contador_pro_2 + 1
    elif defeito == 3:
        contador_pro_3 = contador_pro_3 + 1
    elif defeito == 4:
        contador_pro_4 = contador_pro_4 + 1
    contador_total = contador_total + 1
    if defeito >= 5:
        print("Não existe serviço para este número. Tente outra vez...")
        contador_total = contador_total - 1
    if defeito <= -1:
        print("Não existe serviço para este número. Tente outra vez... ")
        contador_total = contador_total - 1
    identificador = int(input("Informe a identificação ou tecle 0 para sair: "))
    try:
        p1 = contador_pro_1 / contador_total * 100.0
        p2 = contador_pro_2 / contador_total * 100.0
        p3 = contador_pro_3 / contador_total * 100.0
        p4 = contador_pro_4 / contador_total * 100.0
        if identificador == 0:
            print("Situação                                   Quantidade    Precentual")
            print("1 - Troca de Monitor                          {0}          {1:.2f}%".format(contador_pro_1, p1))
            print("2 - Troca de Placa-Mãe                        {0}          {1:.2f}%".format(contador_pro_2, p2))
            print("3 - Troca de fios, teclados ou mouses         {0}          {1:.2f}%".format(contador_pro_3, p3))
            print("4 - Limpeza completa do PC                    {0}          {1:.2f}%".format(contador_pro_4, p4))
            print("Quantidade de serviços: {0}".format(contador_total))
    except ZeroDivisionError:
        print('Não é permitido divisão por 0...')
