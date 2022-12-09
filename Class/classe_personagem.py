# Classe sem interação com o usuário:

class Personagem1:
    def __init__(self, nome, idade, poder, bounty):
        self.nome = nome
        self.idade = idade
        self.poder = poder
        self.bounty = bounty


personagem = Personagem1("Luffy", "19", "Zoan-Mítica", "3.000.000.000")
print(f'O nome, idade, poder e recompensa do personagem é respectivamente: \033[31m'
      f'{personagem.nome}, {personagem.idade}, {personagem.poder}, R$ {personagem.bounty}\033[m')

