import random
import string
import time

qntd = int(input('Informe quantos caracteres terá a senha: '))
# Usando a bilioteca string, não precisamos usar variáveis como no código de gerador de senha 
password = "".join(random.choices(string.printable, k=qntd)).replace(" ", ".")
# Unindo os caracteres com .join gerados pelo método choices de acordo com o string.printable que tem os caracteres
# de acordo com a variável k que determinará o tamanho da senha
    
print('\n\033[31mEstamos gerando sua senha, por favor aguarde!!!\033[m')
time.sleep(1.5)

print(f'\nSua senha é: \033[34m{password}\033[m')
