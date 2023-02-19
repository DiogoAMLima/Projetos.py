# Usando set:

video_games = ('Playstation 1', 'Playstation 2', 'Playstation 2', 'Playstation 3', 'Playstation 4', 'Playstation 4',
               'Game Boy Color', 'Game Boy Advanced', 'Nintendo DS Lite', 'Nintendo DS Lite', 'Nintendo DSi', 'PSP',
               'PSP', 'Nintendo 3DS', 'XBOX ONE S', 'XBOX ONE S')

# print(video_games)  # Irão aparecer todos os itens

# print(set(video_games))  # Os itens repetidos serão removidos

# Conjutos:

conjunto = {1, 2, 3, 4}
conjunto2 = {1, 4, 6, 8}

conjunto3 = conjunto.intersection(conjunto2)
# print(f'\033[31m{conjunto3}\033[m')  # Itens de ambos os conjuntos

# print(f'\033[33m{conjunto.difference(conjunto2)}\033[m')  # Resultado: 2 e 3
# 2 e 3 estão no conjunto 1, mas não no conjunto 2

# print(f'\033[35m{conjunto2.difference(conjunto)}\033[m')  # Resultado: 6, 8
# 6 e 8 estão no conjunto 2, mas não no conjunto 1
