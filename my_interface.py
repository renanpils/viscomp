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


''' Considerações finais:
Comando para converter .ui para .pi:

pyuic5 -x ui-files/ui_mainWindow.ui -o ui_mainWindow.py
pyuic5 -x ui-files/ui_template_widget.ui -o ui_template.py
pyuic5 -x ui-files/ui_start_widget.ui -o ui_start_widget.py
pyuic5 -x ui-files/ui_transformations_widget.ui -o ui_transformations_widget.py
pyuic5 -x ui-files/ui_bordas_widget.ui -o ui_bordas_widget.py
pyuic5 -x ui-files/ui_convert_bin_widget.ui -o ui_convert_bin_widget.py
pyuic5 -x ui-files/ui_convert_grayscale_widget.ui -o ui_convert_grayscale_widget.py
pyuic5 -x ui-files/ui_binary_operations_widget.ui -o ui_binary_operations_widget.py

'''