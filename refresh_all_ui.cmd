@echo off

echo "Refreshing all ui's"

:: Gerando ou atualizando .py's . . ."

pyuic5 -x ui_files/ui_mainWindow.ui -o ui_files/ui_mainWindow.py
pyuic5 -x ui_files/ui_template_widget.ui -o ui_files/ui_template.py
pyuic5 -x ui_files/ui_start_widget.ui -o ui_files/ui_start_widget.py
pyuic5 -x ui_files/ui_transformations_widget.ui -o ui_files/ui_transformations_widget.py
pyuic5 -x ui_files/ui_bordas_widget.ui -o ui_files/ui_bordas_widget.py
pyuic5 -x ui_files/ui_convert_bin_widget.ui -o ui_files/ui_convert_bin_widget.py
pyuic5 -x ui_files/ui_convert_grayscale_widget.ui -o ui_files/ui_convert_grayscale_widget.py
pyuic5 -x ui_files/ui_binary_operations_widget.ui -o ui_files/ui_binary_operations_widget.py
pyuic5 -x ui_files/ui_op_aritmeticas_widget.ui -o ui_files/ui_op_aritmeticas_widget.py

pyuic5 -x ui_files/ui_histograma_widget.ui -o ui_files/ui_histograma_widget.py
pyuic5 -x ui_files/ui_equalizacao_histograma_widget.ui -o ui_files/ui_equalizacao_histograma_widget.py
pyuic5 -x ui_files/ui_limiarizar_widget.ui -o ui_files/ui_limiarizar_widget.py

pyuic5 -x ui_files/ui_gaussiano_widget.ui -o ui_files/ui_gaussiano_widget.py
pyuic5 -x ui_files/ui_laplaciano_widget.ui -o ui_files/ui_laplaciano_widget.py
pyuic5 -x ui_files/ui_media_widget.ui -o ui_files/ui_media_widget.py
pyuic5 -x ui_files/ui_mediana_widget.ui -o ui_files/ui_mediana_widget.py
pyuic5 -x ui_files/ui_passa_altas_widget.ui -o ui_files/ui_passa_altas_widget.py

pyuic5 -x ui_files/ui_dilatacao_erosao_widget.ui -o ui_files/ui_dilatacao_erosao_widget.py
::pyuic5 -x ui_files/ui_erosao_widget.ui -o ui_files/ui_erosao_widget.py
pyuic5 -x ui_files/ui_extracao_widget.ui -o ui_files/ui_extracao_widget.py
echo "Done! "
pause