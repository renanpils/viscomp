# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/ui_dilatacao_erosao_widget.ui'
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
        self.labelOperacao = QtWidgets.QLabel(Form)
        self.labelOperacao.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.labelOperacao.setObjectName("labelOperacao")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 75, 23))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(200, 20, 191, 91))
        self.plainTextEdit.setToolTip("")
        self.plainTextEdit.setStatusTip("")
        self.plainTextEdit.setWhatsThis("")
        self.plainTextEdit.setAccessibleName("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 0, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_x = QtWidgets.QLineEdit(Form)
        self.lineEdit_x.setGeometry(QtCore.QRect(280, 120, 31, 20))
        self.lineEdit_x.setToolTip("")
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.lineEdit_y = QtWidgets.QLineEdit(Form)
        self.lineEdit_y.setGeometry(QtCore.QRect(320, 120, 31, 20))
        self.lineEdit_y.setToolTip("")
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.lineEdit_limiar = QtWidgets.QLineEdit(Form)
        self.lineEdit_limiar.setGeometry(QtCore.QRect(60, 70, 51, 21))
        self.lineEdit_limiar.setObjectName("lineEdit_limiar")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(170, 10, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelOperacao.setText(_translate("Form", "Operacão"))
        self.pushButton.setText(_translate("Form", "Resultado"))
        self.plainTextEdit.setPlainText(_translate("Form", "[[0,1,0],\n"
" [1,0,1],\n"
" [0,1,0]]"))
        self.label.setText(_translate("Form", "Digite o elemento estruturante:"))
        self.label_2.setText(_translate("Form", "Centro (x,y):"))
        self.lineEdit_x.setText(_translate("Form", "1"))
        self.lineEdit_y.setText(_translate("Form", "1"))
        self.lineEdit_limiar.setText(_translate("Form", "127"))
        self.label_3.setText(_translate("Form", "Limiar:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

