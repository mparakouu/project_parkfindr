import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from signin import signInWindow
from signup import signUpWindow

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self):
        self.setWindowTitle('ParkFindr')
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


# TA ΒΛΕΠΟΥΜΕ ΑΥΤΑ ΤΙ ΘΑ ΤΑ ΚΑΝΟΥΜΕ ! 

        # εικόνα στο QLabel
        image_label = QLabel(self)
        image_label.setGeometry(50, 50, 250, 70)
        pixmap = QPixmap('logo.png')
        image_label.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))
       

        image_label = QLabel(self)
        image_label.setGeometry(50, 60, 100, 1000)
        pixmap = QPixmap('instagram.png')
        image_label.setPixmap(pixmap.scaled(31, 31, QtCore.Qt.KeepAspectRatio))

        image_label = QLabel(self)
        image_label.setGeometry(160, 60, 100, 1000)
        pixmap = QPixmap('facebook.png')
        image_label.setPixmap(pixmap.scaled(31, 31, QtCore.Qt.KeepAspectRatio))

        image_label = QLabel(self)
        image_label.setGeometry(265, 60, 100, 1000)
        pixmap = QPixmap('twitter.png')
        image_label.setPixmap(pixmap.scaled(31, 31, QtCore.Qt.KeepAspectRatio))

    

        # Κουμπί Sign in
        Signin_Button = QPushButton('Sign in', self)
        Signin_Button.setGeometry(80, 250, 184, 49)
        Signin_Button.setCursor(QCursor(Qt.PointingHandCursor))
        Signin_Button.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 20px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 21px;
            text-align: center;
        ''')

        Signin_Button.clicked.connect(self.open_signin_window)



        # Κουμπί Sign up
        Signup_Button = QPushButton('Sign up', self)
        Signup_Button.setGeometry(80, 380, 184, 49)
        Signup_Button.setCursor(QCursor(Qt.PointingHandCursor))
        Signup_Button.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 20px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 21px;
            text-align: center;
        ''')

        Signup_Button.clicked.connect(self.open_signup_window)

        self.show()



    def open_signin_window(self):
        self.close()
        self.signin_window = signInWindow()
        self.signin_window.show()



    def open_signup_window(self):
        self.close()
        self.signup_window = signUpWindow()
        self.signup_window.show()

      



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())