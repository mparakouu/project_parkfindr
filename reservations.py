import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import MySQLdb as mdb

class ReservationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadData()

    def initUI(self):
        self.setWindowTitle('Reservations')
        self.setGeometry(100, 100, 340, 667)

        # Περίγραμμα iPhone 
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

        # Εισαγωγή Label Reservations
        self.plus_label = QLabel('Reservations', self)
        self.plus_label.setGeometry(30, 75, 287, 74)
        self.plus_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Quicksand";
            font-weight: bold;
            font-size: 24px;
            text-align: left;
        ''')

        # Underline 
        line = QLabel(self)
        line.setGeometry(30, 130, 270, 1)
        line.setStyleSheet('''
            background: #FFFFFF;
            border-color: #00000000;
            border-bottom: 2px solid #ccc;
        ''')

        # Underline 
        line = QLabel(self)
        line.setGeometry(200, 130, 105, 2)
        line.setStyleSheet('''
            background: #FFFFFF;
            border-color: #00000000;
            border-bottom: 2px solid #3D8AF7;
        ''')


        # Δημιουργία πίνακα
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)  
        self.table.setHorizontalHeaderLabels(['Code', 'Date', 'Status'])
        

        # Ρύθμιση του μεγέθους των κελιών
        self.table.verticalHeader().setDefaultSectionSize(30) 
        self.table.horizontalHeader().setDefaultSectionSize(83)  
        self.table.setShowGrid(False)
        
        #Aπόκρυψη αρίθμησης στήλης
        self.table.verticalHeader().setVisible(False)

        # Αλλαγή χρώματος και πάχους των γραμμών πλέγματος
        self.table.setStyleSheet('''
            QTableWidget {
                background-color: #FFFFFF;  
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
        self.table.setGeometry(table_x, 150, table_width, 430)

    def resizeEvent(self, event):
        # Επανακεντράρισμα του πίνακα όταν αλλάζει το μέγεθος του παραθύρου
        self.centerTable()
        super().resizeEvent(event)

    def loadData(self):
        # Σύνδεση με τη βάση δεδομένων
        db = mdb.connect('localhost', 'root', 'admin', 'ParkFindr')
        cursor = db.cursor()

        # Ανάκτηση δεδομένων από τον πίνακα
        sql_insert = "SELECT * FROM reservations"
        cursor.execute(sql_insert)
        rows = cursor.fetchall()

        # Προσθήκη δεδομένων στον πίνακα
        self.table.setRowCount(len(rows))  # Ορισμός αριθμού γραμμών

        for row_num, row_data in enumerate(rows):
                # Αντικατάσταση της πρώτης στήλης με κουμπιά
                button = QPushButton(str(row_data[0]))
                button.setStyleSheet('''
                    QPushButton {
                        background-color: white;
                        border: none;
                        color: #3D8AF7;
                        font-family: "Quicksand";
                        font-weight: bold;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        color: #6FAFE0;
                    }
                    QPushButton:pressed {
                        background-color: #5B97C6;
                    }
                ''')
                self.table.setCellWidget(row_num, 0, button)

                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)  # Κεντράρισμα του κειμένου
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.table.setItem(row_num, col_num, item)
        
        # exit
        cursor.close()
        db.close()
     
        # Κλείσιμο παραθύρου
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReservationsWindow()
    window.show()
    sys.exit(app.exec_())
