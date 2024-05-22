import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon, QDesktopServices, QRegExpValidator
from PyQt5.QtCore import Qt , QSize, Qt, QUrl, QRegExp
import MySQLdb as mdb
from homepage import homeWindow
import MySQLconnection as connection


class signInWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.user_id = None
        self.initUI()

    def initUI(self): 
        self.setWindowTitle('Sign In')
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

        self.Signin_label = QLabel('Sign in ', self)
        self.Signin_label.setGeometry(130, 150, 180, 40) 
        self.Signin_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Quicksand"; 
            font-weight: bold;
            font-size: 22px;
            text-align: left;
            word-wrap: break-word;
        ''') 


        self.hi_label = QLabel('Hi there! Nice to see you again.', self)
        self.hi_label.setGeometry(70, 130, 250, 200) 
        self.hi_label.setStyleSheet('''
            color: #989EB1;
            font-family: "Asap";
            font-weight: 400;
            font-size: 14px;
            text-align: left;
        ''') 

        # Εισαγωγή της εικόνας στο QLabel
        image_label = QLabel(self)
        image_label.setGeometry(50, 70, 250, 70)
        pixmap = QPixmap('logo.png')
        image_label.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))


         # Πεδίο για εισαγωγή του email
        self.email_label = QLabel('E-mail:', self)
        self.email_label.setGeometry(70, 270, 200, 20) 
        self.email_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap"; 
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(70, 290, 200, 30)
        self.email_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;  
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 14px;
        ''')
        email_validator = QRegExpValidator(QRegExp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'))
        self.email_input.setValidator(email_validator)
        
        # Πεδίο για εισαγωγή του κωδικού
        self.password_label = QLabel('Password:', self)
        self.password_label.setGeometry(70, 370, 200, 20)  
        self.password_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''')
        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(70, 390, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)  
        self.password_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;  
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 14px;
        ''')

        self.show_password_icon = QLabel(self)
        self.show_password_icon.setGeometry(245, 388, 30, 30)
        self.show_password_icon.setPixmap(QPixmap("visible.png"))
        self.show_password_icon.setScaledContents(True)
        self.show_password_icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_password_icon.mousePressEvent = self.toggle_password_visibility
        self.password_input.setEchoMode(QLineEdit.Normal)
        
        


        # κουμπί για είσοδος
        submit_button = QPushButton('Είσοδος', self)
        submit_button.setGeometry(70, 480, 200, 30)
        submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        submit_button.clicked.connect(self.button_signin_pressed) 
        submit_button.setStyleSheet('''
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

        #να βγαλουμε απο τα μοκαπ την συνδεση με google!! δεν υπαρχει λογοσ για εξτρα δουλεια !


    def button_signin_pressed(self):
        email = self.email_input.text()
        password = self.password_input.text()



        if not email or not password:
            print("Παρακαλώ συμπληρώστε όλα τα πεδία.")
            return

        # τα στοιχεία σύνδεσης των ιδιοκτήτων parking --> στην σελίδα για ειδοποιήσεις κρατήσεων 
        if (email == "mparakou7@gmail.com" and password == "1234") or (email == "balasis123@gmail.com" and password == "1234") or (email == "mousele4@gmail.com" and password == "1234") or (email == "mhnogiannhs5@gmail.com" and password == "1234"):
            self.close()
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()

            cursor.execute("SELECT park_Owner_id FROM Parking_owner WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()  # save ότι επιστρέφει η εντολή
            print("EMAIL: ",email)
            print("result: ",result[0])
            if result:
                self.user_id = result[0]


                from parkingOwnerPage import ParkingOwnerWindow
                self.special_window = ParkingOwnerWindow(self.user_id)
                self.special_window.show()
                print("id:",self.user_id)
                return
      
        
        

        try:
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()

            cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()  # save ότι επιστρέφει η εντολή

            if result:
                self.user_id = result[0]  # save το id του χρήστη που συνδέθηκε = user_id
                self.user_email = email 
                print("Successful login! User ID:", self.user_id) # για τις κρατήσεις
                print("Successful login! User email:", self.user_email) # το χρησιμοποιούμε στο homepage

                # κλείσιμο window
                self.close()

                # μεταφορά στο μενού
                self.home_page_window = homeWindow(self.user_email, self.user_id)
                self.home_page_window.show()

            else:
                print("Λάθος στοιχεία. Δοκιμάστε ξανά!")

        except Exception as e:
            print("error:", e)

    def toggle_password_visibility(self, event):
        if self.password_input.echoMode() == QLineEdit.Normal:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.show_password_icon.setPixmap(QPixmap("visible.png"))
        else:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.show_password_icon.setPixmap(QPixmap("hide.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = signInWindow()
    window.show()
    sys.exit(app.exec_())
