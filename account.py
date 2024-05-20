import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from PyQt5.QtWebEngineWidgets import QWebEngineView 
import MySQLconnection as connection
from PyQt5.QtCore import pyqtSignal

class accountWindow(QMainWindow):
    photo_uploaded = pyqtSignal(str)
    def __init__(self,user_mail):
        super().__init__() 
        self.user_mail = user_mail
        self.initUI() 
        self.loadData()

    def initUI(self):
        self.setWindowTitle('Account')
        self.setGeometry(100, 100, 340, 667)
  
        # Κύριο πλαίσιο του iPhone
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
        # Εισαγωγή φωτογραφίας
        self.photo_frame = QFrame(self)
        self.photo_frame.setGeometry(122, 165, 100, 100)
        self.photo_frame.setStyleSheet('''
            background-color: #E0E0E0;
            border: 2px dashed #AAAAAA;
            border-radius: 5px;
        ''')
        # Εισαγωγή του λογότυπου 
        logo_png = QLabel(self)
        logo_png.setGeometry(50, 50, 250, 70)
        pixmap = QPixmap('logo.png')
        logo_png.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))
        # Κουμπί 
        self.photo_button = QPushButton('Upload Photo', self)
        self.photo_button.setGeometry(115, 270, 120, 30)
        self.photo_button.clicked.connect(self.uploadPhoto)
        self.photo_button.setStyleSheet('''
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 1px;
            border-style: solid;
            border-radius: 6px 6px 6px 6px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 17px;
            text-align: center;
<<<<<<< HEAD
             ''')
=======
        ''')
>>>>>>> ca025501127ce23be3c2666632bd43b0f562cdb8
        l_account = QLabel('Account', self)
        l_account.setGeometry(115, 130, 120, 30)
        l_account.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 30px;
            text-align: left;

        '''  )
       
        # Πεδίο για  Full Name
        self.fullname_label = QLabel('Full Name:', self)
        self.fullname_label.setGeometry(70, 320, 200, 20) 
        self.fullname_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        
        # Πεδίο για  Phone Number
        self.number_label = QLabel('Phone Number:', self)
        self.number_label.setGeometry(70, 380, 200, 20) 
        self.number_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        
        # Πεδίο για  email
        self.mail_label = QLabel('E-mail:', self)
        self.mail_label.setGeometry(70, 440, 200, 20) 
        self.mail_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        label_mail = QLabel(self.user_mail,self)
        label_mail.setGeometry(70,470,200,20)
        label_mail.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
        ''')
         # Πεδίο για  Password
        self.pwd_label = QLabel('Password:', self)
        self.pwd_label.setGeometry(70, 490, 200, 20) 
        self.pwd_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            text-align: left;
        ''') 
        button_next = QPushButton('Back', self)
        button_next.setGeometry(100, 550, 140, 48)
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.back_clicked) 
        button_next.setStyleSheet('''
            width: 140px;
            height: 48px;
            padding: 0px 10px 0px 10px;
            background: #75A9F9;
            color: #FFFFFF;
            border-color: #FFFFFF;
            border-width: 3px;
            border-style: solid;
            border-radius: 20px 20px 20px 20px;
            font-family: "Shippori Antique B1";
            font-weight: bold;
            font-size: 19px;
            font-style: italic;
            text-align: center;
                                  
         ''')
    def loadData(self):
         # Σύνδεση με τη βάση δεδομένων
         db = connection.connection()  #σύνδεση με το MySQLconnection.py
         cursor = db.cursor()

         sql = "SELECT full_name,phone,password from user WHERE email= %s"
         cursor.execute(sql, (self.user_mail,))  # χρησημοποισω το μειλ σαν παραμετρο
         
         result = cursor.fetchone()
         db.close()
         if result:
           full_name,phone,password = result


           self.fullname_data = QLabel(full_name, self)
           self.fullname_data.setGeometry(70, 350, 200, 20)
           self.fullname_data.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
            ''')

          # Display phone number
           self.number_data = QLabel(phone, self)
           self.number_data.setGeometry(70, 410, 200, 20)
           self.number_data.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
            ''')

           self.password_data=QLabel(password,self)
           self.password_data.setGeometry(70, 520, 200, 20)
           self.password_data.setStyleSheet('''
            color: #3D8AF7;  
            font-family: "Asap"; 
            font-weight: bold; 
            font-size: 12px; 
            ''')
    def uploadPhoto(self) :  
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', '', 'Image Files (*.png *.jpg *.jpeg)')
        if filename:
            print("photo path:", filename)
            self.photo_button.setHidden(True)
            self.photo_label = QLabel(self.photo_frame)
            self.photo_label.setGeometry(0, 0, 100, 100)
            self.photo_label.setAlignment(Qt.AlignCenter)
            self.photo_label.setStyleSheet(f"""
                QLabel {{
                    border: 2px solid #d6d6d6;
                    background-image: url({filename});
                    background-repeat: no-repeat;
                    background-position: center;
                    border-radius: 5px;
                }}
            """)
            self.photo_label.show()
            self.photo_uploaded.emit(filename)
        
    def back_clicked(self):
        print("back clicked")
        from homepage import homeWindow
        self.homeWindow=homeWindow(self.user_mail)
        self.homeWindow.show()
        self.close()


           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = accountWindow("example@example.com")
    window.show()
    sys.exit(app.exec_())
