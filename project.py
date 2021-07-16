


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-140, -30, 1521, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\background.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 190, 531, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\jarvis23.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-130, 530, 451, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\wave.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -90, 551, 281))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(r"C:\Users\HP\Documents\Downloads\AI gif\AI gif\initiating.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.INITIATE = QtWidgets.QPushButton(self.centralwidget)
        self.INITIATE.setGeometry(QtCore.QRect(580, 520, 181, 23))
        self.INITIATE.setObjectName("INITIATE")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.INITIATE.setText(_translate("MainWindow", "INITIATE  ASSISTANT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
