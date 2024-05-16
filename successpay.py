import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QLabel,QVBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap,QCursor
from PyQt5.QtCore import Qt


class successpayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Success Payment')
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

        #Εισαγωγή Label Your payment
        self.plus_label = QLabel ('Your payment', self)
        self.plus_label.setGeometry(90, 200, 287, 74)
        self.plus_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Εισαγωγή Label Payment
        self.plus_label = QLabel ('was successfull!', self)
        self.plus_label.setGeometry(82, 230, 287, 74)
        self.plus_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')
        #Εισαγωγή του Check 
        check_icon = QLabel(self)
        check_icon.setGeometry(150, 330, 180, 100)
        pixmap = QPixmap ('check.png')
        check_icon.setPixmap(pixmap.scaled(45, 45, QtCore.Qt.KeepAspectRatio))

        #Button Continue to sign in
        button_next = QPushButton('Continue to sign in', self)
        button_next.setGeometry(85, 520, 180, 36)
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.go_to_pressed) # εκτελεί την next_pressed και εισάγει τα data, 
        button_next.setStyleSheet('''
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

    def go_to_pressed(self):
        print("proceed clicked") 
        self.close()  
        from signin import signInWindow
        self.sign_in_window = signInWindow() 
        self.sign_in_window.show()
        self.close() 



# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = successpayWindow()
    window.show()
    sys.exit(app.exec_())