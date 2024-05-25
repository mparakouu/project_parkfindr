import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTableWidget, QPushButton , QTableWidgetItem ,QHeaderView
from PyQt5.QtGui import QPixmap, QCursor , QIcon 
from PyQt5.QtCore import Qt 
import MySQLdb as mdb
import MySQLconnection as connection

class ContactWindow(QMainWindow):
    def __init__(self, parking_name, address ,phone_number , open_hours , code , user_id , user_email):
        super().__init__()
        self.parking_name = parking_name
        self.address = address
        self.phone_number =phone_number
        self.open_hours= open_hours
        self.code =code
        self.user_id= user_id
        self.user_email =user_email
        self.initUI()
       

    def initUI(self):
        self.setWindowTitle('Contact Informations')
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

        label_contact = QLabel('Contact Information:', self)
        label_contact.setGeometry(30, 80, 280, 30)  # Ρυθμίστε τις διαστάσεις και τη θέση ανάλογα με τις ανάγκες σας
        label_contact.setStyleSheet('''
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;
        ''')

        self.tableWidget = QTableWidget(self) 
        # Ρύθμιση του μεγέθους των κελιών
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
        self.tableWidget.setShowGrid(False)
        
        #Aπόκρυψη αρίθμησης στήλης
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        # Αλλαγή χρώματος και πάχους των γραμμών πλέγματος
        self.tableWidget.setStyleSheet('''
            QTableWidget {
                background-color: #FFFFFF; 
                border: 1px solid #808080; 
                gridline-color: #F0F0F0;  
            }
            QHeaderView::section {
                background-color: #3D8AF7;
                color: white;
                font-weight: bold;
                font-size: 14px;
                height: 30px;  
                border: 1px solid #FFFFFF; 
            }
            QTableWidget::item {
                border-bottom: 2px solid #3D8AF7;  
                border-right: none;  
                border-left: none;  
                border-top: none;  
            }
        ''')
        # Kεντράρισμα του πίνακα
        self.centerTable()
        
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(1)
        
        self.tableWidget.setItem(0, 0, QTableWidgetItem(f"Parking Name: {self.parking_name}"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(f"Address: {self.address}"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem(f"Phone Number: {self.phone_number}"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem(f"Open Hours: {self.open_hours}"))


        button_back = QPushButton('Back', self)
        button_back.setGeometry(30, 570, 140, 48)
        button_back.setObjectName('button-back')
        button_back.setCursor(QCursor(Qt.PointingHandCursor))
        button_back.clicked.connect(self.back_clicked) 
        button_back.setStyleSheet('''
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
        
        button_next = QPushButton('Next', self)
        button_next.setGeometry(175, 570, 140, 48)
        button_next.setObjectName('button-14')
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.next_clicked) 
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


    def back_clicked(self):
        print("Back clicked") 
        from review_main import ReviewWindow 
        self.review_window = ReviewWindow(self.code ,self.user_id , self.user_email)
        self.review_window.show()
        self.close()

    def next_clicked(self):
        print("Next clicked")
        from homepage import homeWindow
        self.homepage_window = homeWindow( self.user_email , self.user_id)
        self.homepage_window.show()
        self.close()
    
    def centerTable(self):
        # Υπολογισμός και εφαρμογή νέων διαστάσεων και θέσης για τον πίνακα
        table_width = int(self.width() * 0.8)  #
        table_x = int((self.width() - table_width) // 2)
        self.tableWidget.setGeometry(table_x, 200, table_width, 214)

    def resizeEvent(self, event):
        # Επανακεντράρισμα του πίνακα όταν αλλάζει το μέγεθος του παραθύρου
        self.centerTable()
        super().resizeEvent(event)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactWindow()
    window.show()
    sys.exit(app.exec_())