import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtCore import Qt , QSize, Qt
import MySQLconnection as connection


class premiumPlanWindow(QMainWindow):
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Premium Version')
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

        #Εισαγωγή Label Premium Version
        self.premium_label = QLabel ('Premium Version', self)
        self.premium_label.setGeometry(70, 140, 287, 74)
        self.premium_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 200, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Reserve Now', self)
        self.label.setGeometry(45, 200, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 255, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Arrange Your Reservation For Another Day', self)
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
        self.label = QLabel ('No Limit For Arrival Time', self)
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
        line.setGeometry(40, 345, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Monthly/Yearly Reservations', self)
        self.label.setGeometry(45, 335, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 390, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Choose Your Spot', self)
        self.label.setGeometry(45, 380, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 435, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('Cancel Anytime', self)
        self.label.setGeometry(45, 425, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 480, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')

        #Εισαγωγή Label 
        self.label = QLabel ('2 Free Reservations(4Hr/Time)', self)
        self.label.setGeometry(45, 470, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 525, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')


        #Εισαγωγή Label 
        self.label = QLabel ('8,99\u20ac/Month ', self)
        self.label.setGeometry(45, 510, 287, 74)
        self.label.setStyleSheet('''
	        color: #000000;
	        font-family: "Helvetica";
	        font-weight: 400;
	        font-size: 14px;
	        text-align: center;
        ''')

        #Button Back
        button_back = QPushButton('Back',self)
        button_back.setGeometry(50,570,100,37)
        button_back.setCursor(QCursor(Qt.PointingHandCursor))
        button_back.clicked.connect(self.back_pressed) 
        button_back.setStyleSheet('''
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
        button_next = QPushButton('Next',self)
        button_next.setGeometry(195,570,100,37)
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.next_pressed) 
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

    def back_pressed(self):
        print("back clicked") 
        from chplan import choosePlanWindow

        try:
            #Σύνδεση στη Βάση Δεδομένων
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()


            # Διαγραφή της εγγραφής "Premium Version" για τον συγκεκριμένο χρήστη
            sql_delete = "DELETE FROM plans WHERE plan_type = %s AND user_id = %s"
            data_delete = ("Premium Version", self.user_id)
            cursor.execute(sql_delete, data_delete)
            
            # commit στη βάση
            db.commit()

            # exit
            cursor.close()
            db.close()

            # Κλείσιμο παραθύρου
            self.close()


            self.plan_window = choosePlanWindow(self.user_id)  
            self.plan_window.show()
           

        except Exception as e:
            # Αν υπάρξει σφάλμα, εκτύπωσέ το
            print("Error:", e)

    def next_pressed(self):
        from payment import paymentWindow
        self.payment_window = paymentWindow(self.user_id)   
        self.payment_window.show()
        self.close() 

# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = premiumPlanWindow()
    window.show()
    sys.exit(app.exec_())