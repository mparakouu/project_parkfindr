import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel,  QTableWidget,QPushButton, QLineEdit, QWidget, QCheckBox, QVBoxLayout, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt ,QTimer


class reservationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Reservations')
        self.setGeometry(100, 100, 340, 667)


        #Περίγραμμα iPhone 
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

        #Εισαγωγή Label Reservations
        self.plus_label = QLabel ('Reservations', self)
        self.plus_label.setGeometry(30, 75, 287, 74)
        self.plus_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(30, 130, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(200, 130, 105, 2)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')




# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = reservationsWindow()
    window.show()
    sys.exit(app.exec_())