import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from signin import signInWindow


class makeReservation(QMainWindow):
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
        
       

        label_review = QLabel('Make your reservation ' , self)
        label_review.setGeometry(40, 240, 434, 74)
        label_review.setObjectName('review')
        label_review.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 24px;
            text-align: left;

        '''  )
        label_review = QLabel('  now ' , self)
        label_review.setGeometry(120, 270, 434, 74)
        label_review.setObjectName('review')
        label_review.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 30px;
            text-align: left;

        '''  )
        
        # Κουμπί Sign up
        Signup_Button = QPushButton('Search', self)
        Signup_Button.setGeometry(80, 340, 184, 49)
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = makeReservation()
    window.show()
    sys.exit(app.exec_())