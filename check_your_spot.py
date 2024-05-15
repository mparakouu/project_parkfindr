import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess


class CheckSpot(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('Check your spot')
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


        self.ckeck_spot = QLabel('Ckeck your spot:', self)
        self.ckeck_spot.setGeometry(90, 60, 250, 30)
        self.ckeck_spot.setStyleSheet('''
            color: #75A9F9;
            font-family: "Quicksand";
            font-weight: bold;     
            font-size: 20px;
            text-align: left;
            word-wrap: break-word;                           
        ''')

         # Εισαγωγή της εικόνας στο QLabel
        pixmap = QPixmap('parking_spots.png')
        parking_spots = QLabel(self)
        parking_spots.setPixmap(pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)) #μέγεθος εικόνας
        parking_spots.setGeometry(20, 80, 2000, 470)


        # κουμπιά 
        button1 = QPushButton('', self)
        button1.setGeometry(17, 180, 10, 10)  # θέση και μέγεθος
        button1.setObjectName("button1")
        button1.setFixedSize(30, 30)  # τετράγωνο κουμπί 
        

        button2 = QPushButton('', self)
        button2.setGeometry(60, 180, 10, 10)  
        button1.setObjectName("button2")
        button2.setFixedSize(30, 30)  

        button3 = QPushButton('', self)
        button3.setGeometry(102, 180, 10, 10)  
        button1.setObjectName("button3")
        button3.setFixedSize(30, 30)  

        button4 = QPushButton('', self)
        button4.setGeometry(166, 180, 10, 10)  
        button1.setObjectName("button4")
        button4.setFixedSize(30, 30)  

        button5 = QPushButton('', self)
        button5.setGeometry(208, 180, 10, 10)  
        button1.setObjectName("button5")
        button5.setFixedSize(30, 30)  

        button6 = QPushButton('', self)
        button6.setGeometry(230, 180, 10, 10)  
        button1.setObjectName("button6")
        button6.setFixedSize(30, 30)  

        button7 = QPushButton('', self)
        button7.setGeometry(272, 180, 10, 10)  
        button1.setObjectName("button7")
        button7.setFixedSize(30, 30)  

   
   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckSpot()
    window.show()
    sys.exit(app.exec_())