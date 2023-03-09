import time
from tqdm import tqdm

x = int(input('Informe a quantidade de aulas assistidas: '))
y = 343
i = 0
for i in tqdm(range(y)):  # Para cada número no alcance do método tqdm com o parâmetro y passado
    time.sleep(0.1)  # Tempo de pausa para a próxima ação
    if i == x:  # Se o iterador for igual ao número escolhido, o looping acaba
        break
print(f'\n\n\033[33m{i}\033[m aulas assisitdas, seu progresso é de: \033[34m{(x/y) * 100:.2f}%\033[m')  # Porcentagem

# Esta barra de progresso mostra o número atual até o número final 343 ao lado da barra sendo carregada
