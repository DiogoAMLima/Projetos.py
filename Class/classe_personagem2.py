# Classe com interação com o usuário:

class Persoangem2:  # Definindo a classe e suas respectivas funções (métodos)
    def __init__(self, nome2):
        self.nome2 = nome2
        print(f'Seu personagem chama-se: \033[31m{self.nome2}\033[m')

    def idade(self, idade2):
        self.idade2 = idade2
        print(f'Seu personagem tem \033[36m{self.idade2}\033[m anos de idade')

    def poder(self, poder2):
        self.poder2 = poder2
        print(f'Seu personagem tem o poder: \033[34m{self.poder2}\033[m')

    def bounty(self, bounty2):
        self.bounty2 = bounty2
        print(f'Seu personagem tem uma recompensa avalidada em R$: \033[35m{self.bounty2:,.2f}\033[m')


per = str(input('\033[33mInforme o nome do personagem:\033[m '))
per_idade = str(input('\033[33mInforme a idade do personagem:\033[m '))
per_poder = str(input('\033[33mInforme o poder do personagem:\033[m '))
per_bounty = float(input('\033[33mInforme a recompensa do personagem:\033[m '))

valor = Persoangem2(per)  # Instânciando a classe
valor.idade(per_idade)
valor.poder(per_poder)
valor.bounty(per_bounty)
