from PyQt5 import QtCore, QtGui, QtWidgets
import random

user = 50
pc = 50
switch = 1

class Ui_MainWindow(object):
    def fr(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def update(self):
        global switch, pc, user
        self.score.setText(str(user))

        if pc <= 0 or user <= 0:
            print("pop up comes here")
        if switch == 1:
            self.pushButton.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.even.setEnabled(True)
            self.odd.setEnabled(True)
            self.label_2.setText("It's turn for Player 1")
            
        elif switch == -1:
            
            self.pushButton.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.even.setEnabled(False)
            self.odd.setEnabled(False)
            self.label_2.setText("It's turn for Player 2")
            
    def getinp(self):
        global switch, pc, user
        inp = int(self.lineEdit.text())
        op = random.randint(0, 1)
        if op == 0:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/even.png"))
            if inp % 2 == 0:
                self.userout.setPixmap(QtGui.QPixmap("assets/even.png"))
                pc += inp
                user -= inp
            else:
                self.userout.setPixmap(QtGui.QPixmap("assets/odd.png"))
                pc -= inp
                user += inp
            switch *= -1
        else:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/odd.png"))
            if inp % 2 == 0:
                self.userout.setPixmap(QtGui.QPixmap("assets/even.png"))
                pc -= inp
                user += inp
            else:
                self.userout.setPixmap(QtGui.QPixmap("assets/odd.png"))
                pc += inp
                user -= inp
            switch *= -1

    def evens(self):
        global pc, user, switch
        self.userout.setPixmap(QtGui.QPixmap("assets/even.png"))
        cpval = random.randint(1, pc)
        if cpval % 2 == 0:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/even.png"))
            pc -= cpval
            user += cpval
        else:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/odd.png"))
            pc += cpval
            user -= cpval
        switch *= -1
        self.update()
    def odds(self):
        global pc, user, switch
        self.userout.setPixmap(QtGui.QPixmap("assets/odd.png"))
        cpval = random.randint(1, pc)
        if cpval % 2 != 0:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/odd.png"))
            pc -= cpval
            user += cpval
        else:
            self.cmpout.setPixmap(QtGui.QPixmap("assets/even.png"))
            pc += cpval
            user -= cpval
        switch *= -1
        self.update()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(600, 900))
        MainWindow.setStyleSheet("background-color:skyblue;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(539, 13, 41, 41))
        self.info.setStyleSheet("background-color:transparent;border:none;outline:none;")
        self.info.setText("")
        self.info.setObjectName("info")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(539, 13, 41, 41))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("assets/info.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.cmpout = QtWidgets.QLabel(self.centralwidget)
        self.cmpout.setGeometry(QtCore.QRect(40, 80, 521, 221))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cmpout.setFont(font)
        self.cmpout.setStyleSheet("background-color:white;border-radius:10px")
        self.cmpout.setText("")
        self.cmpout.setPixmap(QtGui.QPixmap("assets/closedhandnew2.png"))
        self.cmpout.setAlignment(QtCore.Qt.AlignCenter)
        self.cmpout.setObjectName("cmpout")
        self.userout = QtWidgets.QLabel(self.centralwidget)
        self.userout.setGeometry(QtCore.QRect(40, 370, 521, 221))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.userout.setFont(font)
        self.userout.setStyleSheet("background-color:white;border-radius:10px")
        self.userout.setText("")
        self.userout.setPixmap(QtGui.QPixmap("assets/closedhandnew.png"))
        self.userout.setAlignment(QtCore.Qt.AlignCenter)
        self.userout.setObjectName("userout")
        self.even = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.evens())
        self.even.setGeometry(QtCore.QRect(67, 609, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.even.setFont(font)
        self.even.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white; border:none; outline:none;color:blue;border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:blue; color:white; border:1px solid white;\n"
"}")
        self.even.setObjectName("even")
        self.odd = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.odds())
        self.odd.setGeometry(QtCore.QRect(70, 690, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.odd.setFont(font)
        self.odd.setStyleSheet("QPushButton\n"
"{\n"
"background-color:white; border:none; outline:none;color:blue;border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:blue; color:white; border:1px solid white;\n"
"}")
        self.odd.setObjectName("odd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 680, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Quit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.fr())
        self.Quit.clicked.connect(MainWindow.close)
        self.Quit.setGeometry(QtCore.QRect(329, 789, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Quit.setFont(font)
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
        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setGeometry(QtCore.QRect(69, 789, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.restart.setFont(font)
        self.restart.setStyleSheet("QPushButton\n"
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
        self.restart.setObjectName("restart")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(410, 720, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.score.setFont(font)
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.getinp())
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(500, 620, 51, 41))
        self.pushButton.setStyleSheet("\n"
"background-color:#cacce8; border:none; outline:none;border-radius:10px;color:black;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(330, 620, 161, 41))
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"background-color:#cacce8; border:none; outline:none;border-radius:10px;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"border:1px solid blue;\n"
"}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 320, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pro H")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Odd or Even - Nexus"))
        self.even.setText(_translate("MainWindow", "EVEN"))
        self.odd.setText(_translate("MainWindow", "ODD"))
        self.label.setText(_translate("MainWindow", "Your score"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.restart.setText(_translate("MainWindow", "Restart"))
        self.score.setText(_translate("MainWindow", "50"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_3.setText(_translate("MainWindow", "Odd or Even Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
