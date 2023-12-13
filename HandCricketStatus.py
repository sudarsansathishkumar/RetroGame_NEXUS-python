from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):

    def no_pressed(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # import HandCricket
        # from HandCricket import Ui_HandCricket
        # self.window2= QtWidgets.QMainWindow()
        # self.ui2 = Ui_HandCricket()
        # self.ui2.setupUi(self.window2)
        self.window.show()
        
    def yes_pressed(self):
        import HandCricket
        from HandCricket import Ui_HandCricket
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HandCricket()
        self.ui.setupUi(self.window)
        self.ui.restart()
        HandCricket.player.play()
        self.window.show()
        # HandCricket.
        # pc_score = 0
        # play = 0
        # self.your_score.setText(str(0))
        # self.computer_score.setText(str(0))
        # self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 300)
        Form.setMinimumSize(QtCore.QSize(550, 300))
        Form.setMaximumSize(QtCore.QSize(550, 800))
        Form.setStyleSheet("background-color:skyblue;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 147, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Yes = QtWidgets.QPushButton(Form, clicked = lambda : self.yes_pressed())
        self.Yes.clicked.connect(Form.close)
        self.Yes.setGeometry(QtCore.QRect(146, 217, 121, 41))
        self.Yes.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:white;\n"
"    color:green;\n"
"    outline:none;\n"
"    border-radius:10px;\n"
"    border:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:green;\n"
"    color:white;\n"
"    border:1px solid white;\n"
"}")
        self.Yes.setObjectName("Yes")
        self.No = QtWidgets.QPushButton(Form, clicked = lambda : self.no_pressed())
        self.No.clicked.connect(Form.close)
        self.No.setGeometry(QtCore.QRect(276, 217, 121, 41))
        self.No.setStyleSheet("QPushButton\n"
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
        self.No.setObjectName("No")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(105, 105, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(285, 107, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(205, 103, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(425, 105, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "Would you like to continue?"))
        self.Yes.setText(_translate("Form", "Yes"))
        self.No.setText(_translate("Form", "No"))
        self.label_3.setText(_translate("Form", "Your score :"))
        self.label_4.setText(_translate("Form", "Computer score :"))
        self.label_5.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
