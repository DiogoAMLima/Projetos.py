from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Colocando o nome no cartaz (1ª parte):

# name = str(input('Informe seu nome: '))
#
# name_length = int(input('Informe o tamanho do nome: '))
#
# imagem = Image.open('cartaz.png')
# draw = ImageDraw.Draw(imagem)
# fonte = ImageFont.truetype('tahoma.ttf', name_length)
# draw.text((51, 309), name, font=fonte)
# imagem.save('imagem.png')

# Colocando uma recompensa no cartaz (2ª parte):

bounty = str(input('Informe o valor da recompensa: '))

bounty_length = int(input('Informe o tamanho do nome: '))

imagem = Image.open('imagem.png')
draw = ImageDraw.Draw(imagem)
fonte = ImageFont.truetype('tahoma.ttf', bounty_length)
draw.text((71, 352), bounty, font=fonte)
imagem.save('imagem.png')
