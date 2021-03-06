# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fridayUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FridayAI(object):
    def setupUi(self, FridayAI):
        FridayAI.setObjectName("FridayAI")
        FridayAI.resize(1133, 931)
        self.centralwidget = QtWidgets.QWidget(FridayAI)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, -10, 1851, 951))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("Black_Template.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.aiHead = QtWidgets.QLabel(self.centralwidget)
        self.aiHead.setGeometry(QtCore.QRect(430, -30, 711, 551))
        self.aiHead.setText("")
        self.aiHead.setPixmap(QtGui.QPixmap("head.gif"))
        self.aiHead.setObjectName("aiHead")
        self.SmAi = QtWidgets.QLabel(self.centralwidget)
        self.SmAi.setGeometry(QtCore.QRect(-180, 200, 551, 341))
        self.SmAi.setText("")
        self.SmAi.setPixmap(QtGui.QPixmap("alexa.gif"))
        self.SmAi.setObjectName("SmAi")
        self.SysIn = QtWidgets.QLabel(self.centralwidget)
        self.SysIn.setGeometry(QtCore.QRect(20, 10, 511, 191))
        self.SysIn.setText("")
        self.SysIn.setPixmap(QtGui.QPixmap("intial.gif"))
        self.SysIn.setObjectName("SysIn")
        self.dataAi = QtWidgets.QLabel(self.centralwidget)
        self.dataAi.setGeometry(QtCore.QRect(40, 640, 431, 211))
        self.dataAi.setText("")
        self.dataAi.setPixmap(QtGui.QPixmap("code.gif"))
        self.dataAi.setObjectName("dataAi")
        self.StartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartBtn.setGeometry(QtCore.QRect(630, 810, 161, 51))
        self.StartBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Modern No. 20\";\n"
"background-color: rgb(0, 85, 255);")
        self.StartBtn.setObjectName("StartBtn")
        self.StopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StopBtn.setGeometry(QtCore.QRect(880, 810, 161, 51))
        self.StopBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Modern No. 20\";\n"
"background-color: rgb(0, 85, 255);")
        self.StopBtn.setObjectName("StopBtn")
        self.waveai = QtWidgets.QLabel(self.centralwidget)
        self.waveai.setGeometry(QtCore.QRect(420, 500, 801, 201))
        self.waveai.setText("")
        self.waveai.setPixmap(QtGui.QPixmap("wave.gif"))
        self.waveai.setObjectName("waveai")
        FridayAI.setCentralWidget(self.centralwidget)

        self.retranslateUi(FridayAI)
        QtCore.QMetaObject.connectSlotsByName(FridayAI)

    def retranslateUi(self, FridayAI):
        _translate = QtCore.QCoreApplication.translate
        FridayAI.setWindowTitle(_translate("FridayAI", "MainWindow"))
        self.StartBtn.setText(_translate("FridayAI", "START"))
        self.StopBtn.setText(_translate("FridayAI", "STOP"))

if __name__ =="__main__":
    import  sys
    app = QtWidgets.QApplication(sys.argv)
    FridayUI = QtWidgets.QMainWindow()
    ui = Ui_FridayAI()
    ui.setupUi(FridayUI)
    FridayUI.show()
    sys.exit(app.exec_())
