import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTableWidget, QPushButton , QTableWidgetItem
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

        self.tableWidget = QTableWidget(self) 
        table_width=260 
        table_height=300
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        table_x = (self.width() - table_width) // 2  
        self.tableWidget.setGeometry(table_x, 120, table_width, table_height) 
        self.tableWidget.setStyleSheet('''
            QTableWidget {
                border: none;
            }
            QTableWidget::item {
                padding-left: 10px;  # Προσθέστε περιθώρια στα κελιά
                padding-right: 10px;
                padding-top: 5px;
                padding-bottom: 5px;
            }                           
        ''')
        self.fetch_data_from_database()

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

            if rows:
                self.tableWidget.setRowCount(len(rows[0]))
                self.tableWidget.setColumnCount(len(rows))

                for row_index, row in enumerate(rows):
                    for col_index, col_data in enumerate(row):
                        item =QTableWidgetItem(str(col_data))
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                        self.tableWidget.setItem(col_index, row_index, item)

                        
        except Exception as e:
            # error
            print("Error:", e)

    def back_clicked(self):
        print("Back clicked") 
        from review_main import ReviewWindow 
        self.review_window = ReviewWindow()
        self.review_window.show()
        self.close()

    def next_clicked(self):
        print("Next clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactWindow()
    window.show()
    sys.exit(app.exec_())