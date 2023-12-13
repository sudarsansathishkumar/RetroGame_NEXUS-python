from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_PlayerGames(object):
    def openhc(self):
        from HandCricket import Ui_HandCricket
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HandCricket()
        self.ui.setupUi(self.window)
        self.window.show()

    def openne(self):
        from NewOddEven import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openpk(self):
        os.system('pallanguli.py')

    def openf(self):
        os.system('flames1.py')

    def setupUi(self, PlayerGames):
        PlayerGames.setObjectName("PlayerGames")
        PlayerGames.resize(900, 650)
        PlayerGames.setMinimumSize(QtCore.QSize(900, 650))
        PlayerGames.setMaximumSize(QtCore.QSize(900, 650))
        PlayerGames.setStyleSheet("background-color:#ffc266;")
        self.centralwidget = QtWidgets.QWidget(PlayerGames)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openhc())
        self.pushButton.setGeometry(QtCore.QRect(304, 150, 331, 71))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openf())
        self.pushButton_2.setGeometry(QtCore.QRect(304, 500, 331, 71))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openne())
        self.pushButton_3.setGeometry(QtCore.QRect(304, 260, 331, 71))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openpk())
        self.pushButton_4.setGeometry(QtCore.QRect(304, 380, 331, 71))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 40, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 221, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("F:/im/b0e09ee13009cdcc90b0c18a20143bb3.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 100, 201, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("F:/im/images.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 430, 55, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 350, 191, 181))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("F:/im/mancala 1 img.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 360, 221, 161))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("F:/im/v4-460px-Play-_Flame_-Step-8-Version-2.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        PlayerGames.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlayerGames)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        PlayerGames.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlayerGames)
        self.statusbar.setObjectName("statusbar")
        PlayerGames.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(PlayerGames.close)
        self.pushButton_2.clicked.connect(PlayerGames.close)
        self.pushButton_3.clicked.connect(PlayerGames.close)
        self.pushButton_4.clicked.connect(PlayerGames.close)

        self.retranslateUi(PlayerGames)
        QtCore.QMetaObject.connectSlotsByName(PlayerGames)

    def retranslateUi(self, PlayerGames):
        _translate = QtCore.QCoreApplication.translate
        PlayerGames.setWindowTitle(_translate("PlayerGames", "1 Player Games - Nexus"))
        self.pushButton.setText(_translate("PlayerGames", "Hand Cricket"))
        self.pushButton_2.setText(_translate("PlayerGames", "Flames"))
        self.pushButton_3.setText(_translate("PlayerGames", "Othaiya Rettaya"))
        self.pushButton_4.setText(_translate("PlayerGames", "Pallankuzhi"))
        self.label.setText(_translate("PlayerGames", "Single Player Games"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlayerGames = QtWidgets.QMainWindow()
    ui = Ui_PlayerGames()
    ui.setupUi(PlayerGames)
    PlayerGames.show()
    sys.exit(app.exec_())
