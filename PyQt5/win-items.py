
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QLabel
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(500,500,500,500)
    win.setWindowIcon(QIcon('icon.png'))
    win.setToolTip('my tooltip')

    lbl_name = QLabel(win)
    lbl_name.setText("First Name: ")
    lbl_name.move(90,80)
    lbl_surname = QLabel(win)
    lbl_surname.setText("Last Name: ")
    lbl_surname.move(90,100)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(160, 80)
    
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(160,100)

    def clicked(self):
        print('You have click to button\nFirst Name: ' + txt_name.text() + '\nLast Name:' + txt_surname.text())  

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(160,140)
    btn_save.clicked.connect(clicked)


    win.show()
    sys.exit(app.exec_())



window()