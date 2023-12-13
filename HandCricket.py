from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys, os
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

user_score = 0
pc_score = 0
playernum = 1
play = 0 # => 0 for batting, 1 for bowling

dist = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six"}

path = os.path.join(os.getcwd(), 'assets/openpage.mp3')
url = QUrl.fromLocalFile(path)
content = QMediaContent(url)
player = QMediaPlayer()
player.setMedia(content)
player.setVolume(50)
win_status = 0
class Ui_HandCricket(object):
    def fr(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def infoinfo(self):
        from hcinfo import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def playaudio(self, val):
        if val != 0:
            player.play()
        else:
            player.pause()


    def openstatus(self):
        player.pause()
        from HandCricketStatus import Ui_Form
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        if win_status == 0:
            txt = "You Win"
        else:
            txt = "Computer Win"
        self.ui.label.setText(txt)
        self.ui.label_5.setText(str(user_score))
        self.ui.label_6.setText(str(pc_score))
        self.window.show()
        self.dummy.click()

    def restart(self):
        global play
        global user_score
        global pc_score

        user_score = 0
        pc_score = 0
        play = 0
        self.your_score.setText(str(0))
        self.computer_score.setText(str(0))

    def playing(self, score):
        global play
        global user_score
        global pc_score
        global win_status

        self.cmp_turn = random.randint(1, 6)
        print("Score :", score, "Cmp :", self.cmp_turn)

        self.userhandsymbol = dist[score]
        self.computersymbol = dist[self.cmp_turn]

        self.userhandsymbolcmd = "assets/" + self.userhandsymbol + ".png"
        self.my_hand.setPixmap(QtGui.QPixmap(self.userhandsymbolcmd))

        self.computerhandsymbolcmd = "assets/" + self.computersymbol + ".png"
        self.computer_hand.setPixmap(QtGui.QPixmap(self.computerhandsymbolcmd))

        if play == 0:
            if self.cmp_turn == score:
                play = 1
                self.label_4.setText("Bowling")
            else:
                user_score += score
                self.your_score.setText(str(user_score))
        elif play == 1:
            if self.cmp_turn == score:
                self.openstatus()
            else:
                pc_score += self.cmp_turn
                self.computer_score.setText(str(pc_score))
                if pc_score > user_score:
                    win_status = 1
                    self.openstatus()
    def setupUi(self, HandCricket):
        HandCricket.setObjectName("HandCricket")
        HandCricket.setEnabled(True)
        HandCricket.resize(700, 800)
        HandCricket.setMinimumSize(QtCore.QSize(700, 800))
        HandCricket.setMaximumSize(QtCore.QSize(700, 800))
        HandCricket.setStyleSheet("background-color:skyblue;")
        self.centralwidget = QtWidgets.QWidget(HandCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.my_hand = QtWidgets.QLabel(self.centralwidget)
        self.my_hand.setGeometry(QtCore.QRect(90, 100, 211, 181))
        self.my_hand.setStyleSheet("background-color:white;\n"
"border-radius:10px")
        self.my_hand.setText("")
        self.my_hand.setPixmap(QtGui.QPixmap("assets/five.png"))
        self.my_hand.setScaledContents(True)
        self.my_hand.setObjectName("my_hand")
        self.computer_hand = QtWidgets.QLabel(self.centralwidget)
        self.computer_hand.setGeometry(QtCore.QRect(400, 100, 211, 181))
        self.computer_hand.setStyleSheet("background-color:white;\n"
"border-radius:10px")
        self.computer_hand.setText("")
        self.computer_hand.setPixmap(QtGui.QPixmap("assets/one.png"))
        self.computer_hand.setScaledContents(True)
        self.computer_hand.setObjectName("computer_hand")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 341, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:blue;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 341, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:red;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(91, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:blue;")
        self.label_5.setObjectName("label_5")
        self.your_score = QtWidgets.QLabel(self.centralwidget)
        self.your_score.setGeometry(QtCore.QRect(250, 401, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.your_score.setFont(font)
        self.your_score.setStyleSheet("color:red;")
        self.your_score.setObjectName("your_score")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(406, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:blue;")
        self.label_7.setObjectName("label_7")
        self.computer_score = QtWidgets.QLabel(self.centralwidget)
        self.computer_score.setGeometry(QtCore.QRect(620, 402, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.computer_score.setFont(font)
        self.computer_score.setStyleSheet("color:red;")
        self.computer_score.setObjectName("computer_score")
        self.dummy = QtWidgets.QPushButton(self.centralwidget)
        self.dummy.setStyleSheet("background-color:transparent; outline:none; border:0px;")
        self.dummy.clicked.connect(HandCricket.close)
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(1))
        self.one.setEnabled(True)
        self.one.setGeometry(QtCore.QRect(90, 480, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(2))
        self.two.setGeometry(QtCore.QRect(280, 480, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(3))
        self.three.setGeometry(QtCore.QRect(470, 480, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(4))
        self.four.setGeometry(QtCore.QRect(90, 580, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(5))
        self.five.setGeometry(QtCore.QRect(280, 580, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.playing(6))
        self.six.setGeometry(QtCore.QRect(470, 580, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six.setFont(font)
        self.six.setStyleSheet("QPushButton\n"
"{\n"
"    color:black; \n"
"    background-color:white;\n"
"    outline:none;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#66c2ff;\n"
"    border:1px solid #005c99;\n"
"    color:white;\n"
"}")
        self.six.setObjectName("six")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(638, 15, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/info.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.info = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.infoinfo())
        self.info.setGeometry(QtCore.QRect(634, 10, 50, 51))
        self.info.setStyleSheet("background-color:transparent;\n"
"border-radius:20%\n"
"")
        self.info.setText("")
        self.info.setObjectName("info")
        self.Quit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.fr())
        self.Quit.setGeometry(QtCore.QRect(206, 700, 121, 41))
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
        self.Quit.clicked.connect(HandCricket.close)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.restart())
        self.pushButton_8.setGeometry(QtCore.QRect(366, 700, 121, 41))
        self.pushButton_8.setStyleSheet("QPushButton\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(227, 7, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 290, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#800080;")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(455, 286, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#800080;")
        self.label_8.setObjectName("label_8")
        HandCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HandCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        HandCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HandCricket)
        self.statusbar.setObjectName("statusbar")
        HandCricket.setStatusBar(self.statusbar)

        self.retranslateUi(HandCricket)
        QtCore.QMetaObject.connectSlotsByName(HandCricket)

    def retranslateUi(self, HandCricket):
        _translate = QtCore.QCoreApplication.translate
        HandCricket.setWindowTitle(_translate("HandCricket", "Hand Cricket - Nexus"))
        self.label_3.setText(_translate("HandCricket", "You are now :"))
        self.label_4.setText(_translate("HandCricket", "Batting"))
        self.label_5.setText(_translate("HandCricket", "Your score :"))
        self.your_score.setText(_translate("HandCricket", "0"))
        self.label_7.setText(_translate("HandCricket", "Computer score :"))
        self.computer_score.setText(_translate("HandCricket", "0"))
        self.one.setText(_translate("HandCricket", "1"))
        self.one.setShortcut(_translate("HandCricket", "1"))
        self.two.setText(_translate("HandCricket", "2"))
        self.two.setShortcut(_translate("HandCricket", "2"))
        self.three.setText(_translate("HandCricket", "3"))
        self.three.setShortcut(_translate("HandCricket", "3"))
        self.four.setText(_translate("HandCricket", "4"))
        self.four.setShortcut(_translate("HandCricket", "4"))
        self.five.setText(_translate("HandCricket", "5"))
        self.five.setShortcut(_translate("HandCricket", "5"))
        self.six.setText(_translate("HandCricket", "6"))
        self.six.setShortcut(_translate("HandCricket", "6"))
        self.Quit.setText(_translate("HandCricket", "Quit"))
        self.pushButton_8.setText(_translate("HandCricket", "Restart"))
        self.label_2.setText(_translate("HandCricket", "HAND CRICKET"))
        self.label_6.setText(_translate("HandCricket", "You"))
        self.label_8.setText(_translate("HandCricket", "Computer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HandCricket = QtWidgets.QMainWindow()
    ui = Ui_HandCricket()
    ui.setupUi(HandCricket)
    ui.playaudio(playernum)
    HandCricket.show()
    sys.exit(app.exec_())
