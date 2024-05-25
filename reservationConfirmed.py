import sys
import qrcode  # pip install "qrcode[pil]"
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from io import BytesIO
import random

class ResConfirmed(QMainWindow):
    def __init__(self, user_id, user_email):
        super().__init__() 
        self.user_id = user_id
        self.user_email = user_email
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
        qr_data =  str(random.randint(1000, 9999)) # χρήση της random για να έχουμε διαφορετικό qr code κάθε φορά 
        qr_img = qrcode.make(qr_data)
        qr_bytes = BytesIO()
        qr_img.save(qr_bytes, format='PNG')
        qr_pixmap = QPixmap()
        qr_pixmap.loadFromData(qr_bytes.getvalue())
        qr_label = QLabel(self)
        qr_label.setPixmap(qr_pixmap.scaled(qr_pixmap.width() //1, qr_pixmap.height() // 1))  # μέγεθος του qr
        qr_label.setGeometry(50, 100, qr_pixmap.width() // 1, qr_pixmap.height() // 1)  # μέγεθος του qr
        qr_label.move(25, 240)  # αλλαγή στη θέση --> x , y 

        # okay logo
        image_label = QLabel(self)
        image_label.setGeometry(127, 70, 80, 100)
        pixmap = QPixmap('Okay.png')
        image_label.setPixmap(pixmap.scaled(80, 80, Qt.KeepAspectRatio))

        self.res_Con = QLabel('Reservation confirmed!', self)
        self.res_Con.setGeometry(50, 130, 250, 200) 
        self.res_Con.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Mukta Vaani";
            font-weight: 400;
            font-size: 25px;
            text-align: left;
        ''')

        button_back = QPushButton('Go to home page', self)
        button_back.setGeometry(70, 550, 200, 48)
        button_back.setObjectName('button-14')
        button_back.setCursor(QCursor(Qt.PointingHandCursor))
        button_back.setStyleSheet('''
            width: 140px;
            height: 48px;
            padding: 0px 10px 0px 10px;
            background: #3D8AF7;
	        border-radius: 6px 6px 6px 6px;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 3px;
            border-style: solid;
            font-family: "Shippori Antique B1";
            font-weight: bold;
            font-size: 19px;
            font-style: italic;
            text-align: center;
                                  
         ''')
        button_back.clicked.connect(self.go_back)

    def go_back(self):
        from homepage import homeWindow
        self.close()
        self.back = homeWindow(self.user_email, self.user_id)
        print("ID χρήστη:", self.user_id)
        print("email χρήστη:", self.user_email)
        self.back.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResConfirmed()
    window.show()
    sys.exit(app.exec_())
