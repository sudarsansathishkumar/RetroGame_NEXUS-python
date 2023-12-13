from PyQt5 import QtCore, QtGui, QtWidgets
import random

count = 0
Aplay = 1 # A is playing
Bplay = -1 # B is waiting
class Ui_MainWindow(object):
    def fr(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def matchless(self, val):
        global count
        global Aplay
        global Bplay

        if count - val <= 0:
            for i in range(count):
                self.ls[i].setPixmap(QtGui.QPixmap("assets/blank.png"))
            from NimStatus import Ui_Form
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.window)
            if Aplay == 1:
                self.ui.label.setText("Player 2 wins")
            else:
                self.ui.label.setText("Player 1 wins")
            self.dummy.click()
            self.window.show()
        else:
            for i in range(count - val, count):
                self.ls[i].setPixmap(QtGui.QPixmap("assets/blank.png"))
            count -= val
            Aplay *= -1
            Bplay *= -1
        
        if Aplay == 1:
            self.playername.setText("Player 1")
        elif Bplay == 1:
            self.playername.setText("Player 2")

    def ranmatch(self):
        global count
        num = random.randint(10, 30)
        count = num
        self.generatedvalue.setText(str(num))
        self.playername.setText("Player 1")
        for i in range(num):
            self.ls[i].setPixmap(QtGui.QPixmap("assets/stick.png"))
        for i in range(num, 30):
            self.ls[i].setPixmap(QtGui.QPixmap("assets/blank.png"))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 900)
        MainWindow.setMinimumSize(QtCore.QSize(950, 900))
        MainWindow.setMaximumSize(QtCore.QSize(950, 900))
        MainWindow.setStyleSheet("background-color:skyblue;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(105, 665, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.matchless(3))
        self.three.setGeometry(QtCore.QRect(535, 795, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white; outline:none; border:none; border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.three.setObjectName("three")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(545, 675, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Quit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.fr())
        self.Quit.clicked.connect(MainWindow.close)
        self.Quit.setGeometry(QtCore.QRect(115, 805, 121, 41))
        self.Quit.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:red;\n"
"    outline:none;\n"
"    border-radius:10px;\n"
"    border:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:red;\n"
"    color:white;\n"
"    border:1px solid white;\n"
"}")
        self.Quit.setObjectName("Quit")
        self.Quit.clicked.connect(MainWindow.close)
        self.playername = QtWidgets.QLabel(self.centralwidget)
        self.playername.setGeometry(QtCore.QRect(235, 675, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.playername.setFont(font)
        self.playername.setStyleSheet("color:red;")
        self.playername.setObjectName("playername")
        self.generatedvalue = QtWidgets.QLabel(self.centralwidget)
        self.generatedvalue.setGeometry(QtCore.QRect(275, 749, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.generatedvalue.setFont(font)
        self.generatedvalue.setObjectName("generatedvalue")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.matchless(2))
        self.two.setGeometry(QtCore.QRect(655, 725, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white; outline:none; border:none; border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.two.setObjectName("two")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(115, 735, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.Restart = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.ranmatch())
        self.Restart.setGeometry(QtCore.QRect(275, 805, 121, 41))
        self.Restart.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:red;\n"
"    outline:none;\n"
"    border-radius:10px;\n"
"    border:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:red;\n"
"    color:white;\n"
"    border:1px solid white;\n"
"}")
        self.Restart.setObjectName("Restart")
        self.dummy = QtWidgets.QPushButton(self.centralwidget)
        self.dummy.clicked.connect(MainWindow.close)
        self.dummy.setStyleSheet("background-color:transparent; outline:none; border:none;")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.matchless(1))
        self.one.setGeometry(QtCore.QRect(405, 725, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white; outline:none; border:none; border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.one.setObjectName("one")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 45, 901, 601))
        self.label.setStyleSheet("background-color:white;border-radius:15px;border:none; outline:none;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(65, 75, 23, 171))
        self.l1.setStyleSheet("background-color:white;")
        self.l1.setText("")
        self.l1.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l1.setScaledContents(True)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(140, 77, 23, 171))
        self.l2.setStyleSheet("background-color:white;")
        self.l2.setText("")
        self.l2.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l2.setScaledContents(True)
        self.l2.setObjectName("l2")
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(319, 78, 23, 171))
        self.l4.setStyleSheet("background-color:white;")
        self.l4.setText("")
        self.l4.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l4.setScaledContents(True)
        self.l4.setObjectName("l4")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(230, 79, 23, 171))
        self.l3.setStyleSheet("background-color:white;")
        self.l3.setText("")
        self.l3.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l3.setScaledContents(True)
        self.l3.setObjectName("l3")
        self.l6 = QtWidgets.QLabel(self.centralwidget)
        self.l6.setGeometry(QtCore.QRect(508, 79, 23, 171))
        self.l6.setStyleSheet("background-color:white;")
        self.l6.setText("")
        self.l6.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l6.setScaledContents(True)
        self.l6.setObjectName("l6")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(412, 79, 23, 171))
        self.l5.setStyleSheet("background-color:white;")
        self.l5.setText("")
        self.l5.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l5.setScaledContents(True)
        self.l5.setObjectName("l5")
        self.l8 = QtWidgets.QLabel(self.centralwidget)
        self.l8.setGeometry(QtCore.QRect(695, 82, 23, 171))
        self.l8.setStyleSheet("background-color:white;")
        self.l8.setText("")
        self.l8.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l8.setScaledContents(True)
        self.l8.setObjectName("l8")
        self.l7 = QtWidgets.QLabel(self.centralwidget)
        self.l7.setGeometry(QtCore.QRect(605, 81, 23, 171))
        self.l7.setStyleSheet("background-color:white;")
        self.l7.setText("")
        self.l7.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l7.setScaledContents(True)
        self.l7.setObjectName("l7")
        self.l10 = QtWidgets.QLabel(self.centralwidget)
        self.l10.setGeometry(QtCore.QRect(869, 83, 23, 171))
        self.l10.setStyleSheet("background-color:white;")
        self.l10.setText("")
        self.l10.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l10.setScaledContents(True)
        self.l10.setObjectName("l10")
        self.l9 = QtWidgets.QLabel(self.centralwidget)
        self.l9.setGeometry(QtCore.QRect(783, 81, 23, 171))
        self.l9.setStyleSheet("background-color:white;")
        self.l9.setText("")
        self.l9.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l9.setScaledContents(True)
        self.l9.setObjectName("l9")
        self.l13 = QtWidgets.QLabel(self.centralwidget)
        self.l13.setGeometry(QtCore.QRect(232, 263, 23, 171))
        self.l13.setStyleSheet("background-color:white;")
        self.l13.setText("")
        self.l13.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l13.setScaledContents(True)
        self.l13.setObjectName("l13")
        self.l14 = QtWidgets.QLabel(self.centralwidget)
        self.l14.setGeometry(QtCore.QRect(321, 262, 23, 171))
        self.l14.setStyleSheet("background-color:white;")
        self.l14.setText("")
        self.l14.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l14.setScaledContents(True)
        self.l14.setObjectName("l14")
        self.l15 = QtWidgets.QLabel(self.centralwidget)
        self.l15.setGeometry(QtCore.QRect(414, 263, 23, 171))
        self.l15.setStyleSheet("background-color:white;")
        self.l15.setText("")
        self.l15.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l15.setScaledContents(True)
        self.l15.setObjectName("l15")
        self.l17 = QtWidgets.QLabel(self.centralwidget)
        self.l17.setGeometry(QtCore.QRect(607, 265, 23, 171))
        self.l17.setStyleSheet("background-color:white;")
        self.l17.setText("")
        self.l17.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l17.setScaledContents(True)
        self.l17.setObjectName("l17")
        self.l12 = QtWidgets.QLabel(self.centralwidget)
        self.l12.setGeometry(QtCore.QRect(142, 261, 23, 171))
        self.l12.setStyleSheet("background-color:white;")
        self.l12.setText("")
        self.l12.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l12.setScaledContents(True)
        self.l12.setObjectName("l12")
        self.l16 = QtWidgets.QLabel(self.centralwidget)
        self.l16.setGeometry(QtCore.QRect(510, 263, 23, 171))
        self.l16.setStyleSheet("background-color:white;")
        self.l16.setText("")
        self.l16.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l16.setScaledContents(True)
        self.l16.setObjectName("l16")
        self.l18 = QtWidgets.QLabel(self.centralwidget)
        self.l18.setGeometry(QtCore.QRect(697, 266, 23, 171))
        self.l18.setStyleSheet("background-color:white;")
        self.l18.setText("")
        self.l18.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l18.setScaledContents(True)
        self.l18.setObjectName("l18")
        self.l11 = QtWidgets.QLabel(self.centralwidget)
        self.l11.setGeometry(QtCore.QRect(67, 259, 23, 171))
        self.l11.setStyleSheet("background-color:white;")
        self.l11.setText("")
        self.l11.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l11.setScaledContents(True)
        self.l11.setObjectName("l11")
        self.l20 = QtWidgets.QLabel(self.centralwidget)
        self.l20.setGeometry(QtCore.QRect(871, 267, 23, 171))
        self.l20.setStyleSheet("background-color:white;")
        self.l20.setText("")
        self.l20.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l20.setScaledContents(True)
        self.l20.setObjectName("l20")
        self.l19 = QtWidgets.QLabel(self.centralwidget)
        self.l19.setGeometry(QtCore.QRect(785, 265, 23, 171))
        self.l19.setStyleSheet("background-color:white;")
        self.l19.setText("")
        self.l19.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l19.setScaledContents(True)
        self.l19.setObjectName("l19")
        self.l23 = QtWidgets.QLabel(self.centralwidget)
        self.l23.setGeometry(QtCore.QRect(232, 443, 23, 171))
        self.l23.setStyleSheet("background-color:white;")
        self.l23.setText("")
        self.l23.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l23.setScaledContents(True)
        self.l23.setObjectName("l23")
        self.l24 = QtWidgets.QLabel(self.centralwidget)
        self.l24.setGeometry(QtCore.QRect(321, 442, 23, 171))
        self.l24.setStyleSheet("background-color:white;")
        self.l24.setText("")
        self.l24.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l24.setScaledContents(True)
        self.l24.setObjectName("l24")
        self.l25 = QtWidgets.QLabel(self.centralwidget)
        self.l25.setGeometry(QtCore.QRect(414, 443, 23, 171))
        self.l25.setStyleSheet("background-color:white;")
        self.l25.setText("")
        self.l25.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l25.setScaledContents(True)
        self.l25.setObjectName("l25")
        self.l27 = QtWidgets.QLabel(self.centralwidget)
        self.l27.setGeometry(QtCore.QRect(607, 445, 23, 171))
        self.l27.setStyleSheet("background-color:white;")
        self.l27.setText("")
        self.l27.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l27.setScaledContents(True)
        self.l27.setObjectName("l27")
        self.l22 = QtWidgets.QLabel(self.centralwidget)
        self.l22.setGeometry(QtCore.QRect(142, 441, 23, 171))
        self.l22.setStyleSheet("background-color:white;")
        self.l22.setText("")
        self.l22.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l22.setScaledContents(True)
        self.l22.setObjectName("l22")
        self.l26 = QtWidgets.QLabel(self.centralwidget)
        self.l26.setGeometry(QtCore.QRect(510, 443, 23, 171))
        self.l26.setStyleSheet("background-color:white;")
        self.l26.setText("")
        self.l26.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l26.setScaledContents(True)
        self.l26.setObjectName("l26")
        self.l28 = QtWidgets.QLabel(self.centralwidget)
        self.l28.setGeometry(QtCore.QRect(697, 446, 23, 171))
        self.l28.setStyleSheet("background-color:white;")
        self.l28.setText("")
        self.l28.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l28.setScaledContents(True)
        self.l28.setObjectName("l28")
        self.l21 = QtWidgets.QLabel(self.centralwidget)
        self.l21.setGeometry(QtCore.QRect(67, 439, 23, 171))
        self.l21.setStyleSheet("background-color:white;")
        self.l21.setText("")
        self.l21.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l21.setScaledContents(True)
        self.l21.setObjectName("l21")
        self.l30 = QtWidgets.QLabel(self.centralwidget)
        self.l30.setGeometry(QtCore.QRect(871, 447, 23, 171))
        self.l30.setStyleSheet("background-color:white;")
        self.l30.setText("")
        self.l30.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l30.setScaledContents(True)
        self.l30.setObjectName("l30")
        self.l29 = QtWidgets.QLabel(self.centralwidget)
        self.l29.setGeometry(QtCore.QRect(785, 445, 23, 171))
        self.l29.setStyleSheet("background-color:white;")
        self.l29.setText("")
        self.l29.setPixmap(QtGui.QPixmap("assets/blank.png"))
        self.l29.setScaledContents(True)
        self.l29.setObjectName("l29")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(890, 0, 41, 41))
        self.label_35.setStyleSheet("background-color:transparent;")
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("assets/info.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(890, 0, 41, 41))
        self.info.setStyleSheet("border:none;background-color:transparent;")
        self.info.setText("")
        self.info.setObjectName("info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ls = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10, self.l11, self.l12, self.l13, self.l14, self.l15, self.l16, self.l17, self.l18, self.l19, self.l20, self.l21, self.l22, self.l23, self.l24, self.l25, self.l26, self.l27, self.l28, self.l29, self.l30]
        self.ranmatch()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Chance for :"))
        self.three.setText(_translate("MainWindow", "3"))
        self.label_3.setText(_translate("MainWindow", "Select the number of sticks"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.playername.setText(_translate("MainWindow", "Player 1"))
        self.generatedvalue.setText(_translate("MainWindow", "10"))
        self.two.setText(_translate("MainWindow", "2"))
        self.label_4.setText(_translate("MainWindow", "The randomly generated value is :"))
        self.Restart.setText(_translate("MainWindow", "Restart"))
        self.one.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
