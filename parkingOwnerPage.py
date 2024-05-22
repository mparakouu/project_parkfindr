import sys
from PyQt5.QtWidgets import QApplication,QHeaderView, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox,QTableWidget,QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QIcon, QDesktopServices, QRegExpValidator
from PyQt5.QtCore import Qt, QSize, QUrl, QRegExp


import MySQLconnection as connection


class ParkingOwnerWindow(QMainWindow): 
    def __init__(self,user_id):
        super().__init__()
        self.user_id = user_id
        print("id:",self.user_id)
        self.initUI()
        self.loadParkingName()
        self.loadData()

    def initUI(self): 
        self.setWindowTitle('ParkingOwnerPage')
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
        l_res = QLabel('Reservations Info', self)
        l_res.setGeometry(60, 70, 1020, 60)
        l_res.setStyleSheet('''
            width: 287px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 25px;
            text-align: left;
        ''')
        # Δημιουργία πίνακα
        self.table = QTableWidget(self)
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels([ 'State', 'Duration', 'Spot'])
         
        # Ρύθμιση του μεγέθους των κελιών
        self.table.verticalHeader().setDefaultSectionSize(30) 
        self.table.horizontalHeader().setDefaultSectionSize(90)   
        self.table.setShowGrid(False)
        
        
        #Aπόκρυψη αρίθμησης στήλης
        self.table.verticalHeader().setVisible(False)
        

        # Αλλαγή χρώματος και πάχους των γραμμών πλέγματος
        self.table.setStyleSheet('''
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

    
    def centerTable(self):
        # Υπολογισμός και εφαρμογή νέων διαστάσεων και θέσης για τον πίνακα
        table_width = int(self.width() * 0.8)  #
        table_x = int((self.width() - table_width) // 2)
        self.table.setGeometry(table_x, 150, table_width, 400)
    
    def resizeEvent(self, event):
        # Επανακεντράρισμα του πίνακα όταν αλλάζει το μέγεθος του παραθύρου
        self.centerTable()
        super().resizeEvent(event)
    
    def loadParkingName(self):
        # Σύνδεση με τη βάση δεδομένων
        db = connection.connection()  #σύνδεση με το MySQLconnection.py
        cursor = db.cursor()
        # Ανάκτηση δεδομένων από τον πίνακα
        sql_select = "SELECT parking_name FROM parkingData WHERE parking_owner_id= %s "
        cursor.execute(sql_select,(self.user_id,))
        result=cursor.fetchone()
        self.pname=result[0]
        print("ID",self.user_id)
        print("Name",self.pname)

       

    def loadData(self):
        # Σύνδεση με τη βάση δεδομένων
        db = connection.connection()  #σύνδεση με το MySQLconnection.py
        cursor = db.cursor()
        # Ανάκτηση δεδομένων από τον πίνακα
        sql_select = "SELECT state, duration, spot FROM reservationsdetails WHERE parking_name= %s "
        cursor.execute(sql_select,(self.pname,))
        rows = cursor.fetchall()

         # Ορισμός αριθμού στηλών και τίτλων στηλών
        


        # Ορισμός αριθμού γραμμών
        self.table.setRowCount(len(rows))

        # Προσθήκη δεδομένων στον πίνακα
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.table.setItem(row_num, col_num, item)

        

        # Εκκίνηση και λειτουργία
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParkingOwnerWindow()
    window.show()
    sys.exit(app.exec_())