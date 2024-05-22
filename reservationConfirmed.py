import sys
import qrcode  #pip install "qrcode[pil]" 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from io import BytesIO


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

        # Δημιουργία και εμφάνιση του QR code
        qr_data = "Τα δεδομένα του QR code που θέλετε να εμφανίσετε"
        qr_img = qrcode.make(qr_data)
        qr_bytes = BytesIO()
        qr_img.save(qr_bytes, format='PNG')
        qr_pixmap = QPixmap()
        qr_pixmap.loadFromData(qr_bytes.getvalue())
        qr_label = QLabel(self)
        qr_label.setPixmap(qr_pixmap.scaled(qr_pixmap.width() // 3, qr_pixmap.height() // 3))  # Μείωση του μεγέθους κατά το ήμισυ
        qr_label.setGeometry(50, 100, qr_pixmap.width() // 3, qr_pixmap.height() // 3)  # Αλλαγή στο μέγεθος
        qr_label.move(92, 340)  # αλλαγή στη θέση --> x , y 

        # Εισαγωγή του okay logo
        image_label = QLabel(self)
        image_label.setGeometry(127, 70, 80, 100)
        pixmap = QPixmap('Okay.png')
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

        button_back = QPushButton('Back', self)
        button_back.setGeometry(95, 550, 140, 48)
        button_back.setObjectName('button-14')
        button_back.setCursor(QCursor(Qt.PointingHandCursor))
        button_back.setStyleSheet('''
            width: 140px;
            height: 48px;
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 3px;
            border-style: solid;
            border-radius: 20px 20px 20px 20px;
            font-family: "Shippori Antique B1";
            font-weight: bold;
            font-size: 19px;
            font-style: italic;
            text-align: center;
                                  
         ''')
       # button_back.clicked.connect(self.go_back)


        
        # κουμπί back
    #def go_back(self):
       # from homepage import homeWindow
       # self.close()
      #  self.back = homeWindow()
       # self.back.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResConfirmed()
    window.show()
    sys.exit(app.exec_())
