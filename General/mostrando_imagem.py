import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Forma 1:

# imagem = cv2.imread("triangulo.png")  # Carregando imagem (neste caso ela está no mesmo diretório do arquivo Python)
# (Lembrando que você deve pegar sua imagem, colocar no mesmo diretório e colocar o nome dentro do imread())
# cv2.imshow("Original", imagem)  # Mostrando imagem
#
# # Pegando as cores: (No openCV é BGR e não RGB)
#
# imagem[0, 0] = (56, 76, 80)  # Coordenadas || Cores
# imagem[10:75, 10:75] = (56, 76, 0)  # Tamanho || Cores
# cv2.imshow("Imagem 2", imagem)  # Mostrando imagem
#
# imagem3 = imagem[0:150, 150:300]  # Recorte da imagem original
# cv2.imshow("Um parte da imagem", imagem3)  # Título
# cv2.imwrite("newtriangle.png", imagem3)  # Salvando em um novo arquivo
#
# cv2.waitKey(0)


# Forma 2:

# im = Image.open('triangulo.png')  # Carregando imagem (neste caso ela está no mesmo diretório do arquivo Python)
# (Lembrando que você deve pegar sua imagem, colocar no mesmo diretório e colocar o nome dentro do open())

# im.show()  # Mostrando imagem


# Forma 3:

img = mpimg.imread('triangulo.png')  # Carregando imagem (neste caso ela está no mesmo diretório do arquivo Python)

# (Lembrando que você deve pegar sua imagem, colocar no mesmo diretório e colocar o nome dentro do imread())

imgplot = plt.imshow(img)  # Colocando como gráfico

plt.show()  # Mostrando imagem
