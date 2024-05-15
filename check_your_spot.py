import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from duration_time_parking import DurationTime


class CheckSpot(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('Check your spot')
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


        self.ckeck_spot = QLabel('Ckeck your spot:', self)
        self.ckeck_spot.setGeometry(90, 60, 250, 30)
        self.ckeck_spot.setStyleSheet('''
            color: #75A9F9;
            font-family: "Quicksand";
            font-weight: bold;     
            font-size: 20px;
            text-align: left;
            word-wrap: break-word;                           
        ''')

         # εισαγωγή εικόνας 
        pixmap = QPixmap('parking_spots.png')
        parking_spots = QLabel(self)
        parking_spots.setPixmap(pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)) #μέγεθος εικόνας
        parking_spots.setGeometry(20, 80, 2000, 470)



        # Κουμπιά 
        self.button1 = QPushButton('', self)
        self.button1.setGeometry(17, 180, 10, 10)  # θέση και μέγεθος
        self.button1.setObjectName("1")
        self.button1.setFixedSize(30, 30)  # τετράγωνο κουμπί
        self.button1.setCheckable(True) # επιλέγουμε το κουμπί
        self.button1.setAutoExclusive(True)  # μόνο ένα επιλέξιμο
        
        self.button2 = QPushButton('', self)
        self.button2.setGeometry(60, 180, 10, 10)  
        self.button2.setObjectName("2")
        self.button2.setFixedSize(30, 30)  
        self.button2.setCheckable(True) 
        self.button2.setAutoExclusive(True)  

        self.button3 = QPushButton('', self)
        self.button3.setGeometry(102, 420, 10, 10)  
        self.button3.setObjectName("3")
        self.button3.setFixedSize(30, 30) 
        self.button3.setCheckable(True) 
        self.button3.setAutoExclusive(True)   

        self.button4 = QPushButton('', self)
        self.button4.setGeometry(166, 180, 10, 10)  
        self.button4.setObjectName("4")
        self.button4.setFixedSize(30, 30) 
        self.button4.setCheckable(True) 
        self.button4.setAutoExclusive(True)   

        self.button5 = QPushButton('', self)
        self.button5.setGeometry(208, 180, 10, 10)  
        self.button5.setObjectName("5")
        self.button5.setFixedSize(30, 30)  
        self.button5.setCheckable(True) 
        self.button5.setAutoExclusive(True)  

        self.button6 = QPushButton('', self)
        self.button6.setGeometry(230, 180, 10, 10)  
        self.button6.setObjectName("6")
        self.button6.setFixedSize(30, 30) 
        self.button6.setCheckable(True) 
        self.button6.setAutoExclusive(True)   

        self.button7 = QPushButton('', self)
        self.button7.setGeometry(272, 420, 10, 10)  
        self.button7.setObjectName("7")
        self.button7.setFixedSize(30, 30) 
        self.button7.setCheckable(True) 
        self.button7.setAutoExclusive(True)   

        self.button8 = QPushButton('', self)
        self.button8.setGeometry(230, 420, 10, 10)  
        self.button8.setObjectName("8")
        self.button8.setFixedSize(30, 30) 
        self.button8.setCheckable(True) 
        self.button8.setAutoExclusive(True)   

        self.button9 = QPushButton('', self)
        self.button9.setGeometry(272, 180, 10, 10)  
        self.button9.setObjectName("9")
        self.button9.setFixedSize(30, 30) 
        self.button9.setCheckable(True) 
        self.button9.setAutoExclusive(True)   

        self.button10 = QPushButton('', self)
        self.button10.setGeometry(17, 420, 10, 10)  
        self.button10.setObjectName("10")
        self.button10.setFixedSize(30, 30)  
        self.button10.setCheckable(True) 
        self.button10.setAutoExclusive(True)  


        # κουμπί next
        reserve_button = QPushButton('Reserve', self)
        reserve_button.setGeometry(155, 550, 140, 35)
        reserve_button.setCursor(QCursor(Qt.PointingHandCursor))
        reserve_button.clicked.connect(self.reserve_button_pressed) 
        reserve_button.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
            background: #75A9F9;
            color: #FFFFFF;
            border-radius: 15px;  
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            line-height: 1.3;
            text-align: center;
            margin-left: 20px;  
            
        ''')

         # κουμπί back 
        back_button = QPushButton('Back', self)
        back_button.setGeometry(20, 550, 140, 35)
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.clicked.connect(self.back_button_pressed) 
        back_button.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
            background: #75A9F9;
            color: #FFFFFF;
            border-radius: 15px;  
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            line-height: 1.3;
            text-align: center;
            margin-left: 20px;  
        ''')

    # έλεγχος για το ποιο κουμπί πατήθηκε, 
    def check_selected_spot(self):
        buttons = [self.button1, self.button2, self.button3, self.button4, self.button5,
                   self.button6, self.button7, self.button8, self.button9, self.button10]

        # όποιο κουμπί πατήθηκε / isChescked --> το αποθηκεύει (όνομα κουμπιού) στην μεταβλητή self.spot_reserved
        for button in buttons:
            if button.isChecked():
                self.spot_reserved = button.objectName()
                break
        else:
            self.spot_reserved = None

    # όταν πατηθεί το κουμπί reserve, θα κρατηθεί η θέση του επέλεξε ο χρήστης
    def reserve_button_pressed(self):
        self.check_selected_spot()
        if self.spot_reserved:
            print("Κρατήθηκε η θέση:", self.spot_reserved)
        else:
            print("Παρακαλώ επιλέξτε μια θέση!")

    # όταν πατήσει το κουμπί back --> duration_time_parking.py
    def back_button_pressed(self):
        self.close()
        self.time_window = DurationTime()
        self.time_window.show()


   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckSpot()
    window.show()
    sys.exit(app.exec_())