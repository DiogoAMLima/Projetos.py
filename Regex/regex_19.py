import re

# Relembrando:

r'''
.- qualquer caractere, exceto linha nova
"\" - usando antes de metacarcteres para especificar seu significado literal
$ - termina com
^ - começa com
[] - opcional entre os que estão dentro dos colchetes
() - captura grupos de caracteres
* - de zero a mais vezes
? - zero ou uma vez
+ = uma ou mais vezes
{m, n} de m a n vezes
| - ou
\w - qualquer caractere alfanumérico
\W - qualquer caractere não-alfanumérico
\d - qualquer caractere que seja um dígito (0-9)
\D - qualquer caractere não dígito
\s - espaço em branco
'''

# Função search - Procurar no texto o padrão informado:

texto = 'Anote meu número de telefone: (95)00000-0000 por favor'

# print(re.search(r'\(\d{2}\)\d{4,5}-\d{4}', texto))

# Função match - Indica se uma expressão regular está no início:

texto2 = 'O número serial do meu objeto é: TTXZ-34565'

# print(re.match(r'[A-Z-a-z]{4}-\d{5}', texto2))

texto3 = 'TTXZ-34565 é o número serial do meu objeto'

# print(re.match(r'[A-Z-a-z]{4}-\d{5}', texto3))
