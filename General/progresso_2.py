import time
from tqdm import tqdm

x = int(input('Informe a quantidade de aulas assistidas: '))
y = 343
i = 0
for i in tqdm(range(y)):
    time.sleep(0.1)
    if i == x:
        break
print(f'\n\n\033[33m{i}\033[m aulas assisitdas, seu progresso é de: \033[34m{(x/y) * 100:.2f}%\033[m')
