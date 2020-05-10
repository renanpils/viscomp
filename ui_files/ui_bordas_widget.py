# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/ui_bordas_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 150)
        Form.setMinimumSize(QtCore.QSize(410, 150))
        Form.setMaximumSize(QtCore.QSize(420, 180))
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(0, 50, 100);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.checkBox_sobrepor = QtWidgets.QCheckBox(Form)
        self.checkBox_sobrepor.setGeometry(QtCore.QRect(210, 100, 181, 20))
        self.checkBox_sobrepor.setObjectName("checkBox_sobrepor")
        self.checkBox_limiar = QtWidgets.QCheckBox(Form)
        self.checkBox_limiar.setGeometry(QtCore.QRect(210, 70, 70, 17))
        self.checkBox_limiar.setChecked(True)
        self.checkBox_limiar.setObjectName("checkBox_limiar")
        self.lineEdit_limiar = QtWidgets.QLineEdit(Form)
        self.lineEdit_limiar.setGeometry(QtCore.QRect(270, 70, 91, 20))
        self.lineEdit_limiar.setObjectName("lineEdit_limiar")

        self.retranslateUi(Form)
        self.checkBox_limiar.toggled['bool'].connect(self.lineEdit_limiar.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Resultado"))
        self.checkBox_sobrepor.setText(_translate("Form", "Sobrepor bordas na imagem"))
        self.checkBox_limiar.setText(_translate("Form", "Limiar:"))
        self.lineEdit_limiar.setText(_translate("Form", "127"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

