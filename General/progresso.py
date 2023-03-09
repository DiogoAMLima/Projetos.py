import pyprind
import time

x = int(input('Informe a quantidade de aulas assistidas: '))
y = 318
i = 0
bar = pyprind.ProgBar(y)  # Barra recebe o método pyprind.ProgBar e colocamos a variável como parâmetro
print()
while i != y:  # Se o iterador for diferente do número determinado anteriormente
    time.sleep(0.1)  # Tempo de pausa para a próxima ação
    i += 1
    if i == x:  # Se o iterador for igual ao número de aulas escolhido, ele faz um update na barra de progresso e para
        break
    bar.update()  # Fazendo o update da barra de progresso
print(f'\n\n\033[33m{i}\033[m aulas assisitdas, seu progresso é de: \033[34m{(x/y) * 100:.2f}%\033[m')  # Porcentagem
