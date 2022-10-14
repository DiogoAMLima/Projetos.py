class CorpoHumano:
    def __init__(self):
        pass

    def skin(self, pele):
        self.pele = pele
        if cor_pele in 'branco branca':
            print(f'\nA pele é \033[97m{cor_pele}\033[m')
        elif cor_pele in 'preto preta':
            print(f'\nA pele é \033[30m{cor_pele}\033[m')
        else:
            print(f'\nA pele é {cor_pele}')

    def nails(self, tamanho, cor):
        self.tamanho = tamanho
        self.cor = cor
        if unha_cor in 'preto preta':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[30m{unha_cor}\033[m')
        elif unha_cor in 'vermelho':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[31m{unha_cor}\033[m')
        elif unha_cor in 'verde':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[32m{unha_cor}\033[m')
        elif unha_cor in 'amarelo':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[33m{unha_cor}\033[m')
        elif unha_cor in 'azul':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[34m{unha_cor}\033[m')
        elif unha_cor in 'roxo':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[35m{unha_cor}\033[m')
        elif unha_cor in 'ciano':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[36m{unha_cor}\033[m')
        elif unha_cor in 'cinza':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[37m{unha_cor}\033[m')
        elif unha_cor in 'branco branca':
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: \033[97m{unha_cor}\033[m')
        else:
            print(f'\nO tamanho da unha é: \033[31m{unha_tamanho}\033[m e a cor é: {unha_cor}')

    def hair(self, tamanho, cor, tipo):
        self.tamanho = tamanho
        self.cor = cor
        self.tipo = tipo
        if cabelo_cor in 'preto preta':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[30m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'vermelho':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[31m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'verde':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[32m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'loiro' or 'loira':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[33m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'azul':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[34m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'roxo':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[35m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'ciano':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[36m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'cinza':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[37m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        elif cabelo_cor in 'branco branca':
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'\033[97m{cabelo_cor}\033[m e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')
        else:
            print(f'\nO tamanho do cabelo é: \033[32m{cabelo_tamanho}\033[m, a cor do cabelo é: '
                  f'{cabelo_cor} e o tipo do cabelo é: \033[33m{cabelo_tipo}\033[m')

    def eyes(self, cor):
        self.cor = cor
        if olhos_cor in 'preto preta':
            print(f'\nA cor dos olhos é: \033[30m{olhos_cor}\033[m')
        elif olhos_cor in 'vermelho':
            print(f'\nA cor dos olhos é: \033[31m{olhos_cor}\033[m')
        elif olhos_cor in 'verde':
            print(f'\nA cor dos olhos é: \033[32m{olhos_cor}\033[m')
        elif olhos_cor in 'amarelo':
            print(f'\nA cor dos olhos é: \033[33m{olhos_cor}\033[m')
        elif olhos_cor in 'azul':
            print(f'\nA cor dos olhos é: \033[34m{olhos_cor}\033[m')
        elif olhos_cor in 'roxo':
            print(f'\nA cor dos olhos é: \033[35m{olhos_cor}\033[m')
        elif olhos_cor in 'ciano':
            print(f'\nA cor dos olhos é: \033[36m{olhos_cor}\033[m')
        elif olhos_cor in 'cinza':
            print(f'\nA cor dos olhos é: \033[37m{olhos_cor}\033[m')
        elif olhos_cor in 'branco branca':
            print(f'\nA cor dos olhos é: \033[97m{olhos_cor}\033[m')
        else:
            print(f'\nA cor dos olhos é: {olhos_cor}')

    def disease(self, doenca):
        self.doenca = doenca
        print(f'\nA doença do corpo é: \033[34m{doenca_corpo}\033[m')

    def blood(self, tipo_sangue, fator_rh):
        self.tipo_sangue = tipo_sangue
        self.fator_rh = fator_rh
        print(f'\nO tipo sanguíneo é: \033[35m{tipo_sangue}\033[m e o fator rh é: \033[36m{fator_rh}\033[m')

    def doacao_sangue(self):
        self.msg = f'\n\033[31mNão existe este tipo sanguíneo...\033[m'
        juncao = sangue_tipo + fator_rh
        if juncao in 'A+':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[33mAB+ e A+\033[m e receber de: ' \
                       f'\033[34mA+, A-, O+ e O-\033[m'
        elif juncao in 'A-':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[32mA+, A-, AB+ e AB-\033[m e receber de: ' \
                       f'\033[35mA- e O-\033[m'
        elif juncao in 'B+':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[31mB+ e AB+\033[m e receber de: ' \
                       f'\033[36mB+, B-, O+ e O-\033[m'
        elif juncao in 'B-':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[30mB+, B-, AB+ e AB-\033[m e receber de: ' \
                       f'\033[37mB- e O-\033[m'
        elif juncao in 'AB+':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[97mAB+\033[m e receber de: ' \
                       f'\033[33mA+, B+, O+, AB+, A-, B-, O- e AB- (todos)\033[m'
        elif juncao in 'AB-':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[31mAB+\033[m e receber de: ' \
                       f'\033[32mA+, B+, O+, AB+, A-, B-, O- e AB- (todos)\033[m'
        elif juncao in 'O+':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[34mA+, B+, O+ e AB+\033[m e receber de: ' \
                       f'\033[35mO+ e O-\033[m'
        elif juncao in 'O-':
            self.msg = f'\nO tipo {juncao} pode doar para: \033[36mA+, B+, O+, AB+, A-, B-, O- e AB- (todos)\033[m ' \
                       f'e receber de: \03337[mO-\033[m'
        return self.msg

    def verifica_tipo_sangue(self):
        print(f'\nSeu tipo sanguíneo é o: \033[34m{sangue_tipo}\033[m e fator RH: \033[35m{fator_rh}.\033[m '
              f'Preste atenção para quem pode doar e receber sangue...')
        print(self.doacao_sangue())


while True:
    try:
        cor_pele = str(input('\nInforme a cor da pele: ')).strip().lower()
        unha_tamanho = str(input('Informe o tamanho da unha: '))
        unha_cor = str(input('Informe a cor da unha: ')).strip().lower()
        cabelo_tamanho = str(input('Informe o tamanho do cabelo (comprido, curto...): '))
        cabelo_cor = str(input('Informe a cor do cabelo: ')).strip().lower()
        cabelo_tipo = str(input('Informe o tipo do cabelo (liso, crespo...): '))
        olhos_cor = str(input('Informe a cor dos olhos: ')).strip().lower()
        doenca_corpo = str(input('Informe a doença do corpo caso tenha: '))
        sangue_tipo = str(input('Informe o tipo sanguíneo: ')).upper()
        fator_rh = str(input('Informe o fator rh: '))
        res = CorpoHumano()
        res.skin(cor_pele)
        res.nails(unha_tamanho, unha_cor)
        res.hair(cabelo_tamanho, cabelo_cor, cabelo_tipo)
        res.eyes(olhos_cor)
        res.disease(doenca_corpo)
        res.blood(sangue_tipo, fator_rh)
        res.verifica_tipo_sangue()
    except (ValueError, KeyboardInterrupt):
        print('\n\033[36mHouve um problema com o tipo de dado informado ou o usuário interrompeu a entrada de '
              'informações, tente novamente...\033[m')
    esc = str(input('\nDeseja continuar? [S/N]? ')).strip().upper()
    if esc in 'S':
        continue
    else:
        print('\n\033[33mAté a próxima...\033[m')
        break
