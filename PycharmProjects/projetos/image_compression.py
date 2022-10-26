import numpy as np
import imageio
import matplotlib.pyplot as plt

# Image Compression:

image = imageio.imread('Python.svg.png')
# Carregando imagem (imagem deve estar no mesmo diretório)
A = image[:, :, 1]  # Array
u, s, v = np.linalg.svd(A, full_matrices=0)  # Reconstruindo imagem
# U -> autovetor esquerdo || S -> array diagonal de valores singulares || V - > autovetor direito

plt.subplots(1, 2, figsize=(10, 10))
plt.subplot(1, 2, 1)  # Número de linha, Coluna e index
plt.imshow(A)  # Mostranho a imagem
plt.title('PYTHON')  # Título
plt.axis('off')  # Eixo

rank = 60  # Porcentagem da imagem
titulo = 2  # Número da imagem no título

for i in range(0, 3):  # Loop para 60%, 70% e 80%
    plt.subplot(1, 2, 2)
    plt.imshow(u[:, : rank] @ np.diag(s[: rank]) @ v[: rank, :])
    plt.title(f'PYTHON {titulo}')
    plt.axis('off')
    plt.show()
    rank += 10
    titulo += 1
