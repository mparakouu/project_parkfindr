import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from PyQt5.QtWebEngineWidgets import QWebEngineView 

class AccountWindow(QMainWindow):
    def __init__(self,user_mail):
        super().__init__() 
        self.user_mail = user_mail
        self.initUI() 

    def initUI(self):
        self.setWindowTitle('Account')
        self.setGeometry(100, 100, 340, 667)
  
        # Κύριο πλαίσιο του iPhone
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
# Εισαγωγή φωτογραφίας
        self.photo_frame = QFrame(self)
        self.photo_frame.setGeometry(122, 165, 100, 100)
        self.photo_frame.setStyleSheet('''
            background-color: #E0E0E0;
            border: 2px dashed #AAAAAA;
            border-radius: 5px;
        ''')
        # Εισαγωγή του λογότυπου 
        logo_png = QLabel(self)
        logo_png.setGeometry(50, 50, 250, 70)
        pixmap = QPixmap('logo.png')
        logo_png.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))
    # Κουμπί 
        self.photo_button = QPushButton('Upload Photo', self)
        self.photo_button.setGeometry(115, 270, 120, 30)
        #self.photo_button.clicked.connect(self.uploadPhoto)
        self.photo_button.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 6px 6px 6px 6px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 17px;
            text-align: center;
''')
        l_account = QLabel('Account', self)
        l_account.setGeometry(115, 130, 120, 30)
        l_account.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 30px;
            text-align: left;

        '''  )
        # Πεδίο για  Full Name
        self.fullname_label = QLabel('Full Name:', self)
        self.fullname_label.setGeometry(70, 320, 200, 20) 
        self.fullname_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        # Πεδίο για  Phone Number
        self.number_label = QLabel('Phone Number:', self)
        self.number_label.setGeometry(70, 380, 200, 20) 
        self.number_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        
    # Πεδίο για  email
        self.mail_label = QLabel('E-mail:', self)
        self.mail_label.setGeometry(70, 440, 200, 20) 
        self.mail_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        label_mail = QLabel(self.user_mail,self)
        label_mail.setGeometry(70,470,200,20)
        label_mail.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
        ''')
         # Πεδίο για  Password
        self.pwd_label = QLabel('Password:', self)
        self.pwd_label.setGeometry(70, 490, 200, 20) 
        self.pwd_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AccountWindow("example@example.com")
    window.show()
    sys.exit(app.exec_())
