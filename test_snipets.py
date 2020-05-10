import cv2
import numpy as np 
from operacoes_viscomp import *

img = cv2.imread('yoda.jpg')

def kernel_gaussiano(size, sigma=1):
    size = int(size) // 2
    x, y = np.meshgrid(range(-size,size+1), range(-size,size+1))
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g

kernel = kernel_gaussiano(7, 1)

print(kernel)

img2 = aplica_mascara(img, kernel)



cv2.imshow('img', img)
cv2.imshow('img2', img2)


cv2.waitKey()