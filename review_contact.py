import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget 
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor , QIcon 
from PyQt5.QtCore import Qt , QSize
from review_write import ReviewSubmitWindow
import MySQLdb as mdb

class ContactWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        tableWidget = QTableWidget(self) 
        table_width=300 
        table_height=200
        table_x = (self.width() - table_width) // 2  
        tableWidget.setGeometry(table_x, 120, table_width, table_height) 

        self.fetch_data_from_database()


    
    def fetch_data_from_database(self):
        try:
            connection = mdb.connect(
                host='localhost',
                user='root',
                password='admin',
                database='ParkFindr'
            )

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM reviews")
            rows = cursor.fetchall()

                # Προσθήκη των δεδομένων σε QLabel widgets
            if rows:
                for row_index, row in enumerate(rows):
                    for col_index, col_data in enumerate(row):
                        data_label = QLabel(str(col_data), self)
                        data_label.setGeometry(50 + col_index * 120, 200 + row_index * 30, 100, 20)
                        data_label.setStyleSheet('''
                            color: #000000;
                            font-family: Arial;
                            font-size: 12px;
                        ''')
                        
        except Exception as e:
            # error
            print("Error:", e)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactWindow()
    window.show()
    sys.exit(app.exec_())