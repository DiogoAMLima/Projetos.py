import pandas as pd

# Inicializando as listas:

info1 = []
info2 = []
info3 = []
info4 = []
info5 = []
info6 = []
info7 = []
info8 = []

while True:
    mar = str(input('\033[33mInforme a marca do PC:\033[m '))
    info1.append(mar)  # Adicionando a lista
    p = str(input('\033[33mInforme o processador do PC:\033[m '))
    info2.append(p)  # Adicionando a lista
    volt = float(input('\033[33mInforme a voltagem da fonte do PC:\033[m '))
    info3.append(volt)  # Adicionando a lista
    me = str(input('\033[33mInforme a quantidade de memória do PC:\033[m '))
    info4.append(me)  # Adicionando a lista
    p_l = str(input('\033[33mInforme a placa de vídeo do PC:\033[m '))
    info5.append(p_l)  # Adicionando a lista
    v = str(input('\033[33mInforme o valor total do PC:\033[m '))
    info6.append(v)  # Adicionando a lista
    arm = str(input('\033[33mInforme se o PC terá: HD / SSD / NVME:\033[m '))
    info7.append(arm)  # Adicionando a lista
    monitor_marca = str(input('\033[33mInforme a marca do monitor do PC:\033[m '))
    info8.append(monitor_marca)  # Adicionando a lista
    esc = str(input('Quer continuar? [S/N]? ')).upper()
    if esc not in 'S':
        break
    else:
        continue

# Mostrando os resultados:

print(f'\nA(s) marca(s) do(s) PC(s) é/são: \033[31m{info1}\033[m'
      f'\nO(s) processador(es) do(s) PC(s) é/são: \033[31m{info2}\033[m'
      f'\nA(s) voltagem(s) da(s) fonte(s) é/são: \033[31m{info3}W\033[m'
      f'\nA(s) quantidade(s) de memória(s) do(s) PC(s) é/são: \033[31m{info4}\033[m'
      f'\nA(s) placa(s) de vídeo(s) do(s) PC(s) é/são: \033[31m{info5}\033[m'
      f'\nO(s) valor(es) total(is) do(s) PC(s) é/são: \033[31m{info6}\033[m'
      f'\nO(s) armazenamento(s) do(s) PC(s) será/serão pelo(s): \033[31m{info7}\033[m'
      f'\nA(s) marca(s) do(s) monitor(es) do(s) PC(s) é/são: \033[31m{info8}\033[m')


print()

# Adicioanando a um DataFrame:

dados = {'Marcas': info1, 'Processadores': info2, 'Fontes': info3, 'Memória': info4, 'Placas de vídeo': info5,
         'Valores totais': info6, 'Armazenamentos': info7, 'Marcas dos monitores': info8}

tabela = pd.DataFrame(data=dados)
print(tabela)

opcao = str(input('\nGostaria de criar uma tabela em Excel: [S/N]? ')).strip().upper()
if opcao not in 'S':
    print('\033[37mTudo bem, até a próxima...\033[m')
else:
    nome_tabela = str(input('\nInforme o nome do seu arquivo em excel: '))

    extensao = '.xlsx'

    nome_final = nome_tabela + extensao

    print(f'\nEsta será sua planilha: \033[34m{nome_final}\033[m')

    folha = str(input('\nInforme o nome da aba do excel: '))

    tabela.to_excel(f'{nome_final}', sheet_name=f'{folha}')

    print('\n\033[34mPlanilha criada com sucesso!!!\033[m')
