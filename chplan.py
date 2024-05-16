import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtCore import Qt , QSize, Qt


class choosePlanWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Choose Plan')
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

        #Εισαγωγή Label Choose your Plan
        self.plan_label = QLabel ('Choose your plan', self)
        self.plan_label.setGeometry(75, 165, 287, 74)
        self.plan_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Button Free
        button_free = QPushButton('Free Version', self)
        button_free.setGeometry(40, 260, 160, 50)
        button_free.setCursor(QCursor(Qt.PointingHandCursor))
        button_free.clicked.connect(self.free_version) # εκτελεί την next_pressed και εισάγει τα data, 
        button_free.setStyleSheet('''
            border: none;
	        color: #3D8AF7;
	        font-family: "ADLaM Display";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;                   
        ''')

        #Εισαγωγή του Arrow 
        arrow = QLabel(self)
        arrow.setGeometry(270, 235, 180, 100)
        pixmap = QPixmap ('right-arrow.png')
        arrow.setPixmap(pixmap.scaled(29, 29, QtCore.Qt.KeepAspectRatio))

        #Underline Free Version
        line1 = QLabel(self)
        line1.setGeometry(40, 310, 270, 1)
        line1.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')
         
        #Button Plus
        button_plus = QPushButton('Plus Version', self)
        button_plus.setGeometry(40, 330, 180, 50)
        button_plus.setCursor(QCursor(Qt.PointingHandCursor))
        button_plus.clicked.connect(self.plus_version) # εκτελεί την next_pressed και εισάγει τα data, 
        button_plus.setStyleSheet('''
            border: none;
	        color: #3D8AF7;
	        font-family: "ADLaM Display";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;                   
        ''')

        #Εισαγωγή του Arrow 
        arrow = QLabel(self)
        arrow.setGeometry(270, 305, 180, 100)
        pixmap = QPixmap ('right-arrow.png')
        arrow.setPixmap(pixmap.scaled(29, 29, QtCore.Qt.KeepAspectRatio))

        #Underline Plus Version
        line2 = QLabel(self)
        line2.setGeometry(40, 380, 270, 1)
        line2.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')
 

        #Button Premium
        button_Premium = QPushButton('Premium Version', self)
        button_Premium.setGeometry(40, 400, 205, 50)
        button_Premium.setCursor(QCursor(Qt.PointingHandCursor))
        button_Premium.clicked.connect(self.premium_version) # εκτελεί την next_pressed και εισάγει τα data, 
        button_Premium.setStyleSheet('''
            border: none;
	        color: #3D8AF7;
	        font-family: "ADLaM Display";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;                   
        ''')

        #Εισαγωγή του Arrow 
        arrow = QLabel(self)
        arrow.setGeometry(270, 375, 180, 100)
        pixmap = QPixmap ('right-arrow.png')
        arrow.setPixmap(pixmap.scaled(29, 29, QtCore.Qt.KeepAspectRatio))

        #Underline Premium Version
        line2 = QLabel(self)
        line2.setGeometry(40, 450, 270, 1)
        line2.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')
        
        message = QLabel('You have to choose a plan', self)
        message.setGeometry(75, 504, 200, 42)
        message.setStyleSheet('''
	        color: #727579;
	        font-family: "Asap";
	        font-weight: 400;
	        font-size: 16px;
	        line-height: 1.5;
	        text-align: left;
        ''')


    #Λειτουργία Free Version Button
    def free_version(self):
        print("free clicked") 
        from freeplan import freePlanWindow
        self.free_planwindow = freePlanWindow()
        self.free_planwindow.show()
        self.close()
        
    #Λειτουργία Plus Version Button
    def plus_version(self):
        print("plus clicked") 
        from plusplan import plusPlanWindow
        self.plus_planwindow = plusPlanWindow()
        self.plus_planwindow.show()
        self.close()

    #Λειτουργία Premium Version Button
    def premium_version(self):
        print("Premium clicked") 
        from premiumplan import premiumPlanWindow
        self.prem_planwindow = premiumPlanWindow()
        self.prem_planwindow.show()
        self.close()




# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = choosePlanWindow()
    window.show()
    sys.exit(app.exec_())