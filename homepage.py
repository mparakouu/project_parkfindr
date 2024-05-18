import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt

class homeWindow(QMainWindow):
    def __init__(self, user_mail):
        super().__init__() 
        self.user_email = user_mail
        self.initUI() 

    def initUI(self):
        self.setWindowTitle('Home Page')
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

        # Εισαγωγή του λογότυπου 
        logo_png = QLabel(self)
        logo_png.setGeometry(50, 70, 250, 70)
        pixmap = QPixmap('logo.png')
        logo_png.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))

        # Εισαγωγή φωτογραφίας
        self.photo_frame = QFrame(self)
        self.photo_frame.setGeometry(122, 140, 100, 100)
        self.photo_frame.setStyleSheet('''
            background-color: #E0E0E0;
            border: 2px dashed #AAAAAA;
            border-radius: 5px;
        ''')

        # Κουμπί 
        self.photo_button = QPushButton('Upload Photo', self)
        self.photo_button.setGeometry(115, 250, 120, 30)
        self.photo_button.clicked.connect(self.uploadPhoto)
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
        # Ετικέτα καλωσορίσματος
        welcome_label = QLabel('Welcome', self)  
        welcome_label.setGeometry(120, 290, 250, 30)  
        welcome_label.setStyleSheet('''
            color: #3D8AF7; 
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 22px;
        ''')

        # Ετικέτα email
        email_label = QLabel(self.user_email, self)
        email_label.setGeometry(100, 320, 250, 30)  
        email_label.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
        ''')

        # Δημιουργία κουμπιών για επιλογές μενού
        button1 = QPushButton('Reserve Now', self)
        button1.setGeometry(120, 370, 100, 30)
        button1.clicked.connect(self.openPage1)
        button1.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 6px 6px 6px 6px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 13px;
            text-align: center;
''')

        button2 = QPushButton('Reservations', self)
        button2.setGeometry(120, 420, 100, 30)
        button2.clicked.connect(self.openPage2)
        button2.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 6px 6px 6px 6px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 14px;
            text-align: center;
''')

        button3 = QPushButton('Calendar', self)
        button3.setGeometry(120, 470, 100, 30)
        button3.clicked.connect(self.openPage3)
        button3.setStyleSheet('''
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

        button4 = QPushButton('Acount', self)
        button4.setGeometry(120, 520, 100, 30)
        button4.clicked.connect(self.openPage4)
        button4.setStyleSheet('''
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

    def openPage1(self):
        print("home clicked")
        from makeReservation import makeReservation
        self.makeReservation_window= makeReservation()
        self.makeReservation_window.show()
        self.close()


    def openPage2(self):
        print("reservation")
    
    def openPage3(self):
        print("calendar")
    
    def openPage4(self):
        print("account")

    def uploadPhoto(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', '', 'Image Files (*.png *.jpg *.jpeg)')
        if filename:
            print("photo path:", filename)
            self.photo_button.setHidden(True)
            self.photo_label = QLabel(self.photo_frame)
            self.photo_label.setGeometry(0, 0, 100, 100)
            self.photo_label.setAlignment(Qt.AlignCenter)
            self.photo_label.setStyleSheet(f"""
                QLabel {{
                    border: 2px solid #d6d6d6;
                    background-image: url({filename});
                    background-repeat: no-repeat;
                    background-position: center;
                    border-radius: 5px;
                }}
            """)
            self.photo_label.show()

    def logout_window(self):
        from signin import signInWindow
        self.close()
        self.logout_window = signInWindow()
        self.logout_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = homeWindow("example@example.com")
    window.show()  
    sys.exit(app.exec_())
