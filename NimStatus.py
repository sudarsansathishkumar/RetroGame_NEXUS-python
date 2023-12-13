from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def no_pressed(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def yes_pressed(self):
        from Nim import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.ranmatch()
        self.window.show()


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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "Would you like to continue?"))
        self.Yes.setText(_translate("Form", "Yes"))
        self.No.setText(_translate("Form", "No"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
