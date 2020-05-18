'''
Aplicativo desenvolvido para disciplinda Visão Computacional do
Programa de Pós Graduação em Engenharia Elétrica (PROEE) 
da Universidade Federal de Sergipe (UFS).

Semestre: 2020.1
Prof. Dr. Eduardo Oliveira Freire

Aluno: Renan Praciano Ideburque Leal Sandes
Data: Mai/2020
Versão: 3

Descrição:
Este aplicativo implementa as funções relativas às operações vistas ao longo da disciplina:
Funções implementadas nesta versão:
    - Conversão de Imagens coloridas para tons de cinza
    - Conversão de Imagens coloridas para Binário
    - Operações aritméticas:
        - adição de constante
        - adição entre duas imagens
        - multiplicação por uma constante

    - operações lógicas:
        - and, or, xor, not
        - bitwise and, bitwise or, bitwise xor, bitwise not
    
    - operações de transformações geométricas
    
    - operações de detecção de bordas:
        - derivativo
        - sobel
        - kirsch

*** Observações para abrandar a leitura do código: ***

o código segue a sequência:

Primeiramente são definidas as funções que realizam as operações da disciplina. 
Estas estão declaradas fora da classe, e serão chamadas em tempo de execução pelos callbacks da GUI.

A Janela principal é definida pela classe ApplicationWindow, que herda as funcionalidades da biblioteca PyQt5
Dentro desta classe, é instanciado um objeto da classe Ui_MainWindow importada de ViscompUtilGui, 
que é gerada através da conversão do arquivo '.ui' para o arquivo '.py' pelo uso do recurso pyuic5 
da biblioteca PyQt5. O arquivo '.ui' citado é gerado pelo software "cross-platagorm" qt designer.

Dentro da classe ApplicationWindow:
    As funcionalidades da GUI tem nomenclatura que refere ao que ela faz. Embora nem todas estejam padronizadas
    a regra vale para a maioria.

    Os métodos da classe cujo identificador inicia por call_action são callbacks das funcionalidades do programa,
    sendo disparadas no menu de ações. Quando chamadas elas ajustam os diversos elementos da GUI para 
    uma dada funcionalidade. Ela armazena a função atual na variavel current_function.

    Os métodos da classe cujo identificado inicia por call_resultado são callbacks que realizam a função a depender
    de qual funcionalidade o programa está, semelhante a uma máquina de estado. O estado é armazenado na
    variávels current_funcion.

    Os métodos da classe que não se encaixam nos quesitos acima não estão padronizados, mas os que contem
    call são atribuidos a algum widget como callback.

Ao final, a classe é instanciada e executada.


Modificações da versão 3:
    - Operações movidas para operacoes_viscomp.py
    - Elementos widgets adicionados e importados via my_interface.py
    - GUI refeita
    - Adicionadas funções de transformações geométricas e bordas
    - 
'''



import sys
# importar operações de visão computacional.
from operacoes_viscomp import*
# Importar os elementos gráficos da GUI
from my_interface import *


# ===================================================================================
#
# ===================================================================================

