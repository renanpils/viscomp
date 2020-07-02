import numpy as np 
import datetime
import sys
import cv2
import matplotlib.pyplot as plt


a =  datetime.datetime.now()

s ='{}-{}-{}-{}-{}-{}.txt'.format(a.year,a.month,a.day,a.hour,a.minute,a.second) 

print(s)

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



def display_on(self, img, frme, tipo='cor'):
        '''
        Função para colocar no label uma imagem.
        img = matriz (np.ndarray)
        frame = self.ui.imgFrameX  (Qlabel)
        tipo = 'cor', 'pb', 'bin' (Inutilizado!)
        '''
        if(len(img.shape) == 3):
            tipo = 'cor'
        elif(len(img.shape) == 2):
            tipo = 'pb'
        else:
            tipo = ''
            return
        
        if tipo == 'cor':
            # Fazer o QImage da imagem, 
            image = QtGui.QImage(img,
                                 img.shape[1], 
                                 img.shape[0], 
                                 QtGui.QImage.Format_RGB888).rgbSwapped()   

            # Ajustar o pixmap para caber no label.
            if img.shape[0] < img.shape[1]:
                #maior largura:
                frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToWidth(frme.width()))
            else:
                #maior altura: 
                frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToHeight(frme.height()))
        
        elif tipo == 'pb':
            # Fazer o QImage da imagem, 
            image = QtGui.QImage(img,
                                 img.shape[1], 
                                 img.shape[0], 
                                 QtGui.QImage.Format_Grayscale8) 

            pixmap = QtGui.QPixmap.fromImage(image)
            # Ajustar o pixmap para caber no label.
            if img.shape[0] < img.shape[1]:
                #maior largura:
                #frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToWidth(frme.width()))
                pass
            else:
                #maior altura: 
                #frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToHeight(frme.height()))
                pass
            