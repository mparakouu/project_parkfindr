import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from PyQt5.QtWebEngineWidgets import QWebEngineView  



class makeReservation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
  
    def initUI(self):
        self.setWindowTitle('Make Reservation')
        self.setGeometry(100, 100, 340, 667)



  
        # περίγραμμα του iPhone
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

        
        #Εισαγωγή του Background
        self.background_label = QLabel(self)
        self.background_label.setGeometry(23, 50, 295, 578)
        pixmap = QPixmap('image.png')
        self.background_label.setPixmap(pixmap.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio))




       

        label_res = QLabel('Make your reservation ' , self)
        label_res.setGeometry(40, 200, 434, 74)
        label_res.setObjectName('reservation')
        label_res.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 24px;
            text-align: left;

        '''  )

        label_reser = QLabel('  now ' , self)
        label_reser.setGeometry(120, 240, 434, 74)
        label_reser.setObjectName('reservation1')
        label_reser.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 30px;
            text-align: left;

        '''  )
        
        # Κουμπί search
        search_Button = QPushButton('Search', self)
        search_Button.setGeometry(80, 340, 184, 49)
        search_Button.setCursor(QCursor(Qt.PointingHandCursor))
        search_Button.clicked.connect(self.open_map)
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
    
     from selectParking import selectParking
     self.selectParkingWindow= selectParking()
     self.selectParkingWindow.show()
             
   



    def open_map(self):
        print("ok")
        from selectParking import selectParking
        self.close()
        self.map_window = selectParking()
        self.map_window.show()
    


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = makeReservation()
    window.show()
    sys.exit(app.exec_())
