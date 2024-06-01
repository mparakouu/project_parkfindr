import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QRegExpValidator
from PyQt5.QtCore import Qt , QRegExp
import MySQLdb as mdb
import MySQLconnection as connection


class paymentWindow(QMainWindow,):
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id  # Αποθήκευση του user_id
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle('Payment')
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

        #Εισαγωγή Label Payment
        self.plus_label = QLabel ('Payment', self)
        self.plus_label.setGeometry(120, 165, 287, 74)
        self.plus_label.setStyleSheet('''
	        color: #3D8AF7;
	        font-family: "Quicksand";
	        font-weight: bold;
	        font-size: 24px;
	        text-align: left;
        ''')

        #Underline 
        line = QLabel(self)
        line.setGeometry(40, 230, 270, 1)
        line.setStyleSheet('''
	        background: #FFFFFF;
	        border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        # Δημιουργία ενός πλαισίου με border
        self.frame = QFrame(self)
        self.frame.setGeometry(40, 280, 260, 200)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(2)
        self.frame.setStyleSheet('''
        border: 2px dashed #87CEFA; 
        border-radius: 5px;
        ''')

        # Όνομα
        self.label_fname = QLabel("FIRST NAME:",self.frame)
        self.label_fname.move(15, 20)
        self.label_fname.setStyleSheet('''
        border: none;
        ''')
        self.input_fname = QLineEdit(self.frame)
        self.input_fname.setGeometry(110, 17, 135, 25)
        self.input_fname.setStyleSheet('''
        background-color: #FFFFFF;
        border: none;      
        border-bottom: 2px solid #87CEFA;
        border-radius: 1px;
        padding: 5px;
        ''')

        # Επίθετο
        self.label_lname = QLabel("LAST NAME:", self.frame)
        self.label_lname.move(15, 50)
        self.label_lname.setStyleSheet('''
        border:none;
        ''')
        self.input_lname = QLineEdit(self.frame)
        self.input_lname.setGeometry(110, 47, 135, 25)
        self.input_lname.setStyleSheet('''
        background-color: #FFFFFF;
        border: none;      
        border-bottom: 2px solid #87CEFA;
        border-radius: 1px;
        padding: 5px;
        ''')

        # Αριθμός Κάρτας
        self.label_card_no = QLabel("CARD NO:", self.frame)
        self.label_card_no.move(15, 80)
        self.label_card_no.setStyleSheet('''
        border:none;
        ''')
        self.input_card_no = QLineEdit(self.frame)
        self.input_card_no.setGeometry(110, 75, 135, 25)
        self.input_card_no.setStyleSheet('''
        background-color: #FFFFFF;
        border: none;      
        border-bottom: 2px solid #87CEFA;
        border-radius: 1px;
        padding: 5px;
        ''')
        # Ορισμός  QValidator για να επιτρέπει μόνο αριθμούς με κενό ανάμεσα τους
        validator_card = QRegExpValidator(QRegExp(r'\d{4}\s\d{4}\s\d{4}\s\d{4}'))
        self.input_card_no.setValidator(validator_card)


        # Ημερομηνία Λήξης
        self.label_exp_date = QLabel("EXP.DATE:", self.frame)
        self.label_exp_date.move(15, 110)
        self.label_exp_date.setStyleSheet('''
        border:none;
        ''')
        self.input_exp_date = QLineEdit(self.frame)
        self.input_exp_date.setGeometry(110, 107, 50, 25)
        self.input_exp_date.setStyleSheet('''
        background-color: #FFFFFF;
        border: none;      
        border-bottom: 2px solid #87CEFA;
        border-radius: 1px;
        padding: 5px;
        ''')
        self.input_expiry_month = QLineEdit(self.frame)
        self.input_expiry_month.setGeometry(110, 107, 30, 20)
        self.input_expiry_month.setPlaceholderText("MM")
        self.input_expiry_month.setStyleSheet('''
        border:none;
        ''')
        self.input_line = QLineEdit("/", self.frame)
        self.input_line.setGeometry(130, 107, 20, 20)
        self.input_line.setDisabled(True)  # Απενεργοποίηση του επεξεργαστή κειμένου
        self.input_line.setStyleSheet('''
        border:none;
        ''')
        self.input_expiry_year = QLineEdit(self.frame)
        self.input_expiry_year.setGeometry(140, 107, 30, 20)
        self.input_expiry_year.setPlaceholderText("YY")
        self.input_expiry_year.setStyleSheet('''
        border:none;
        ''')
        # Ορισμός ενός QValidator για το φορμάτ ημερομηνίας (MM/YY) με περιορισμό του πρώτου διψήφιου σε τιμές 01-12
        validator_date = QRegExpValidator(QRegExp(r'(0[1-9]|1[0-2])'))  
        self.input_expiry_month.setValidator(validator_date) 

        # CVV
        self.label_cvv = QLabel("CVV:", self.frame)
        self.label_cvv.move(15, 140)
        self.label_cvv.setStyleSheet('''
        border:none;
        ''')
        self.input_cvv = QLineEdit(self.frame)
        self.input_cvv.setGeometry(110, 137, 50, 25)
        self.input_cvv.setStyleSheet('''
        background-color: #FFFFFF;
        border: none;      
        border-bottom: 2px solid #87CEFA;
        border-radius: 1px;
        padding: 5px;
        ''')
        # Ορισμός ενός QValidator για το φορμάτ CVV με περιορισμό σε 3 αριθμούς μεταξύ 0 και 9
        validator_cvv = QRegExpValidator(QRegExp(r'\d{3}'))  
        self.input_cvv.setValidator(validator_cvv)


        #Button Proceed
        button_next = QPushButton('Proceed', self)
        button_next.setGeometry(90, 520, 175, 36)
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.proceed_pressed) # εκτελεί την proceed_pressed και εισάγει τα data, 
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

    def proceed_pressed(self):
        FName = self.input_fname.text()
        LName = self.input_lname.text()
        card_n = self.input_card_no.text()
        exp_m = self.input_expiry_month.text()
        exp_y = self.input_expiry_year.text()
        cvv = self.input_cvv.text()
        
        #Εάν είναι κενά τα πεδία να μην μπορεί να πατηθεί το κουμπί
        if not FName or not LName or not card_n or not exp_m or not exp_y or not cvv:
            print("Παρακαλώ συμπληρώστε όλα τα πεδία. ")
            return

        try:
            #Σύνδεση στη Βάση Δεδομένων
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()

            #Πραγματοποίηση Insert στον πίνακα 
            sql = "INSERT INTO payments (FName, LName,user_id) VALUES (%s, %s, %s)" 
            data = (FName, LName,self.user_id)

            #Εκτέλεση
            cursor.execute(sql, data)

            #Commit
            db.commit()

            #Exit
            cursor.close()
            db.close()

            
            self.close()  

            #Πάει στο Success Pay Window 
            from successpay import successpayWindow
            self.sign_in_window = successpayWindow() 
            self.sign_in_window.show()
            
            print("Data inserted successfully!")

        except Exception as e:
            #Σφάλμα
            print("Error",e)




# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_id = 1
    window = paymentWindow()
    window.show()
    sys.exit(app.exec_())