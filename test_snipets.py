import cv2
import numpy as np 
from operacoes_viscomp import *



def aplica_mascara_2(img:np.ndarray, mask: np.ndarray):
    '''
    img - Imagem a ser aplicada a máscara (apenas 1 canal de 8 bits)
    mask - mascara
    retorna: imagem resultado da convolução da mascara. sem normalização.

    '''

    # Parâmetros do tamanho da mascara
    m = mask.shape[0]//2 ; k = mask.shape[0]
    n = mask.shape[1]//2 ; l = mask.shape[1]

    # Parâmetros do tamanho da imagem
    w = img.shape[1]
    h = img.shape[0]

    # reshape image:

    # Alocar o espaço para nova imagem
    imgRes = np.zeros((h+2*m, w+2*n))

    imgOrgAdj = np.zeros((h+2*m, w+2*n))

    imgOrgAdj[m:(m+img.shape[0]), n:(img.shape[1]+n)] = img[:, :]

    # Parâmetros do tamanho da imagem
    w = imgOrgAdj.shape[1]
    h = imgOrgAdj.shape[0]

    # Método rápido: n iterações é o n de elementos na mascara
    for i in range(k):
        for j in range(l):
            imgRes[m:(h-m),n:(w-n)] += mask[i,j] * imgOrgAdj[i:(h-(k-i)+1), j:(w-(l-j)+1)]

    return imgRes[m:(img.shape[0]+m), n:(img.shape[1]+n)]


def sobel_2(A:np.ndarray):
    '''
    Aplica a mascara de sobel aos 
    utilizando poucas iterações.
    
    A: imagem em np.ndarray com apenas 1 canal.
    threshold: Após a aplicação das mascaras threshold.
    normalizado: Pode escolher receber a imagem como float, sem normalização.

    '''

    # Benchmarking
    #t1 = time.perf_counter()
    if len(A.shape)>2:
        A = convert_color_para_pb(A)

    # Alocar espaço para as matrizes:
    By = np.zeros(A.shape)
    Bx = np.zeros(A.shape)

    # Kernels de Sobel
    mask_sx = 0.25 * np.array([[ 1, 0, -1], 
                               [ 2, 0, -2],
                               [ 1, 0, -1]])

    mask_sy = 0.25 * np.array([[-1,-2,-1], 
                               [ 0, 0, 0],
                               [ 1, 2, 1]])

    Bx = aplica_mascara_2(A, mask_sx)
    By = aplica_mascara_2(A, mask_sy)

    # Benchmarking
    # t2 = time.perf_counter()
    # print('sobel time elapsed: {} s'.format(t2-t1))
    
    # Retornar normalizado ou não
    return [np.sqrt(np.power(Bx,2) + np.power(By,2)), np.arctan2(By,Bx)]



def kernel_gaussiano(size, sigma=1):
    '''Gera uma mascara gaussiana de tamanho e sigma dados.'''
    size = int(size) // 2
    x, y = np.meshgrid(range(-size,size+1), range(-size,size+1))
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z

def threshold_(img, lowThresholdRatio=0.05, highThresholdRatio=0.09):
    
    highThreshold = img.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return (res, weak, strong)

def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img

###################################################


# Aplicar mascara gaussiana na img
'''
img - Imagem a ser aplicada a máscara (apenas 1 canal de 8 bits)
mask - mascara
fast - método rápido (True), devagar(False)
normalize - normalizar para 8 bits (True), senão retorna em float.

retorna: Imagem normalizada para uint8 ou em float mesmo.

'''

# Abrir
img = cv2.imread('yoda.jpg')

# PB # [0:10, 0:10]
img = convert_color_para_pb(img)

# Mascara
mask = kernel_gaussiano(3, 100)

# Mostrar o tamanho da imagem
print('img', img.shape)

# Aplicar mascara gaussiana
imgRes = aplica_mascara_2(img, mask)

# Aplicar sobel
imgRes, D = sobel_2(imgRes)

# 
imgRes = non_max_suppression(imgRes, D)
cv2.imshow('imgRes', normalize_uint8(imgRes))
cv2.waitKey()
#
imgRes, weak, strong = threshold_(img, lowThresholdRatio=0.05, highThresholdRatio=0.09)

#
imgRes = hysteresis(img, weak, strong=255)

# normalizar
imgRes = normalize_uint8(imgRes)

# aplicar o threshold
threshold = 100
#imgRes = convert_pb_para_bin(imgRes, threshold)

# mostrar o tamanho da img resultante
print('imgRes', imgRes.shape)

# Ampliar o tamanho
# imgRes = cv2.resize(imgRes, (500,500), interpolation= cv2.INTER_AREA) 

# mostrar a imagem
cv2.imshow('imgRes', imgRes)

# esperar a janela fechar
cv2.waitKey()

# Mostrar o tamanho dps da mascara 
# print(img.shape,'=>', img_suave.shape)

# Resize para mostrar na tela
# img = cv2.resize(img, (500,500), interpolation= cv2.INTER_AREA)
# img_suave = cv2.resize(img_suave, (500,500), interpolation= cv2.INTER_AREA)

# Mostrar na tela
