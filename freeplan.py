import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtCore import Qt , QSize, Qt


class freePlanWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Free Version')
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

        #Εισαγωγή του Logo
        image_label = QLabel(self)
        image_label.setGeometry(50, 70, 250, 70)
        pixmap = QPixmap ('logo.png')
        image_label.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))

        #Εισαγωγή Label Free Version
        self.Signup_label = QLabel ('Free Version', self)
        self.Signup_label.setGeometry(95, 165, 287, 74)
        self.Signup_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 240, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Reserve Now', self)
        self.label.setGeometry(45, 245, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 240, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Reserve Now', self)
        self.label.setGeometry(45, 245, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 300, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('30 Minutes Until Your Arrival', self)
        self.label.setGeometry(45, 290, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 340, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')
        
        #Εισαγωγή Label 
        self.label = QLabel ('Choose Your Duration Time', self)
        self.label.setGeometry(45, 330, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 380, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Choose Your Spot', self)
        self.label.setGeometry(45, 370, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 420, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Cancel Anytime', self)
        self.label.setGeometry(45, 410, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 460, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Free', self)
        self.label.setGeometry(45, 440, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Button Back
        button_signin = QPushButton('Back',self)
        button_signin.setGeometry(50,550,100,37)
        button_signin.setCursor(QCursor(Qt.PointingHandCursor))
        button_signin.clicked.connect(self.back_pressed) 
        button_signin.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
            background: #3D8AF7;                    
            color: #FFFFFF;
            border-radius: 6px 6px 6px 6px;
	        font-family: "Asap";
	        font-weight: 600;
	        font-size: 17px;
	        line-height: 1.3;
	        text-align: center;
        ''')

        #Button Next
        button_signin = QPushButton('Next',self)
        button_signin.setGeometry(195,550,100,37)
        button_signin.setCursor(QCursor(Qt.PointingHandCursor))
        button_signin.clicked.connect(self.next_pressed) 
        button_signin.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);    
            background: #3D8AF7;                    
            color: #FFFFFF;
            border-radius: 6px 6px 6px 6px;
	        font-family: "Asap";
	        font-weight: 600;
	        font-size: 17px;
	        line-height: 1.3;
	        text-align: center;
        ''')

    def back_pressed(self):
        print("back clicked") 
        from chplan import choosePlanWindow
        self.sign_in_window = choosePlanWindow()  
        self.sign_in_window.show()
        self.close() 


    def next_pressed(self):
        print("next clicked") 



# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = freePlanWindow()
    window.show()
    sys.exit(app.exec_())