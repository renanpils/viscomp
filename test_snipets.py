import cv2
import numpy as np 
from operacoes_viscomp import *
import matplotlib.pyplot as plt
import time
import os

'''

- TODO:geração de histograma
- TODO:equalização de histogramas
- TODO:autoescala 
- TODO:limiarização global
- TODO:segmentação global ótima pelo método de Otsu

'''

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
