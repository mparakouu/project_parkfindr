import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon, QDesktopServices, QRegExpValidator
from PyQt5.QtCore import Qt , QSize, Qt, QUrl, QRegExp,QEvent
from signin import signInWindow
from chplan import choosePlanWindow
import MySQLconnection as connection


class signUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
       
    
    def initUI(self): 
        self.setWindowTitle('Sign Up')
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

        #Εισαγωγή Label Sign Up
        self.Signup_label = QLabel ('Sign Up', self)
        self.Signup_label.setGeometry(130, 150, 180, 40)
        self.Signup_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Quicksand";
            font-weight: bold;     
            font-size: 22px;
            text-align: left;
            word-wrap: break-word; 
        ''')
 
        #Εισαγωγή του Logo
        image_label = QLabel(self)
        image_label.setGeometry(50, 70, 250, 70)
        pixmap = QPixmap ('logo.png')
        image_label.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))

         # Πεδίο για εισαγωγή του Full Name
        self.fullname_label = QLabel('Full Name', self)
        self.fullname_label.setGeometry(70, 210, 200, 20) 
        self.fullname_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.fullname_input = QLineEdit(self)
        self.fullname_input.setGeometry(70, 230, 200, 30)
        self.fullname_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;  
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 12px;
        ''')

        
         # Πεδίο για εισαγωγή του Phone Number
        self.pnumber_label = QLabel('Phone Number', self)
        self.pnumber_label.setGeometry(70, 270, 200, 20) 
        self.pnumber_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.pnumber_input = QLineEdit(self)
        self.pnumber_input.setGeometry(70, 290, 200, 30)
        self.pnumber_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;  
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 12px;
        ''')

        # Πεδίο για εισαγωγή του email
        self.email_label = QLabel('E-mail', self)
        self.email_label.setGeometry(70, 330, 200, 20) 
        self.email_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(70, 350, 200, 30)
        self.email_input.setPlaceholderText("Your email address")
        self.email_input.textChanged.connect(self.email_changed)
        self.email_input.setStyleSheet('''
            background-color: #FFFFFF;
            color:  #ccc;                         
            border: none;  
            font-size: 13px;
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;                           
        ''')
        self.email_input.installEventFilter(self)
        email_validator = QRegExpValidator(QRegExp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'))
        self.email_input.setValidator(email_validator)
        self.email = " "

    
        # Πεδίο για εισαγωγή του Password
        self.password_label = QLabel('Password', self)
        self.password_label.setGeometry(70, 390, 200, 20) 
        self.password_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(70, 410, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;  
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 12px;
        ''')

        self.show_password_icon = QLabel(self)
        self.show_password_icon.setGeometry(245, 408, 30, 30)
        self.show_password_icon.setPixmap(QPixmap("visible.png"))
        self.show_password_icon.setScaledContents(True)
        self.show_password_icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_password_icon.mousePressEvent = self.toggle_password_visibility
        self.password_input.setEchoMode(QLineEdit.Normal)
        

        # Πεδίο για εισαγωγή του Confirm Password
        self.cpassword_label = QLabel('Confirm Password', self)
        self.cpassword_label.setGeometry(70, 450, 200, 20) 
        self.cpassword_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 14px;
            text-align: left;
        ''') 
        self.cpassword_input = QLineEdit(self)
        self.cpassword_input.setGeometry(70, 470, 200, 30)
        self.cpassword_input.setEchoMode(QLineEdit.Password)
        self.cpassword_input.setStyleSheet('''
            background-color: #FFFFFF;
            border: none;      
            border-bottom: 2px solid #ccc;
            border-radius: 1px;
            padding: 5px;
            font-size: 12px;
        ''')
        self.cpassword_input.setEchoMode(QLineEdit.Normal)

        #CheckBox 
        self.termsCheck = QCheckBox(self)
        self.termsCheck.setGeometry(70, 500, 50, 50)
        self.termsCheck.setCursor(QCursor(Qt.PointingHandCursor))
        self.termsCheck.setStyleSheet('''
            width: 25px;
	        height: 23px;
	        background-color: #FFFFFF;
	        color: #000000;
	       
	        font-weight: 40;
	        font-size: 14px;
	        text-align: left;
        ''')
        self.termsCheck.stateChanged.connect(self.next_button_enable)

        #Terms
        termsmessage = QLabel('I agree to the Terms of Service and Privacy Policy', self)
        termsmessage.setGeometry(100, 504, 200, 42)
        termsmessage.setStyleSheet('''
	        color: #35424A;
	        font-family: "Asap";
	        font-weight: 400;
	        font-size: 13px;
	        line-height: 1.5;
	        text-align: left;
        ''')
        termsmessage.setWordWrap(True)
        colored_text = " I agree to the <font color='#3D8AF7'>Terms of Services</font> and <font color='#3D8AF7'>Privacy Policy</font>"
        termsmessage.setText(colored_text)


        #Button Next
        self.button_next = QPushButton('Next', self)
        self.button_next.setGeometry(90, 570, 175, 36)
        self.button_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_next.clicked.connect(self.next_pressed) # εκτελεί την next_pressed και εισάγει τα data, 
        self.button_next.setStyleSheet('''
	        padding: 8px 8px 8px 8px;
	        box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
	        color: #FFFFFF;
            background: #3D8AF7;
	        border-radius: 6px 6px 6px 6px;
	        font-family: "Asap";
	        font-weight: 600;
	        font-size: 17px; 
	        line-height: 1.3;
	        text-align: center;                    
        ''')
        self.button_next.setEnabled(False)  # Αρχικά απενεργοποιούμε το κουμπί

        # σε πάει στο signin.py 
        acc_exists = QLabel('Have an Account? ',self)
        acc_exists.setGeometry(100, 600, 210, 42)
        acc_exists.setStyleSheet('''
	        color: #35424A;
	        font-family: "Asap";
	        font-weight: 400;
	        font-size: 13px;
	        line-height: 1.5;
	        text-align: left;
        ''')
       

        button_signin = QPushButton('Sign In',self)
        button_signin.setGeometry(208,600,210,42)
        button_signin.setCursor(QCursor(Qt.PointingHandCursor))
        button_signin.clicked.connect(self.signin_pressed) 
        button_signin.setStyleSheet('''
            color: #3D8AF7;
	        font-family: "Asap";
	        font-weight: 400;
	        font-size: 13px;
	        line-height: 1.5;
	        text-align: left;
            border: none;
        ''')


    def email_changed(self,text):
        self.email = text
        print("Email is: ", self.email)
    
    def signin_pressed(self):
        print("signin clicked") 
        self.close()  
        self.sign_in_window = signInWindow()  
        self.sign_in_window.show()

    def eventFilter(self, obj, event):
        if obj == self.email_input:
            if event.type() == QtCore.QEvent.FocusIn:
                self.email_input.setStyleSheet('''
                    background-color: #FFFFFF;
                    color: #000000;
                    border: none;
                    font-size: 16px;
                    border-bottom: 2px solid #ccc;
                    border-radius: 1px;
                    padding: 5px;
                ''')
            elif event.type() == QtCore.QEvent.FocusOut and not self.email_input.text():
                self.email_input.setStyleSheet('''
                    background-color: #FFFFFF;
                    color:  #ccc;
                    border: none;
                    font-size: 16px;
                    border-bottom: 2px solid #ccc;
                    border-radius: 1px;
                    padding: 5px;
                ''')
        return super().eventFilter(obj, event)
       

    # οταν πατηθεί το "next" , εισάγει τα data στο table 
    def next_pressed(self):
        full_name = self.fullname_input.text()
        phone = self.pnumber_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.cpassword_input.text()

        # εάν είναι κενά τα πεδία --> σφαλμα
        if not full_name or not phone or not email or not password:
            print("Παρακαλώ συμπληρώστε όλα τα πεδία.")
            return
        
        # Έλεγχος αν οι κωδικοί ταιριάζουν
        if password != confirm_password:
            print("Οι κωδικοί δεν ταιριάζουν.")
            self.password_input.setStyleSheet('''
                background-color: #FFFFFF;
                border: none;
                border-bottom: 2px solid red;
                border-radius: 1px;
                padding: 5px;
                font-size: 16px;
            ''')
            self.cpassword_input.setStyleSheet('''
                background-color: #FFFFFF;
                border: none;
                border-bottom: 2px solid red;
                border-radius: 1px;
                padding: 5px;
                font-size: 16px;
            ''')
            return
        



        try:
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()

            # insert στο table user
            sql_insert = "INSERT INTO user (full_name, phone, email, password) VALUES (%s, %s, %s, %s)"
            data_insert = (full_name, phone, email, password)

            # εκτέλεση του insert
            cursor.execute(sql_insert, data_insert)
            
            # commit στην βάση
            db.commit()

            sql_select = "SELECT id FROM user WHERE email = %s"
            cursor.execute(sql_select,(email,))
            user_id = cursor.fetchone()[0]
            print("User ID is: ",user_id)

            # exit
            cursor.close()
            db.close()

            # κλείνω signup παράθυρο
            self.close()

            # με πάει στο signin πράθυρο 
            self.choose_plan_window = choosePlanWindow(user_id)
            self.choose_plan_window.show()

            print("Data inserted successfully!")

        except Exception as e:
            # error
            print("Error:", e)

    def toggle_password_visibility(self, event):
        if self.password_input.echoMode() == QLineEdit.Normal:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.cpassword_input.setEchoMode(QLineEdit.Password)
            self.show_password_icon.setPixmap(QPixmap("visible.png"))
        else:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.cpassword_input.setEchoMode(QLineEdit.Normal)
            self.show_password_icon.setPixmap(QPixmap("hide.png"))


    def next_button_enable(self):
        if self.termsCheck.isChecked():
            self.button_next.setEnabled(True)
        else:
            self.button_next.setEnabled(False)

# Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = signUpWindow()
    window.show()
    sys.exit(app.exec_())