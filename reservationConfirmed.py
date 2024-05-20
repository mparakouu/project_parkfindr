import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication



class ResConfirmed(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('Reservation confirmed')
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


        #Εισαγωγή του okay logo
        image_label = QLabel(self)
        image_label.setGeometry(127, 70, 80, 100)
        pixmap = QPixmap ('Okay.png')
        image_label.setPixmap(pixmap.scaled(80, 80, QtCore.Qt.KeepAspectRatio))



        
        self.res_Con = QLabel('Reservation confirmed!', self)
        self.res_Con.setGeometry(50, 130, 250, 200) 
        self.res_Con.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Mukta Vaani";
            font-weight: 400;
            font-size: 25px;
            text-align: left;
        ''') 





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResConfirmed()
    window.show()
    sys.exit(app.exec_())        