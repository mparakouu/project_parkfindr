import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon, QDesktopServices
from PyQt5.QtCore import Qt , QSize, Qt, QUrl
import MySQLdb as mdb
from homepage import homeWindow


class signInWindow(QMainWindow):
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
        ''')

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
        ''')


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

         # εάν είναι κενά τα πεδία --> σφαλμα
        if not email or not password:
            print("Παρακαλώ συμπληρώστε όλα τα πεδία.")
            return

        try:
            # Σύνδεση στη βάση δεδομένων
            db = mdb.connect('localhost', 'root', 'garfield', 'ParkFindr')
            cursor = db.cursor()

            # ερώτημα SQL
            cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()

            if result:
                # συνδέθηκε
                print("Successful login!")


                # κλείνω signup παράθυρο
                self.close()

                # με πάει στο signin πράθυρο 
                self.home_page_window = homeWindow()
                self.home_page_window.show()


            else:
                # error
                print("Wrong data, try again!")

        except Exception as e:
            # error
            print("Error:", e)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = signInWindow()
    window.show()
    sys.exit(app.exec_())
