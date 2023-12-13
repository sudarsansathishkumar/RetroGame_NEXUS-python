from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
	def opens(self):
		from SinglePlayer import Ui_PlayerGames
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_PlayerGames()
		self.ui.setupUi(self.window)
		self.window.show()
	def openm(self):
		from MultiPlayer import Ui_MainWindow
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.window.show()
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(900, 650)
		MainWindow.setMinimumSize(QtCore.QSize(900, 650))
		MainWindow.setMaximumSize(QtCore.QSize(900, 650))
		font = QtGui.QFont()
		font.setFamily("Calibri")
		font.setItalic(False)
		MainWindow.setFont(font)
		MainWindow.setStyleSheet("background-color:#ffc266;")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(463, 83, 91, 60))
		font = QtGui.QFont()
		font.setFamily("Segoe Print")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.label.setFont(font)
		self.label.setStyleSheet("background-color:transparent;")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(368, 104, 90, 20))
		font = QtGui.QFont()
		font.setFamily("Segoe Print")
		font.setBold(False)
		font.setWeight(50)
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("background-color:transparent;")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(260, 12, 411, 91))
		font = QtGui.QFont()
		font.setFamily("Segoe Print")
		font.setPointSize(25)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("background-color:transparent;color:#e62e00;")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(40, 440, 221, 191))
		self.label_4.setStyleSheet("background-color: transparent;")
		self.label_4.setText("")
		self.label_4.setPixmap(QtGui.QPixmap("assets/mancala 1 img.png"))
		self.label_4.setScaledContents(True)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(660, 440, 211, 211))
		self.label_5.setText("")
		self.label_5.setPixmap(QtGui.QPixmap("assets/img 2.png"))
		self.label_5.setScaledContents(True)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(300, 460, 331, 161))
		self.label_6.setText("")
		self.label_6.setPixmap(QtGui.QPixmap("assets/angshuman-dhar-pen-fight.png"))
		self.label_6.setScaledContents(True)
		self.label_6.setObjectName("label_6")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.opens())
		self.pushButton.clicked.connect(MainWindow.close)
		self.pushButton.setGeometry(QtCore.QRect(310, 190, 291, 51))
		font = QtGui.QFont()
		font.setFamily("OCR A Std")
		font.setPointSize(12)
		font.setItalic(False)
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
		# self.pushButton.clicked.connect(MainWindow.close)
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openm())
		self.pushButton_2.clicked.connect(MainWindow.close)
		self.pushButton_2.setGeometry(QtCore.QRect(310, 270, 291, 51))
		font = QtGui.QFont()
		font.setFamily("OCR A Std")
		font.setPointSize(12)
		font.setItalic(False)
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
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setGeometry(QtCore.QRect(310, 350, 291, 51))
		font = QtGui.QFont()
		font.setFamily("OCR A Std")
		font.setPointSize(12)
		font.setItalic(False)
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
		self.pushButton_3.clicked.connect(MainWindow.close)
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(840, 20, 41, 41))
		self.label_7.setStyleSheet("background-color:transparent;")
		self.label_7.setText("")
		self.label_7.setPixmap(QtGui.QPixmap("assets/sett.png"))
		self.label_7.setScaledContents(True)
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(830, 70, 61, 61))
		self.label_8.setText("")
		# self.label_8.setPixmap(QtGui.QPixmap("assets/sett.png"))
		self.label_8.setScaledContents(True)
		self.label_8.setObjectName("label_8")
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.p())
		self.pushButton_4.setGeometry(QtCore.QRect(825, 15, 71, 51))
		self.pushButton_4.setStyleSheet("background-color:transparent; outline : none; border : 0px;")
		self.pushButton_4.setText("")
		self.pushButton_4.setObjectName("pushButton_4")
		self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.p())
		self.pushButton_5.setGeometry(QtCore.QRect(827, 75, 71, 51))
		self.pushButton_5.setStyleSheet("background-color:transparent; outline : none; border : 0px;")
		self.pushButton_5.setText("")
		self.pushButton_5.setObjectName("pushButton_5")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionHelp = QtWidgets.QAction(MainWindow)
		self.actionHelp.setObjectName("actionHelp")
		self.actionBenefits = QtWidgets.QAction(MainWindow)
		self.actionBenefits.setObjectName("actionBenefits")		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)		
	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "NEXUS"))
		self.label_2.setText(_translate("MainWindow", "Presented by"))
		self.label_3.setText(_translate("MainWindow", "Classic 90\'s Games"))
		self.pushButton.setText(_translate("MainWindow", "1 - Player"))
		self.pushButton_2.setText(_translate("MainWindow", "2 - Players"))
		self.pushButton_3.setText(_translate("MainWindow", "Quit"))
		self.actionHelp.setText(_translate("MainWindow", "Help"))
		self.actionBenefits.setText(_translate("MainWindow", "Benefits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
