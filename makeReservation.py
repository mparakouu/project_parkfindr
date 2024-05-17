import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor,QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess

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
        
       

        label_reservation = QLabel('Make your reservation ' , self)
        label_reservation.setGeometry(40, 240, 434, 74)
        label_reservation.setObjectName('review')
        label_reservation.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 24px;
            text-align: left;

        '''  )
        label_reservation2 = QLabel('  now ' , self)
        label_reservation2.setGeometry(120, 270, 434, 74)
        label_reservation2.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 30px;
            text-align: left;

        '''  )
        
        # Κουμπί Search
        search_Button = QPushButton('Search', self)
        search_Button.setGeometry(80, 340, 184, 49)
        search_Button.setCursor(QCursor(Qt.PointingHandCursor))
        search_Button.clicked.connect(self.search_pressed)
        search_Button.setStyleSheet('''
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
    def search_pressed(self):
     print("search clicked")
     from selectParking import selectParkingWindow
     self.selectParkingWindow= selectParkingWindow()
     self.selectParkingWindow.show()
             
     if __name__ == '__main__':
      app = QApplication(sys.argv)
     window = makeReservation()
     window.show()
     sys.exit(app.exec_())