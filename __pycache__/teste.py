import numpy as np 
import datetime
import sys
import cv2
import matplotlib.pyplot as plt



# print(datetime.date.today())
# print(datetime.datetime.now())

#TODO: aprender a numerar e desenhar formas na imagem.

# t = datetime.time

A1 = np.array([[0, 1, 0],
               [0, 0, 0],
               [0, 0, 0]])

A2 = np.array([[0, 1, 0],
               [0, 0, 0],
               [0, 0, 0]])

A3 = np.array([[0, 1, 0],
               [1, 0, 0],
               [0, 0, 0]])

A4 = np.array([[0, 1, 0],
               [3, 0, 0],
               [0, 0, 0]])

img = np.array([[1,1,1,1,0,0,1,1,0,0,1,1,1],
                [0,0,0,1,1,0,1,1,0,0,0,1,0],
                [0,0,1,1,1,0,1,1,0,0,1,1,1],
                [0,0,0,1,1,0,1,1,0,0,1,1,1],
                [1,1,1,1,1,0,1,1,0,0,1,1,1],
                [0,0,0,0,0,0,1,1,0,0,1,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,0,0,1,1,0,0,0,0,0],
                [1,1,1,1,0,0,1,1,0,0,1,1,1]])


# M = 10000

# i = 0.5/100 # am

# t = 12

# J =  M * (1 + i)**t - M

# print(M, '+', J, '= ', M+J)


# x,y,w,h = cv2.boundingRect(contour)
# image = cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 1)
