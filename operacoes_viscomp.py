'''
Funções referentes as operações de visão computacional e algumas auxiliares.

Programador: Renan Sandes
Data: Mai/2020
'''

import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

class MyImage:
    '''
    classe para auxiliar na manipulação das imagens
    '''
    def __init__(self, img_matrix:np.ndarray):

        # Matriz da imagem
        self.data = img_matrix

        if len(self.data.shape) == 3:
            self.type = 'cor'
        elif len(self.data.shape) == 2:
            self.type = 'tons_de_ciza'
        else:
            self.type = ''


def abrir_img(path):
    '''
    Função para abrir as imagens
    path: diretório da imagem
    returns: ndarray (imagem em matriz)
    '''
    return cv2.imread(path, cv2.IMREAD_COLOR)
    


def normalize_uint8(img):
    '''
    Função para normalizar a imagem. 
    '''
    # Encontrar o máx.
    mx = np.max(img)
    # Encontrar o min
    mn = np.min(img)
    # Nova matriz normalizada.
    # Checar os valores de min e max. Se forem iguais, geram erros.
    if mn != mx:
        img2 = 255 * (img - mn) / (mx-mn)
        return np.uint8(img2)   
    else:
        return np.uint8(img)
    # Retornar convertendo para uint8.
    return np.uint8(img2)


def clip_uint8(img):
    '''Função para clipar os valores na faixa de 8 bits (entre 0 e 255). Retorna img em uint8'''
    img[img>=255] = 255
    img[img<= 0] = 0
    return np.uint8(img)


def convert_color_para_pb(img_color, conv_BGR= np.array([0.1140, 0.5870, 0.2989]) ):
    ''' 
    Converter uma imagem colorida para tons de cinza:
    img_color: B G R
    conv_BGR: Proporção das cores. default = [0.1140, 0.5870, 0.2989]
    '''
    if len(img_color.shape)==3:
        # Converter
        img_bw = img_color[:, :, 0] * conv_BGR[0] + img_color[:, :, 1] * conv_BGR[1] + img_color[:, :, 2] * conv_BGR[2]
        # Normalizar e retornar imangem
        return np.uint8(img_bw)
    
    else:
        return np.uint8(img_color)


def convert_pb_para_bin(img_pb, thresh):
    '''
    Converter imagem em pb para binario
    img_pb: numpy ndarray
    thresh: int entre 0 e 255
    '''
    # Aplicar o limiar
    img_bin = 255 * (img_pb > thresh)
    # Retornar normalizando
    return np.uint8(img_bin)


def soma_imagens(img1:np.ndarray, img2:np.ndarray, normalize=True):
    '''
    Função para somar duas imagens. 
    img1, img2: np.ndarray do mesmo tamanho.
    retorna: np.ndarray normalizada ou clipada.

    '''
    imgA = np.float32(img1)
    imgB = np.float32(img2)

    # Checar os tamanhos da mensagem:
    if (np.array_equal(imgA.shape, imgB.shape)):
        # Caso as imagens sejam do mesmo tamanho:
        # Somar as imagens
        imgC = imgA + imgB

        if normalize:
            # Retornar a matriz normalizada.
            return normalize_uint8(imgC)
        else:
            # Retornar a matriz clipada
            return clip_uint8(imgC)
    else:
        # Jeito besta de retornar se houve algum erro.
        print('Imagens de dimensões diferentes')


def soma_imagem_constante(img ,k, normalize=False):
    '''
    somar uma imagem com uma constante k.
    caso dê valor acima de 255, o valor será clipado para 255.
    '''
    # Somar com a constante.
    imgC = np.float32(img) + k
    # Retornar em uint8
    if normalize:
        return normalize_uint8(imgC)
    else:
        return clip_uint8(imgC)


def multiplicar_imagem_constante(img, k:float, normalize= True):
    ''' Multiplicar uma imagem com uma constante. '''
    imgC = k * img
    if normalize:
        return normalize_uint8(imgC)
    if not normalize:
        return clip_uint8(imgC)