class ApplicationWindow(QtWidgets.QMainWindow):
    #################################################################
    ######### Funções da classe e de inicialização da ui. ###########
    #################################################################
    def __init__(self):
        '''construtor da classe ApplicationWindow'''
        # Inicializar a superclasse
        super(ApplicationWindow, self).__init__()
        # Instanciar a janela criada usando o qt designer
        self.ui = Ui_MainWindow()
        # Inicializar a janela do qt designer
        self.ui.setupUi(self)
        # Colocar o widget de controle:
        self.put_current_widget(ui_start_widget)
        # Inicializar o menu:
        self.menu_setup()
        # Inicializar variáveis
        self.variables_setup()

    def variables_setup(self):
        '''inicializar algumas variáveis que serão usadas ao longo do código.'''
        self.img1 = np.array([0])
        self.img2 = np.array([0])
        self.img3 = np.array([0])
        

    def menu_setup(self):
        '''configurar os callbacks das funções dos menus'''

        self.ui.actionSalvar_resultado.triggered.connect(self.call_action_salvar_resultado)
        self.ui.pushButton_abrirPara1.clicked.connect(self.call_action_openTo1)
        self.ui.pushButton_abrirPara2.clicked.connect(self.call_action_openTo2)
        self.ui.actionAbrir_para_principal.triggered.connect(self.call_action_openTo1)
        self.ui.actionAbrir_para_auxiliar.triggered.connect(self.call_action_openTo2)
        self.ui.pushButton_usarResultado1.clicked.connect(self.call_copy_res_para_prin)
        self.ui.pushButton_usarResultado2.clicked.connect(self.call_copy_res_para_aux)
        self.ui.actionConverter_para_Tons_de_Cinza.triggered.connect(self.call_action_convert_tc)
        self.ui.actionConverter_para_Preto_e_Branco_bin_rio.triggered.connect(self.call_action_convert_bin)
        self.ui.actionSomar_constante.triggered.connect(self.call_action_somar_constante)
        self.ui.actionSomar_Imagens.triggered.connect(self.call_action_somar_imagens)
        self.ui.actionMultiplicar_por_constante.triggered.connect(self.call_action_multiplicar_constante)
        self.ui.actionAnd.triggered.connect(self.call_action_and)
        self.ui.actionOr.triggered.connect(self.call_action_or)
        self.ui.actionXor.triggered.connect(self.call_action_xor)
        self.ui.actionNot.triggered.connect(self.call_action_not)
        self.ui.actionAnd_2.triggered.connect(self.call_action_and_2)
        self.ui.actionOr_2.triggered.connect(self.call_action_or_2)
        self.ui.actionXor_2.triggered.connect(self.call_action_xor_2)
        self.ui.actionNot_2.triggered.connect(self.call_action_not_2)
        self.ui.actionAplicar_transforma_es_geom_tricas.triggered.connect(self.call_action_transform)
        self.ui.actionDerivativo.triggered.connect(self.call_action_derivativo)
        self.ui.actionKirsch.triggered.connect(self.call_action_kirsch)
        self.ui.actionSobel.triggered.connect(self.call_action_sobel)

    def put_current_widget(self, ui_widget):
        '''colocar um widget referente a uma função na tela'''
        self.remove_current_widget()
        self.current_widget = QtWidgets.QWidget()
        self.current_widget_form = ui_widget.Ui_Form()
        self.current_widget_form.setupUi(self.current_widget)
        self.ui.panel_layout.addWidget(self.current_widget)    

    def remove_current_widget(self):
        '''remover um widget referente a uma função da tela'''
        try:
            self.current_widget.hide()
            self.ui.panel_layout.removeWidget(self.current_widget) 
        except:
            pass
    
    ##################################################### 
    ########## funções call_resultado ###################
    #####################################################

    def call_resultado_convert_tons_cinza(self):
        
        B = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_B.text(),
            'float',default_return=0.1140)
        G = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_G.text(),
            'float', default_return=0.5870)
        R = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_R.text(),
            'float', default_return=0.2989)
        
        self.img3 = convert_color_para_pb(self.img1 , conv_BGR = np.array([B, G, R]) )
        self.display_on(self.img3, self.ui.imgFrame3)


    def call_resultado_convert_bin(self):

        B = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_B.text(),
            'float',default_return=0.1140)
        G = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_G.text(),
            'float', default_return=0.5870)
        R = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_R.text(),
            'float', default_return=0.2989)
        
        thresh = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return=0)

        self.img3 = convert_color_para_pb(self.img1 , conv_BGR = np.array([B, G, R]) )
        self.img3 = convert_pb_para_bin(self.img3, thresh)
        
        self.display_on(self.img3, self.ui.imgFrame3)
    
    def call_resultado_and(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_pb_para_bin(convert_color_para_pb(self.img1), threshold)
        imgB = convert_pb_para_bin(convert_color_para_pb(self.img2), threshold)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_logica_and(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_or(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_pb_para_bin(convert_color_para_pb(self.img1), threshold)
        imgB = convert_pb_para_bin(convert_color_para_pb(self.img2), threshold)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_logica_or(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_xor(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_pb_para_bin(convert_color_para_pb(self.img1), threshold)
        imgB = convert_pb_para_bin(convert_color_para_pb(self.img2), threshold)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_logica_xor(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_not(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_pb_para_bin(convert_color_para_pb(self.img1), threshold)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        # Realizar a operação
        self.img3 = op_logica_not(imgA)
        # Exibir na tela
        self.display_on(self.img3, self.ui.imgFrame3)

    def call_resultado_and_2(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_color_para_pb(self.img1)
        imgB = convert_color_para_pb(self.img2)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_bitwise_and(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_or_2(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_color_para_pb(self.img1)
        imgB = convert_color_para_pb(self.img2)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_bitwise_or(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_xor_2(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_pb_para_bin(convert_color_para_pb(self.img1), threshold)
        imgB = convert_pb_para_bin(convert_color_para_pb(self.img2), threshold)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        self.display_on(imgB, self.ui.imgFrame2,'')
        # Checar o tamanho
        if np.array_equal(imgA.shape, imgB.shape):
            # Realizar a operação
            self.img3 = op_bitwise_xor(imgA, imgB)
            # Exibir na tela
            self.display_on(self.img3, self.ui.imgFrame3)

        else:
            self.exibe_janela_aviso('Imagens não são do mesmo tamanho!')

    def call_resultado_not_2(self):
        # Pegar o threshold do slider
        threshold = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_limiar.text(),
            'int', default_return= 127)    
        # Primeiro passo: Converter ambas imagens para binario:
        imgA = convert_color_para_pb(self.img1)
        # Exibir as conversões:
        # As imagens convertidas não ficam salvas.
        self.display_on(imgA, self.ui.imgFrame1,'')
        # Realizar a operação
        self.img3 = op_bitwise_not(imgA)
        # Exibir na tela
        self.display_on(self.img3, self.ui.imgFrame3)

    def call_resultado_somar_imagens(self):
        if np.array_equal(self.img1.shape, self.img2.shape):
            self.img3 = soma_imagens(self.img1, self.img2,
                                normalize=self.current_widget_form.radioButton_normalizar.isChecked())
            self.display_on(self.img3, self.ui.imgFrame3,'')
        
        else:
            self.exibe_janela_aviso('Imagens devem ser do mesmo tamanho!')

    def call_resultado_somar_constante(self):
        
        constante = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_constante.text(),
            'float')

        self.img3 =soma_imagem_constante(self.img1, 
            constante, 
            normalize=self.current_widget_form.radioButton_normalizar.isChecked())
        
        self.display_on(self.img3, self.ui.imgFrame3)

    def call_resultado_multiplicar_constante(self):
        
        constante = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_constante.text(),
            'float')

        self.img3 =multiplicar_imagem_constante(self.img1, 
            constante, 
            normalize=self.current_widget_form.radioButton_normalizar.isChecked())
        
        self.display_on(self.img3, self.ui.imgFrame3)

    
    def call_resultado_transform(self):
        ''' Calcular a transformação geométrica'''
        # desabilitar botão:
        self.current_widget_form.pushButton.setEnabled(False)

        # Coletar todas as informações do dialogo:
        theta = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_3.text(), 'float')
        dx = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_dx.text(), 'int')
        dy = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_dy.text(), 'int')
        scale_factor = self.get_number_whithout_error(
            self.current_widget_form.lineEdit_escala.text(), 'float')

        if self.current_widget_form.radioButton_rad.isChecked():
            angle_unit = 'rad'
        else:
            angle_unit = 'deg'

        if self.current_widget_form.radioButton_origem.isChecked():
            center = False
            cx = 0
            cy = 0
        elif self.current_widget_form.radioButton_outro.isChecked():
            center = False
            cx = self.get_number_whithout_error(
                self.current_widget_form.lineEdit_cx.text(), 'int')
            cy = self.get_number_whithout_error(
                self.current_widget_form.lineEdit_cy.text(), 'int') 
        else:
            center = True
            cx = 0
            cy = 0

        # Calcular a nova imagem
        self.img3 = transform_geom_rapida(self.img1, dx, dy,theta, scale_factor, center)
        # Mostrar na tela
        self.display_on(self.img3, self.ui.imgFrame3)
        # Habilitar o botão ao final da execução da transformação.
        self.current_widget_form.pushButton.setEnabled(True)

    def call_resultado_derivativo(self):
        # Converter para Tons de cinza
        im = convert_color_para_pb(self.img1)
        # Mostrar apenas imagem convertida no frame
        self.display_on(im,self.ui.imgFrame1)
        # Obter o threshold do lineEdit
        thresh = self.get_number_whithout_error(self.current_widget_form.lineEdit_limiar.text(),'int')
        
        # Calcular o derivativo.
        self.img3 = derivativo(im)
        self.img3 = normalize_uint8(self.img3)

        # Aplicar threshold
        if self.current_widget_form.checkBox_limiar.isChecked():
            self.img3 = convert_pb_para_bin(self.img3, thresh)
        # Preparar para sobrepor borda na imagem
        self.img2 = np.stack([im, im, im],axis=-1)
        self.img2[self.img3>thresh] = np.array([255,0,255]) 
        # mostrar a tela sobreposta no frame maior
        if self.current_widget_form.checkBox_sobrepor.isChecked():
            self.img3, self.img2 = self.img2, self.img3
        # Mostrar na tela
        self. display_on(self.img2, self.ui.imgFrame2)
        self. display_on(self.img3, self.ui.imgFrame3)

    
    def call_resultado_sobel(self):
        # Converter para Tons de cinza
        im = convert_color_para_pb(self.img1)
        # Mostrar apenas imagem convertida no frame
        self.display_on(im,self.ui.imgFrame1)
        # Obter o threshold do lineEdit
        thresh = self.get_number_whithout_error(self.current_widget_form.lineEdit_limiar.text(),'int')
        
        # Calcular o derivativo.
        self.img3 = sobel(im, threshold= thresh, normalizado=True)
        
        # Aplicar threshold
        if self.current_widget_form.checkBox_limiar.isChecked():
            self.img3 = convert_pb_para_bin(self.img3, thresh)
        # Preparar para sobrepor borda na imagem
        self.img2 = np.stack([im, im, im],axis=-1)
        self.img2[self.img3>thresh] = np.array([255,0,255]) 
        # mostrar a tela sobreposta no frame maior
        if self.current_widget_form.checkBox_sobrepor.isChecked():
            self.img3, self.img2 = self.img2, self.img3
        # Mostrar na tela
        self. display_on(self.img2, self.ui.imgFrame2)
        self. display_on(self.img3, self.ui.imgFrame3)

    def call_resultado_kirsch(self):
        # Converter para Tons de cinza
        im = convert_color_para_pb(self.img1)
        # Mostrar apenas imagem convertida no frame
        self.display_on(im,self.ui.imgFrame1)
        # Obter o threshold do lineEdit
        thresh = self.get_number_whithout_error(self.current_widget_form.lineEdit_limiar.text(),'int')
        
        # Calcular o derivativo.
        self.img3 = kirsch(im)
        
        # Aplicar threshold
        if self.current_widget_form.checkBox_limiar.isChecked():
            self.img3 = convert_pb_para_bin(self.img3, thresh)
        # Preparar para sobrepor borda na imagem
        self.img2 = np.stack([im, im, im],axis=-1)
        self.img2[self.img3>thresh] = np.array([255,0,255]) 
        # mostrar a tela sobreposta no frame maior
        if self.current_widget_form.checkBox_sobrepor.isChecked():
            self.img3, self.img2 = self.img2, self.img3
        # Mostrar na tela
        self. display_on(self.img2, self.ui.imgFrame2)
        self. display_on(self.img3, self.ui.imgFrame3)



    ##################################################### 
    ########## funções call_action    ###################
    #####################################################

    def call_action_convert_tc(self):
        self.put_current_widget(ui_convert_grayscale_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_convert_tons_cinza)
    
    def call_action_convert_bin (self):
        self.put_current_widget(ui_convert_bin_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_convert_bin) 

    def call_action_and (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_and)

    def call_action_or (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_or)
 
    def call_action_xor (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_xor)
  
    def call_action_not (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_not)

    def call_action_and_2 (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_and_2)

    def call_action_or_2 (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_or_2)
 
    def call_action_xor_2 (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_xor_2)
 
    def call_action_not_2 (self):
        self.put_current_widget(ui_binary_operations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_not_2)
  
    def call_action_somar_constante(self):
        self.put_current_widget(ui_op_aritmeticas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_somar_constante)
        self.current_widget_form.radioButton_clip.setChecked(True)

    def call_action_somar_imagens(self):
        self.put_current_widget(ui_op_aritmeticas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_somar_imagens)
        self.current_widget_form.lineEdit_constante.setVisible(False)
        self.current_widget_form.label_2.setText(' ')
    
    def call_action_multiplicar_constante(self):
        self.put_current_widget(ui_op_aritmeticas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_multiplicar_constante)

    def call_action_transform(self):
        self.put_current_widget(ui_transformations_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_transform)

    def call_action_derivativo(self):
        self.put_current_widget(ui_bordas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_derivativo)
            
    def call_action_sobel(self):
        self.put_current_widget(ui_bordas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_sobel)

    def call_action_kirsch(self):
        self.put_current_widget(ui_bordas_widget)
        self.current_widget_form.pushButton.clicked.connect(
            self.call_resultado_kirsch)

    
    ################################################
    ############ outras funções ####################
    ################################################

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

            # Ajustar o pixmap para caber no label.
            if img.shape[0] < img.shape[1]:
                #maior largura:
                frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToWidth(frme.width()))
            else:
                #maior altura: 
                frme.setPixmap(QtGui.QPixmap.fromImage(image).scaledToHeight(frme.height()))
        
        s = '{} x {}, dim: {}, dtype: {}, max: {}, min: {}'.format(img.shape[0],img.shape[1],
                                                           len(img.shape),img.dtype, 
                                                           np.max(img),np.min(img))
        frme.setToolTip(s)

    def call_action_openTo1(self):
        # Criar uma instância da janela de seleção
        diag = QtWidgets.QFileDialog()
        if diag.exec_():
            # Coletar e desempacotar a string do caminho.
            [arq] = diag.selectedFiles()
            # Carregar imagem
            self.img1 = abrir_img(arq)
            # Mostrar na barra de status mensagem de abertura
            self.ui.statusbar.showMessage('Arquivo: ' + arq + ' aberto para imagem 1!')  
            # Mostrar no display
            self.display_on(self.img1, self.ui.imgFrame1, 'cor')
        else:
            # Caso o usuário desista, mostrar mensagem na barra de status
            self.ui.statusbar.showMessage('Imagem não selecionada.')
    
    def call_action_openTo2(self):
        # Criar uma instância da janela de seleção
        diag = QtWidgets.QFileDialog()
        # Chamar, caso seja escolhido um arquivo.
        if diag.exec_():
            # Coletar e desempacotar a string do caminho.            
            [arq] = diag.selectedFiles()  
            # Carregar imagem
            self.img2 = abrir_img(arq)
            # Mostrar na barra de status mensagem de abertura
            self.ui.statusbar.showMessage('Arquivo: ' + arq + ' aberto para imagem 2!')
            # Mostrar no display
            self.display_on(self.img2, self.ui.imgFrame2,'cor')

        else:
            # Caso o usuário desista, mostrar mensagem na barra de status
            self.ui.statusbar.showMessage('Imagem não selecionada.')

    def call_action_salvar_resultado(self):
        
        diag = QtWidgets.QFileDialog()
        #  diag.setFileMode()
        
        if diag.exec_():
            print(diag.getSaveFileName())
        else:
            print('ops')


    def call_copy_res_para_prin(self):
        self.img1 = self.img3.copy()
        self.display_on(self.img1,self.ui.imgFrame1)
        
    def call_copy_res_para_aux(self):
        self.img2 = self.img3.copy()
        self.display_on(self.img2,self.ui.imgFrame2)

    def exibe_janela_aviso(self, mensagem:str):
        '''
        Chama um QMessageBox e exibe a mensagem.
        '''
        msgbx = QtWidgets.QMessageBox()
        msgbx.setText(mensagem)
        msgbx.setIcon(QtWidgets.QMessageBox.Warning)
        msgbx.exec()
        self.ui.statusbar.setStatusTip(mensagem)

    def get_number_whithout_error(self, the_string: str, data_type:str, default_return= 0):
        '''
        data_type = 'int', 'float'
        '''
        try:
            if data_type == 'int':
                return int(the_string)
            elif data_type == 'float':
                return float(the_string)
            else:
                return 0
        except:
            print(the_string, 'is not valid for type ',data_type)
            return default_return
        

    def dummy(self):
        pass

    def funcao1(self):
        print('Funcao 1')

    def funcao2(self):
        print('Funcao 2')
        self.exibe_janela_aviso('Olá!')

    def teste_setup(self):
        ''' Função para inicializar a gui em testes.'''
        self.img1 = cv2.imread('yoda.jpg')
        # Remover...
        self.display_on(self.img1, self.ui.imgFrame1,'cor')      

# ===================================================================================
#
# ===================================================================================

def main():
    # Instanciar e inicar a janela.
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    
    # Teste!
    application.teste_setup()

    #Função de teste para carregar automaticamente a img do yoda
    # Permite que a aplicação termine ao fechar a janela.
    sys.exit(app.exec_())

# Este arquivo deve ser rodado como principal.
if __name__ == "__main__":
    main()
