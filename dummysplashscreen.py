from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_Splash(object):
    
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(700, 400)
        Splash.setMinimumSize(QtCore.QSize(700, 400))
        Splash.setMaximumSize(QtCore.QSize(700, 400))
        Splash.setStyleSheet("background-color:skyblue;")
        self.centralwidget = QtWidgets.QWidget(Splash)
        Splash.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(144, 138, 420, 81))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(222, 218, 260, 20))
        self.label_2.setStyleSheet("color:blue;")
        self.label_2.setObjectName("label_2")
        Splash.setCentralWidget(self.centralwidget)
        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)
    def openmain(self):
        from front import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def retranslateUi(self, Splash):
        _translate = QtCore.QCoreApplication.translate
        Splash.setWindowTitle(_translate("Splash", "Nexus - Imagine ChildWorks"))
        self.label.setText(_translate("Splash", "Retro games by Nexus"))
        self.label_2.setText(_translate("Splash", "From the community of Imagine ChildWorks"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Splash = QtWidgets.QMainWindow()
    ui = Ui_Splash()
    ui.setupUi(Splash)
    Splash.show()
    time.sleep(3)
    Splash.close()
    ui.openmain()
    sys.exit(app.exec_())
