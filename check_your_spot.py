import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
import MySQLconnection as connection



class CheckSpot(QMainWindow):
    def __init__(self, user_id, parking_number, selected_duration_time):
        super().__init__() 
        self.parking_number = parking_number
        self.selected_duration_time = selected_duration_time
        self.user_id = user_id
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
        self.checkbox1 = QCheckBox('', self)
        self.checkbox1.setGeometry(23, 180, 10, 10)  # θέση και μέγεθος
        self.checkbox1.setObjectName("1")
        self.checkbox1.setFixedSize(30, 30)  # τετράγωνο κουμπί
        
        self.checkbox3 = QCheckBox('', self)
        self.checkbox3.setGeometry(108, 420, 10, 10)  
        self.checkbox3.setObjectName("3")
        self.checkbox3.setFixedSize(30, 30) 

        self.checkbox4 = QCheckBox('', self)
        self.checkbox4.setGeometry(172, 180, 10, 10)  
        self.checkbox4.setObjectName("4")
        self.checkbox4.setFixedSize(30, 30) 

        self.checkbox5 = QCheckBox('', self)
        self.checkbox5.setGeometry(214, 180, 10, 10)  
        self.checkbox5.setObjectName("5")
        self.checkbox5.setFixedSize(30, 30)  

        self.checkbox6 = QCheckBox('', self)
        self.checkbox6.setGeometry(236, 180, 10, 10)  
        self.checkbox6.setObjectName("6")
        self.checkbox6.setFixedSize(30, 30)   

        self.checkbox7 = QCheckBox('', self)
        self.checkbox7.setGeometry(278, 420, 10, 10)  
        self.checkbox7.setObjectName("7")
        self.checkbox7.setFixedSize(30, 30)   

        self.checkbox8 = QCheckBox('', self)
        self.checkbox8.setGeometry(236, 420, 10, 10)  
        self.checkbox8.setObjectName("8")
        self.checkbox8.setFixedSize(30, 30)   

        self.checkbox9 = QCheckBox('', self)
        self.checkbox9.setGeometry(278, 180, 10, 10)  
        self.checkbox9.setObjectName("9")
        self.checkbox9.setFixedSize(30, 30)   

        self.checkbox10 = QCheckBox('', self)
        self.checkbox10.setGeometry(23, 420, 10, 10)  
        self.checkbox10.setObjectName("10")
        self.checkbox10.setFixedSize(30, 30)  


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


# όταν συνδέσουμε με βάση, θα συνδέουμε id πελάτη με θέση, και όταν την κάνει reserve δεν θα είναι πλέον διαθέσιμη 

    # έλεγχος για το ποιο κουμπί πατήθηκε, 
    def check_selected_spot(self):
        buttons = [self.checkbox1, self.checkbox3, self.checkbox4, self.checkbox5,
                   self.checkbox6, self.checkbox7, self.checkbox8, self.checkbox9, self.checkbox10]

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
            print("ID χρήστη:", self.user_id)
            print("Κρατήθηκε η θέση:", self.spot_reserved)
            print("Parking number που επιλέχθηκε:", self.parking_number)
            print("Διάρκεια διαμονής που επιλέχθηκε:", self.selected_duration_time )

            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()

            # insert στο table user
            sql_insert = "INSERT INTO createReservation (costumerID, ParkNum, DurationTime, NumSpot) VALUES (%s, %s, %s, %s)"
            data_insert = (self.user_id, self.parking_number, self.selected_duration_time, self.spot_reserved)

            # εκτέλεση του insert
            cursor.execute(sql_insert, data_insert)
            
            # commit στην βάση
            db.commit()

            # exit
            cursor.close()
            db.close()
            print("Η κράτηση πραγματοποιήθηκε!")


            from reservationConfirmed import ResConfirmed
            self.close()
            # με πάει στο confirmed πράθυρο 
            self.confirmed_window = ResConfirmed()
            self.confirmed_window.show()


        else:
            print("Παρακαλώ επιλέξτε μια θέση!")

    # όταν πατήσει το κουμπί back --> duration_time_parking.py
    def back_button_pressed(self):
        from duration_time_parking import DurationTime
        self.close()
        self.time_window = DurationTime()
        self.time_window.show()


   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckSpot()
    window.show()
    sys.exit(app.exec_())