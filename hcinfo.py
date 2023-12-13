from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 711)
        MainWindow.setStyleSheet("background-color:skyblue;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 561, 591))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:skyblue;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 26))
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
        self.label.setText(_translate("MainWindow", "1).The game is played between two players. both user and computer takes turns as the batsman and the bowler.\n"
"\n"
"2).The objective of the game is for the batsman to score runs by choosing a number between 1 and 6 and trying to guess the number the bowler is thinking.\n"
"\n"
"3).The bowler thinks of a number between 1 and 6 and shows it to the batsman.\n"
"\n"
"4).The batsman then guesses a number between 1 and 6. If the number guessed by the batsman matches the number thought by the bowler, the batsman is out. \n"
"If the numbers don\'t match, the batsman scores the number of runs he guessed.\n"
"\n"
"5).The game continues until the batsman is out.\n"
"\n"
"6).After wicket goes off the user and the computer swith the switch roles, with the bowler becoming the batsman and the batsman becoming the bowler.\n"
"\n"
"7).The player with the highest score at the end of the game is the winner"))
        self.label_2.setText(_translate("MainWindow", "Rules for Hand Cricket :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
