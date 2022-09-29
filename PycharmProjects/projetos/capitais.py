def capitais(opcao):
    print('\033[32mOPÇÕES ABAIXO...\033[m')
    print("\n\033[34m(1) - Rio de Janeiro, (2) - São Paulo, (3) - Minas Gerais, (4) - Espírito Santo, "
          "\n(5) - Amazonas, (6) - Goiás, (7) - Acre, (8) - Rio Grande do Sul, (9) - Paraná, (10) - Santa Catarina, "
          "\n(11) - Rondônia, (12) - Roraima, (13) - Alagoas, (14) - Amapá, (15) - Maranhão, (16) - Bahia, "
          "\n(17) - Ceará, (18) - Pará, (19) - Piauí, (20) - Mato Grosso, (21) - Mato Grosso do Sul, (22) - Tocantins, "
          "\n(23) - Pernambuco, (24) - Rio Grande do Norte, (25) - Sergipe, (26) - Paraíba\033[m\n")
    match opcao:
        case 1:
            return 'Rio de Janeiro'
        case 2:
            return 'São Paulo'
        case 3:
            return 'Belo Horizonte'
        case 4:
            return 'Vitória'
        case 5:
            return 'Manaus'
        case 6:
            return 'Goiânia'
        case 7:
            return 'Rio Branco'
        case 8:
            return 'Porto Alegre'
        case 9:
            return 'Curitiba'
        case 10:
            return 'Florianópolis'
        case 11:
            return 'Poto Velho'
        case 12:
            return 'Boa Vista'
        case 13:
            return 'Maceió'
        case 14:
            return 'Macapá'
        case 15:
            return 'São Luís'
        case 16:
            return 'Salvador'
        case 17:
            return 'Fortaleza'
        case 18:
            return 'Belém'
        case 19:
            return 'Teresina'
        case 20:
            return 'Cuiabá'
        case 21:
            return 'Campo Grande'
        case 22:
            return 'Palmas'
        case 23:
            return 'Recife'
        case 24:
            return 'Natal'
        case 25:
            return 'Aracaju'
        case 26:
            return 'João Pessoa'
        case 27:
            print('\033[31mAté a próxima...\033[m')
        case _:
            print(f"\033[35mNúmero {opcao} inválido...\033[m\n")


res = float(input('\033[33mInforme um número de 1 a 26 para saber a capital ou 27 para sair... \033[m'))


print(capitais(res))

