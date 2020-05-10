# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/ui_op_aritmeticas_widget.ui'
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
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 75, 23))
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
        self.radioButton_normalizar = QtWidgets.QRadioButton(Form)
        self.radioButton_normalizar.setGeometry(QtCore.QRect(220, 110, 82, 17))
        self.radioButton_normalizar.setChecked(True)
        self.radioButton_normalizar.setObjectName("radioButton_normalizar")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_normalizar)
        self.radioButton_clip = QtWidgets.QRadioButton(Form)
        self.radioButton_clip.setGeometry(QtCore.QRect(320, 110, 82, 17))
        self.radioButton_clip.setObjectName("radioButton_clip")
        self.buttonGroup.addButton(self.radioButton_clip)
        self.lineEdit_constante = QtWidgets.QLineEdit(Form)
        self.lineEdit_constante.setGeometry(QtCore.QRect(90, 20, 61, 20))
        self.lineEdit_constante.setObjectName("lineEdit_constante")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Resultado"))
        self.radioButton_normalizar.setText(_translate("Form", "Normalizar"))
        self.radioButton_clip.setText(_translate("Form", "Clip"))
        self.lineEdit_constante.setText(_translate("Form", "1"))
        self.label_2.setText(_translate("Form", "Constante:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

