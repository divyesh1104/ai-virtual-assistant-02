# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edithui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edith(object):
    def setupUi(self, edith):
        edith.setObjectName("edith")
        edith.resize(911, 628)
        edith.setWindowOpacity(0.0)
        self.edithui = QtWidgets.QLabel(edith)
        self.edithui.setGeometry(QtCore.QRect(-4, -8, 921, 641))
        self.edithui.setText("")
        self.edithui.setPixmap(QtGui.QPixmap("../7LP8.gif"))
        self.edithui.setScaledContents(True)
        self.edithui.setObjectName("edithui")
        self.label_2 = QtWidgets.QLabel(edith)
        self.label_2.setGeometry(QtCore.QRect(6, 2, 391, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../VID-1608093668227.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(edith)
        self.label_3.setGeometry(QtCore.QRect(500, 20, 181, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../download.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(edith)
        self.label_4.setGeometry(QtCore.QRect(680, 20, 181, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../download.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(edith)
        self.pushButton.setGeometry(QtCore.QRect(650, 490, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(edith)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 490, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(edith)
        QtCore.QMetaObject.connectSlotsByName(edith)

    def retranslateUi(self, edith):
        _translate = QtCore.QCoreApplication.translate
        edith.setWindowTitle(_translate("edith", "edith"))
        self.pushButton.setText(_translate("edith", "run"))
        self.pushButton_2.setText(_translate("edith", "exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edith = QtWidgets.QDialog()
    ui = Ui_edith()
    ui.setupUi(edith)
    edith.show()
    sys.exit(app.exec_())
