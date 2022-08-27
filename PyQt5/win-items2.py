

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QLabel
from PyQt5.QtGui import QIcon



class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('First Application')
        self.setGeometry(500,500,500,500)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('my tooltip')
        self.initUI()

    def initUI(self):
        self.lbl_name = QLabel(self)
        self.lbl_name.setText("First Name: ")
        self.lbl_name.move(80,60)
        self.lbl_surname = QLabel(self)
        self.lbl_surname.setText("Last Name: ")
        self.lbl_surname.move(80,100)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(160, 60)
        self.txt_name.resize(200,32)
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(160,100)
        self.txt_surname.resize(200,32)

        self.lbl_resut = QtWidgets.QLabel(self)
        self.lbl_resut.resize(300,50)
        self.lbl_resut.move(280, 140)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(160,140)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        # print('You have click to button\nFirst Name: ' + self.txt_name.text() + '\nLast Name:' + self.txt_surname.text()) 
        self.lbl_resut.setText('First Name: ' + self.txt_name.text().title() + '\nLast Name: ' + self.txt_surname.text().title())

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()