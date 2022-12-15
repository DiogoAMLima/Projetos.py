from rich.progress import track
from time import sleep
from rich import print as print

# Progresso

alcance = int(input('Informe o alcance: '))

for progresso in track(range(alcance), 'Processing...'):
    sleep(0.5)
print(f'[blue]FINALIZADO!!![/]')
