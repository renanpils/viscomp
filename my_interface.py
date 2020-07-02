'''
Este arquivo importa os elementos necessários para rodar a GUI do aplicativo

Suas dependências estão contidas no diretório ui_files
'''

from PyQt5 import QtGui, QtCore, QtWidgets


from   ui_files.ui_mainWindow import*
import ui_files.ui_template  as ui_template
import ui_files.ui_start_widget  as ui_start_widget
import ui_files.ui_transformations_widget  as ui_transformations_widget
import ui_files.ui_bordas_widget  as ui_bordas_widget
import ui_files.ui_convert_bin_widget  as ui_convert_bin_widget
import ui_files.ui_convert_grayscale_widget  as ui_convert_grayscale_widget
import ui_files.ui_binary_operations_widget  as ui_binary_operations_widget
import ui_files.ui_op_aritmeticas_widget  as ui_op_aritmeticas_widget
import ui_files.ui_histograma_widget as ui_histograma_widget
import ui_files.ui_equalizacao_histograma_widget as ui_equalizacao_histograma_widget
import ui_files.ui_limiarizar_widget as ui_limiarizar_widget

import ui_files.ui_gaussiano_widget as ui_gaussiano_widget
import ui_files.ui_laplaciano_widget as ui_laplaciano_widget
import ui_files.ui_media_widget as ui_media_widget
import ui_files.ui_mediana_widget as ui_mediana_widget
import ui_files.ui_passa_altas_widget as ui_passa_altas_widget

import ui_files.ui_dilatacao_erosao_widget as ui_dilatacao_erosao_widget
# import ui_files.ui_erosao_widget as ui_erosao_widget
import ui_files.ui_extracao_widget as ui_extracao_widget