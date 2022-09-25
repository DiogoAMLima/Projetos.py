class Computador:
    def __init__(self, marca):
        self.marca = marca
        print(f'\nO computador tem a marca: \033[34m{self.marca}\033[m')

    def proc(self, processador):
        self.processador = processador
        print(f'O computador tem o processador: \033[34m{self.processador}\033[m')

    def font(self, fonte):
        self.fonte = fonte
        print(f'O computador tem a fonte com voltagem de: \033[34m{self.fonte}\033[m')

    def mem(self, memoria):
        self.memoria = memoria
        print(f'O computador tem a memória: \033[34m{self.memoria}\033[m')

    def placa_vid(self, placa_video):
        self.placa_video = placa_video
        print(f'O computador tem a placa de vídeo: \033[34m{self.placa_video}\033[m')

    def val(self, valor):
        self.valor = valor
        print(f'O computador tem o valor de: \033[34mR${self.valor:,.2f}\033[m')

    def armaz(self, armazenamento):
        self.armazenamento = armazenamento
        print(f'O computador tem como armazenamento: \033[34m{self.armazenamento}\033[m')

    def monitor(self, tela):
        self.tela = tela
        print(f'O computador tem o monitor da marca: \033[34m{self.tela}\033[m')

    # Método utilitário:
    def _voltagem_fonte(self):
        self.msg = '\033[33mPode funcionar normalmente\033[m'
        if self.fonte < 500:
            self.msg = '\033[32mCuidado com a voltagem da fonte!!!\033[m'
        if self.fonte >= 550:
            self.msg = '\033[31mBoa escolha de fonte\033[m'
        return self.msg

    # Método para chamar o método utilitário:
    def acesso(self):
        print(f'\nO PC \033[36m{self.marca}\033[m, com o processador '
              f'\033[37m{self.processador}\033[m, com a fonte \033[35m{self.fonte}\033[m, é um bom pc')
        print(self._voltagem_fonte())


mar = str(input('\033[33mInforme a marca do PC:\033[m '))
p = str(input('\033[33mInforme o processador do PC:\033[m '))
volt = float(input('\033[33mInforme a voltagem da fonte do PC:\033[m '))
me = str(input('\033[33mInforme a quantidade de memória do PC:\033[m '))
p_l = str(input('\033[33mInforme a placa de vídeo do PC:\033[m '))
v = float(input('\033[33mInforme o valor total do PC:\033[m '))
arm = str(input('\033[33mInforme se o PC terá: HD / SSD / NVME:\033[m '))
monitor_marca = str(input('\033[33mInforme a marca do monitor do PC:\033[m '))

res = Computador(mar)
res.proc(p)
res.font(volt)
res.mem(me)
res.placa_vid(p_l)
res.val(v)
res.armaz(arm)
res.monitor(monitor_marca)
res.acesso()
