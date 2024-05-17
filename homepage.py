import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess


class homeWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('Home Page')
        self.setGeometry(100, 100, 340, 667)

        # Φόρτωση του περιγράμματος του iPhone
        iphonePixmap = QPixmap('iphoneFrame.png')
        iPhoneFrame = QFrame(self)
        iPhoneFrame.setGeometry(5, 5, iphonePixmap.width(), iphonePixmap.height())
        iPhoneFrame.setStyleSheet('''
            border-image: url('iphoneFrame.png') 13 13 13 13 stretch stretch;
            border: 6px solid #aaa;
            border-radius: 50px;                     
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            background-color: transparent; 
            background-color: #FFFFFF; 
        ''')


       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = homeWindow()
    window.show()  
    sys.exit(app.exec_())