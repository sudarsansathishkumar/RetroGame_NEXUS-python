from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def opennim(self):
        from Nim import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openttt(self):
        import os
        os.system('tictac.py')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        MainWindow.setStyleSheet("background-color:#ffc266;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openttt())
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 270, 331, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:black;\n"
"    padding:3px;\n"
"    outline:none;\n"
"    border:1px solid white;\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #b3ecff;\n"
"    border:1px solid skyblue;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.opennim())
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.setGeometry(QtCore.QRect(280, 160, 331, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:black;\n"
"    padding:3px;\n"
"    outline:none;\n"
"    border:1px solid white;\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #b3ecff;\n"
"    border:1px solid skyblue;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 510, 331, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:black;\n"
"    padding:3px;\n"
"    outline:none;\n"
"    border:1px solid white;\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #b3ecff;\n"
"    border:1px solid skyblue;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 390, 331, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:black;\n"
"    padding:3px;\n"
"    outline:none;\n"
"    border:1px solid white;\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #b3ecff;\n"
"    border:1px solid skyblue;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 360, 211, 211))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("assets/img 2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MultiPlayer Games"))
        self.pushButton_3.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.pushButton.setText(_translate("MainWindow", "Nim"))
        self.pushButton_2.setText(_translate("MainWindow", "Thaayam"))
        self.pushButton_4.setText(_translate("MainWindow", "Aadu puli aatam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