def op_logica_and(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica AND'''
    # Comparar os tamanhos:
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op and.
        return np.uint8(255 * np.logical_and(imgA>127, imgB>127))


def op_logica_or(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica OR'''
    # Comparar os tamanhos:
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op or.
        return np.uint8(255 * np.logical_or(imgA>127, imgB>127))


def op_logica_xor(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica XOR'''
    # Comparar os tamanhos:
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op xor.
        return np.uint8(255 * np.logical_xor(imgA>127, imgB>127))


def op_logica_not(imgA:np.ndarray):
    '''Realizar a operação lógica NOT'''
    # Retornar a op and.
    return np.uint8(255 * np.logical_not(imgA>127))


def op_bitwise_and(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica bitwise AND'''
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op bitwise and.
        return np.uint8(np.bitwise_and(imgA, imgB))


def op_bitwise_or(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica bitwise OR'''
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op bitwise or.
        return np.uint8(np.bitwise_or(imgA, imgB))


def op_bitwise_xor(imgA:np.ndarray, imgB:np.ndarray):
    '''Realizar a operação lógica bitwise XOR'''
    if np.array_equal(imgA.shape, imgB.shape):
        # Retornar a op bitwise xor.
        return np.uint8(np.bitwise_xor(imgA, imgB))


def op_bitwise_not(imgA:np.ndarray):
    '''Realizar a operação lógica bitwise NOT'''
    # Retornar a op bitwise and.
    return np.uint8(np.bitwise_not(imgA))


class my_T:
    '''
    Classe com os métodos para retornar as matrizes para transformações geométricas
    '''
    @staticmethod
    def traslation(dx, dy):
        return np.array([[1, 0, dy],[0, 1, dx], [0, 0, 1]])

    @staticmethod
    def rotation(theta, unit='rad'):
        '''
        theta: angle of rotation
        unit: 'deg' or 'rad'. 'rad' by default
        '''
        if unit == 'deg':
            theta = np.pi* theta / 180
 
        return np.array([[np.cos(theta), -np.sin(theta), 0],
                         [np.sin(theta),  np.cos(theta), 0],
                         [0            ,  0            , 1]])

    @staticmethod
    def scale(factor):
        return np.array([[factor, 0, 0],[0, factor, 0], [0, 0, 1]])
    
    @staticmethod
    def shear(sx=0, sy=0):
        '''
        sx for horizontal
        sy for vertical
        
        '''
        return np.array([[1, sy, 0],[sx, 1, 0], [0, 0, 1]])


def transform_geom(img: np.ndarray, dx=0, dy=0, theta=45,scale_factor= 1,center=True,cx=0, cy=0): 
    '''
    Aplicar transformações geométricas a imagens.
    '''
    #t1 =time.perf_counter()

    # Alocar o espaço para a nova imagem.
    imgB = np.zeros(img.shape)

    # Translação
    T = my_T.traslation(dx, dy)
    
    # Rotação
    R = my_T.rotation(theta, unit='deg')
    
    # Escala
    S = my_T.scale(scale_factor)

    # Matriz resultante.    
    T_R = np.linalg.multi_dot([T, R, S])

    if center:
        T_R = np.linalg.multi_dot([
              my_T.traslation(np.floor(img.shape[1]/2), np.floor(img.shape[0]/2)),
              T_R,
              my_T.traslation(-np.floor(img.shape[1]/2), -np.floor(img.shape[0]/2))])

    elif (not center) and (cx !=0 or cy !=0):
        T_R = np.linalg.multi_dot([
              my_T.traslation(cy, cx),
              T_R,
              my_T.traslation(-cy,-cx)])
        

    # Inverter a matriz para realizar busca inversa,
    T_R_ = np.linalg.inv(T_R)
    s = img.shape
    print(s)
    for x in range(s[0]):
        for y in range(s[1]):
            P_l = np.uint16(np.dot(T_R_, np.array([[x], [y], [1]])))
            if 0 < P_l[0] < s[0] and 0 < P_l[1] < s[1]:
                imgB[x, y] = img[P_l[0], P_l[1]]

    #t2 = time.perf_counter()
    #print('Time elapsed: ', t2-t1)

    return np.uint8(imgB)


def transform_geom_rapida(img: np.ndarray, dx=0, dy=0, theta=45,scale_factor= 1,center=True, cx=0, cy=0):
    '''
    Função para realizara as transfomrações geométricas nas imagens
    
    retorna: np.ndarray de mesma dimensão de img.
    
    argumentos:
        - img: imagem a ser transformada
        - dx e dy: int - distancia para translação
        - theta: float -angulo de rotacao
        - scale_factor: float - fator de escala: ampliar ou reduzir
        - center: bool- operar em torno do centro da imagem.
        - cx, cy: int - Caso o centro não seja a origem ou o centro da imagem.
        -

    '''
    # Benchmark:
    #t1 =time.perf_counter()
    # Alocar o espaço para a nova imagem.
    imgB = np.zeros(img.shape)

    # Translação
    T = my_T.traslation(dx, dy)
    
    # Rotação
    R = my_T.rotation(theta, unit='deg')
    
    # Escala
    S = my_T.scale(scale_factor)

    # Matriz resultante.    
    T_R = np.linalg.multi_dot([T, R, S])

    if center:
        T_R = np.linalg.multi_dot([
              my_T.traslation(np.floor(img.shape[1]/2), np.floor(img.shape[0]/2)),
              T_R,
              my_T.traslation(-np.floor(img.shape[1]/2), -np.floor(img.shape[0]/2))])

    elif (not center) and (cx !=0 or cy !=0):
        T_R = np.linalg.multi_dot([
              my_T.traslation(cy, cx),
              T_R,
              my_T.traslation(-cy,-cx)])

    # Inverter a matriz para realizar busca inversa,
    T_R_ = np.linalg.inv(T_R)

    # Dividir em imagens menores
    h_division = 1000
    v_division = 1000
    ys  = np.arange(0, img.shape[0], v_division)
    xs = np.arange(0, img.shape[1], h_division)
    
    # Executar nas subimagens para poupar memória
    for x0 in xs:
        for y0 in ys:

            x1 = x0+ h_division 
            y1 = y0+ v_division

            if x1 > img.shape[1]:
                x1 = img.shape[1]

            if y1 > img.shape[0]:
                y1 = img.shape[0]
    
            # Meshgrid para combinar os pares ordenados de todas os elementos da imagem
            xx, yy = np.meshgrid(np.arange(x0, x1),
                                 np.arange(y0, y1))

            # Criar o array das posições para busca INVERSA!. uint16 para poupar memoria
            P = np.array([yy.flatten(), 
                          xx.flatten(), 
                          np.ones(xx.shape).flatten()]  ,dtype='uint16')

            # Aplicar a transformação
            P_ = np.dot(T_R_, P)

            # Extrair os indices
            P = np.uint16(P[0:2, :])
            P_ =np.uint16(P_[0:2 , :])

            # Condição para retirar os ídices inválidos: Os valores forem maiores que o da imagem. Como são em uint16 não serão negativos.
            valid_index = np.logical_not(
                np.logical_or( P_[0, :]>= img.shape[0],
                               P_[1, :]>= img.shape[1]))    
            
            # Retirar os indices invalidos
            P =  P[:, valid_index] 
            P_= P_[:, valid_index]

            imgB[P[0,:], P[1,:]] = img[P_[0,:], P_[1,:]]
        

    #t2 = time.perf_counter()
    #print('Time elapsed: ', t2-t1)

    return np.uint8(imgB)


def sobel(A:np.ndarray, threshold=127, normalizado=True):
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

    m = 1; k = 3 # dimensões da mascara
    n = 1; l = 3 # dimensões da mascara

    w = A.shape[1] # Dimensões da imagem
    h = A.shape[0] # Dimensões da imagem

    # Aplicar mascara convoluindo a imagem pela mascara.
    for i in range(k):
        for j in range(l):
            Bx[m:(h-m),n:(w-n)] += mask_sx[i,j] * A[i:(h-(k-i)+1), j:(w-(l-j)+1)]
            By[m:(h-m),n:(w-n)] += mask_sy[i,j] * A[i:(h-(k-i)+1), j:(w-(l-j)+1)]

    # Benchmarking
    # t2 = time.perf_counter()
    # print('sobel time elapsed: {} s'.format(t2-t1))
    
    # Retornar normalizado ou não
    if normalizado:
        return convert_pb_para_bin(normalize_uint8(np.sqrt(np.power(Bx,2) + np.power(By,2))),threshold)

    else:
        return np.sqrt(np.power(Bx,2) + np.power(By,2))


def sobel_slow(A: np.ndarray):
    '''
    EM DESUSO.

    Sobel utilizando muitas iterações

    A: imagem em e com 1 canal ndarray
    '''

    # Benchmarking
    # t1 = time.perf_counter()
    
    # Alocar espaço para as matrizes.
    B = np.zeros(A.shape)
    Gx = np.zeros(A.shape)
    Gy = np.zeros(A.shape)

    # Kernels de Sobel
    sy = np.array([[ -1,-2,-1], 
                   [  0, 0, 0],
                   [  1, 2, 1]])

    sx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

    # Dimensões do kernel
    m = sx.shape[0]//2; k = sx.shape[0]
    n = sx.shape[1]//2; l = sx.shape[1]
    # Dimensões da imagem
    w = A.shape[1]
    h = A.shape[0]

    for i in range (m, h-m):
        for j in range(n, w-n):
            Gx[i,j] = np.sum(np.multiply(sx , A[(i-m):(i+m+1), (j-n):(j+n+1)]))
            Gy[i,j] = np.sum(np.multiply(sy , A[(i-m):(i+m+1), (j-n):(j+n+1)]))            
    
    # Benchmarking
    # t2 = time.perf_counter()
    # print('sobel2: time elapsed: {} s'.format(t2-t1))

    # Retornar convertendo para bin aplicando threshold de 127
    return convert_pb_para_bin( normalize_uint8(np.sqrt(np.power(Gx,2) + np.power(Gy,2))), 127)


def derivativo_slow(A: np.ndarray):
    '''
    EM DESUSO:

    derivativo muitas iterações

    Retorna: Gx e Gy
    '''

    t1 = time.perf_counter()
    
    mask_x = np.array([[ -1,0,1]])
    mask_y = np.array([[-1],[0],[1]])

    w = A.shape[1]
    h = A.shape[0]

    # Fazer para a direção horizontal:
    Gx = np.zeros(A.shape)

    mask = mask_x
    m = mask.shape[0]//2
    n = mask.shape[1]//2
    k = mask.shape[0]
    l = mask.shape[1]

    for i in range (m, A.shape[0]-m):
        for j in range(n, A.shape[1]-n):
            Gx[i,j] = np.sum(np.multiply(mask_x , A[(i-m):(i+m+1), (j-n):(j+n+1)]))

    # Fazer para a direção vertical:
    Gy = np.zeros(A.shape)
    
    mask = mask_y
    m = mask.shape[0]//2
    n = mask.shape[1]//2
    k = mask.shape[0]
    l = mask.shape[1]
    for i in range (m, A.shape[0]-m):
        for j in range(n, A.shape[1]-n):
            Gy[i,j] = np.sum(np.multiply(mask_y , A[(i-m):(i+m+1), (j-n):(j+n+1)]))
    
    t2 = time.perf_counter()
    print('derivativo2: time elapsed: {} s'.format(t2-t1))
    
    return [normalize_uint8(Gx), normalize_uint8(Gy)]


def derivativo(A: np.ndarray, apply_threshold = False, threshold=127):
    '''
    derivativo poucas iterações
    
    Aplica mascara derivativa na direção dada.
    Retorna np.ndarray resultado.

    '''
    t1 = time.perf_counter()

    if len(A.shape) == 3:
        A = convert_color_para_pb(A)
    elif len(A.shape)==2:
        pass
    else:
        return np.zeros(A.shape)

    mask_x = np.array([[ -1,0,1]])
    mask_y = np.array([[-1],[0],[1]])

    # Fazer para a direção horizontal:
    Gx = np.zeros(A.shape)
    Gy = np.zeros(A.shape)
    
    # Para x
    mask = mask_x
    
    # Dimensões da mascara
    m = mask.shape[0]//2; k = mask.shape[0]
    n = mask.shape[1]//2; l = mask.shape[1]
    # Dimensões da imagem
    w = A.shape[1]
    h = A.shape[0]

    # Aplicar 
    for i in range(k):
        for j in range(l):
            Gx[m:(h-m),n:(w-n)] += mask[i,j] * A[i:(h-(k-i)+1), j:(w-(l-j)+1)]

    # Para y:
    mask = mask_y
    
    # Dimensões da mascara
    m = mask.shape[0]//2; k = mask.shape[0]
    n = mask.shape[1]//2; l = mask.shape[1]
    # Dimensões da imagem
    w = A.shape[1]
    h = A.shape[0]

    # Aplicar 
    for i in range(k):
        for j in range(l):
            Gy[m:(h-m),n:(w-n)] += mask[i,j] * A[i:(h-(k-i)+1), j:(w-(l-j)+1)]

    # Benchmarking
    # t2 = time.perf_counter() 
    # print('derivativo: time elapsed: {} s'.format(t2-t1))
    return np.sqrt(np.power(Gx,2)+np.power(Gy,2))


def aplica_mascara(img:np.ndarray, mask: np.ndarray, fast=True, normalize=True):
    '''
    img - Imagem a ser aplicada a máscara (apenas 1 canal de 8 bits)
    mask - mascara
    fast - método rápido (True), devagar(False)
    normalize - normalizar para 8 bits (True), senão retorna em float.
    
    retorna: Imagem normalizada para uint8 ou em float mesmo.

    '''
    imgRes = np.zeros(img.shape)

    # Parâmetros do tamanho da mascara
    m = mask.shape[0]//2 ; k = mask.shape[0]
    n = mask.shape[1]//2 ; l = mask.shape[1]

    # Parâmetros do tamanho da imagem
    w = img.shape[1]
    h = img.shape[0]

    # Método rápido: n iterações é o n de elementos na mascara
    if fast:
        for i in range(k):
            for j in range(l):
                imgRes[m:(h-m),n:(w-n)] += mask[i,j] * img[i:(h-(k-i)+1), j:(w-(l-j)+1)]
    
    # Método lento: n iterações é o n de elementos na imagem (menos os pixels de borda)
    else:
        for i in range (m, h-m):
            for j in range(n, w-n):
                imgRes[i,j] = np.sum(np.multiply(mask , img[(i-m):(i+m+1), (j-n):(j+n+1)]))

    if normalize:
        return normalize_uint8(imgRes)
    else:
        return imgRes


def kirsch(A:np.ndarray):
    '''
    A - IMAGEM
    retorna - imagem normalizada.
    '''
    # Alocar o lugar da imagem resultante
    R = np.zeros(A.shape)

    masks = [(1/15)* np.array([[-3,-3, 5], [-3, 0, 5], [-3,-3, 5]]), 
             (1/15)* np.array([[-3, 5, 5], [-3, 0, 5], [-3,-3,-3]]),
             (1/15)* np.array([[ 5, 5, 5], [-3, 0,-3], [-3,-3,-3]]),
             (1/15)* np.array([[ 5, 5,-3], [ 5, 0,-3], [-3,-3,-3]]),
             (1/15)* np.array([[ 5,-3,-3], [ 5, 0,-3], [ 5,-3,-3]]),
             (1/15)* np.array([[-3,-3,-3], [ 5, 0,-3], [ 5, 5,-3]]),
             (1/15)* np.array([[-3,-3,-3], [-3, 0,-3], [ 5, 5, 5]]),
             (1/15)* np.array([[-3,-3,-3], [-3, 0, 5], [-3, 5, 5]]) ]
    # Aplicar cada uma das mascaras e comparar guardando os maiores valores.
    for mask in masks:
        G = aplica_mascara(A, mask, normalize=False)
        R[G>R] = G[G>R] 
    
    return normalize_uint8(R)


########################## FIXME

def kernel_gaussiano(size, sigma=1):
    size = int(size) // 2
    x, y = np.meshgrid(range(-size,size+1), range(-size,size+1))
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


def canny(img:np.ndarray, thresh=127, sigma=1):
    pass

###############################

def histograma(img:np.ndarray, normalize=True):
    '''
    calcular histogramas para 256 tons de cinza.
    img: np.ndarray em tons de cinza.
    retorna histograma np.ndarray (256,)
    '''

    # Check dimension:
    if len(img.shape) == 3:
        img = convert_color_para_pb(img)
    
    # Check data type
    if img.dtype != np.uint8(1).dtype:
        img = np.uint8(img)

    # Alocar espaço
    hist = np.zeros(256)
    for i in range(256):
        hist[i] = np.sum(img == i)

    # normalizar 
    if normalize:
        hist = hist / np.sum(hist)

    return hist


def cdf(hist:np.ndarray):
    '''
    Calcular a CDF de um histograma normalizado.
    hist em vetor de shape(n,)
    return cdf mesmo shape do vetor.
    '''
    # Alocar
    c = np.zeros(hist.shape)
    # Acumular
    for i in range(1, len(hist)):
        c[i] = c[i-1] + hist[i-1]
    
    return c


def equalizacao_histogramas(img: np.ndarray):
    '''
    
    '''
    # calcular a cdf do histograma
    f=cdf(histograma(img))

    # Alocar espaço
    img_res = np.zeros(img.shape, dtype= 'uint8')
    # Catar na função de probabilidade e multiplicar.
    # g[i, j] = img[i, j] * f(img[i, j])
    img_res = np.uint8(np.multiply(np.take(f, img), img))
    
    return img_res

def transformacao_intensidade(img: np.ndarray, 
                                f =31.875 * np.log2(np.arange(256) + 1)):
    '''
    img é a img
    f é o vetor de lookup ( f(range(256)) )
    retorna o f resultante
    '''

    # Alocar espaço
    img_res = np.zeros(img.shape, dtype= 'uint8')
    # Catar na função de probabilidade e multiplicar.
    # g[i, j] = img[i, j] * f(img[i, j])
    img_res = np.uint8(np.take(f, img))

    return img_res
    
def autoescala(img:np.ndarray):
    
    # Encontrar o máx.
    mx = np.max(img)
    # Encontrar o min
    mn = np.min(img)
    # Nova matriz normalizada.
    # Checar os valores de min e max. Se forem iguais, geram erros.
    if mn != mx:
        return np.uint8((255/ (mx-mn)) * (img - mn))
    else:
        return np.uint8(img)
    

def multi_limiarizacao(img, threshs= [127], values= [0, 255]):
    '''
    limiariza a imagem de acordo com os limiares em thresh(lista) ou iteravel
    thresh: iteravel contendo n limiares (em ordem cresecente)
    values: n+1 valores dos limiares contendo 
    
    Ex.: img_limiarizada = multi_limiarizaca(img, threshs=[100, 150], values=[20, 100, 255])
    
    retorna a img limiarizada.
    '''
    # Alocar
    img_lim = np.zeros(img.shape)

    t = values[-1] * np.ones(256, dtype='uint8')

    last= 0
    for trsh, val in zip(threshs, values):
        t[last:trsh] = val
        last = trsh

    return np.uint8(np.take(t, img))


def limiarizacao_global(img:np.ndarray, thresh=0):
    '''
    img: imagem em tons de cinza
    thresh: limiar inicial
            para média, deixe 0.
            para usar o seu, entre com inteiro
    retorna a img limiarizada e o threshold
    '''

    # Chute inicial para o threshold
    if thresh == 0:
        thresh = img.mean()

    # dT inicial
    dT = 255
    # limitar o numero de iterações
    i=0; iterlimit = 100

    while dT>2 and i< iterlimit:
        # print(thresh)
        M1 = (img[img< thresh]).mean()
        M2 = (img[img>=thresh]).mean()
        novo_thresh = 0.5* (M1+M2)
        dT = np.abs(thresh - novo_thresh)
        thresh = novo_thresh
        i+=1

    return (np.uint8(255*(img>=thresh)) , thresh)


def media_k(h, k):
    '''
    intensidade média até o nivel k de um histograma 256.
    '''
    return np.sum(np.multiply(np.arange(256), h)[0:int(k+1)])


def segmentacao_global_otsu(img:np.ndarray):
    '''
    encontra um limiar ótimo conforme o método de otsu
    retorna uma tupla com a imagem limiarizada e o limiar.
    '''
    # Calcular as propabilidades da imagem
    p = histograma(img) # P robabilidade (histograma)
    P = cdf(p)          # Cumulativa
    #P = P+0.00001
    mg = media_k(P, 255)   # media geral

    # alocar espaço
    var_k_2 = 0 * np.arange(256,dtype='float32')
    
    media_k_vec = np.multiply(np.arange(256), p)

    for k in range(256):
        var_k_2[k] = P[k] * (np.sum(media_k_vec[0:(k+1)]) - mg)**2 + \
                     (1-P[k]) * (np.sum(media_k_vec[k+1:]) - mg)**2
    
    k_max = np.argmax(var_k_2)
    
    #print(k_max)
    # plt.subplot(2,2,1)
    # plt.bar(np.arange(256), p, label= 'p'); plt.legend()
    # plt.subplot(2,2,2)
    # plt.plot(P, label='P'); plt.legend()
    # plt.subplot(2,2,3)
    # plt.plot(var_k, label='var_k'); plt.legend()
    # plt.subplot(2,2,4)
    # plt.plot(var_k_2, label='var_k_2'); plt.legend()
    # plt.show()

    return (np.uint8(255*(img>= int(k_max))) ,int(k_max))

