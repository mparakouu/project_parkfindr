import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView 

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
        logo_png.setGeometry(50, 50, 250, 70)
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



        # Ετικέτα καλωσορίσματος
        welcome_label = QLabel('Welcome', self)  
        welcome_label.setGeometry(120, 270, 250, 30)  
        welcome_label.setStyleSheet('''
            color: #3D8AF7; 
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 22px;
        ''')

        # Ετικέτα email
        email_label = QLabel(self.user_email, self)
        email_label.setGeometry(120, 300, 250, 30)  
        email_label.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
        ''')

        # Δημιουργία κουμπιών για επιλογές μενού
        button_reserve = QPushButton('Reserve Now', self)
        button_reserve.setGeometry(100, 370, 140, 40)
        button_reserve.setCursor(QCursor(Qt.PointingHandCursor))
        button_reserve.clicked.connect(self.openPage1)
        button_reserve.setStyleSheet('''
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

        button_reservations = QPushButton('Reservations', self)
        button_reservations.setGeometry(100, 440, 140, 40)
        button_reservations.setCursor(QCursor(Qt.PointingHandCursor))
        button_reservations.clicked.connect(self.openPage2)
        button_reservations.setStyleSheet('''
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

        button_calendar = QPushButton('Calendar', self)
        button_calendar.setGeometry(100, 510, 140, 40)
        button_calendar.setCursor(QCursor(Qt.PointingHandCursor))
        button_calendar.clicked.connect(self.openPage3)
        button_calendar.setStyleSheet('''
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

        button_account = QPushButton('Account', self)
        button_account.setGeometry(100, 580, 140, 40)
        button_account.setCursor(QCursor(Qt.PointingHandCursor))
        button_account.clicked.connect(self.openPage4)
        button_account.setStyleSheet('''
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
        from reservations import ReservationsWindow
        self.Reservations_window= ReservationsWindow()
        self.Reservations_window.show()
        self.close()
       
    
    def openPage3(self):
        print("calendar")
    
    def openPage4(self):
        print("account")
        from account import accountWindow
        self.acc_window= accountWindow(self.user_email)
        self.acc_window.show()
        self.close()

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
