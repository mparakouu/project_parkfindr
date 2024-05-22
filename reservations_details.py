import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QTableWidget, QTableWidgetItem, QPushButton,QHeaderView
from PyQt5.QtGui import QPixmap,QCursor
from PyQt5.QtCore import Qt
import MySQLconnection as connection


class ReservationsDetailsWindow(QMainWindow):
    def __init__(self, code, status , user_id , user_email):
        super().__init__()
        self.code = code
        self.status = status
        self.user_id = user_id
        self.user_email= user_email
        self.initUI()
        self.loadData()

      

    def initUI(self):

        self.setWindowTitle('Reservations Details')
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
        self.resdet_label = QLabel('Reservations Details' , self)
        self.resdet_label.setGeometry(30, 75, 287, 74)
        self.resdet_label.setStyleSheet('''
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
         
        # Ρύθμιση του μεγέθους των κελιών
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  
        self.table.setShowGrid(False)
        
        #Aπόκρυψη αρίθμησης στήλης
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)

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

        #Button Review
        button_review = QPushButton('Review',self)
        button_review.setGeometry(50,550,100,37)
        button_review.setCursor(QCursor(Qt.PointingHandCursor))
        button_review.clicked.connect(self.review_pressed) 
        button_review.setStyleSheet('''
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

        #Button Cancel
        button_cancel = QPushButton('Cancel',self)
        button_cancel.setGeometry(195,550,100,37)
        button_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        button_cancel.clicked.connect(self.cancel_pressed) 
        button_cancel.setStyleSheet('''
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
        
        if self.status == "Cancelled" or self.status == "Confirmed":
            button_cancel.hide()
            button_review.setGeometry(125,500,100,37)
                
            
            

    def review_pressed(self):
        print("review clicked")  
        from review_main import ReviewWindow
        self.review_contact_window = ReviewWindow(self.code , self.user_id) 
        self.review_contact_window.show()
        self.close()

    def cancel_pressed(self):
        print("cancel clicked")  
        from reservations import ReservationsWindow
        
        #σύνδεση με το MySQLconnection.py
        db = connection.connection()  
        cursor = db.cursor()

        try:
            if self.status == "Waiting":
                # Ενημέρωση του πίνακα reservationsdetails
                sql_update_reservation_details = "UPDATE reservationsdetails SET state = 'Cancelled' WHERE id_code = %s"
                cursor.execute(sql_update_reservation_details, (self.code,))

                # Ενημέρωση του πίνακα reservations
                sql_update_reservation = "UPDATE reservations SET status = 'Cancelled' WHERE code = %s"
                cursor.execute(sql_update_reservation, (self.code,))

                # Ενημέρωση του πίνακα createReservation
                sql_update_create_reservation = "UPDATE createReservation SET status = 'Cancelled' WHERE reservationNum = %s"
                cursor.execute(sql_update_create_reservation, (self.code,))

                db.commit()

        except Exception as e:
            db.rollback()
            print(f"An error occurred: {e}")
        
        
        
        cursor.close()
        db.close()

        # Ανανέωση των δεδομένων στον πίνακα
        self.loadData()

        # Κλείσιμο της τρέχουσας παραθύρου
        self.close()


        self.review_contact_window = ReservationsWindow(self.user_email, self.user_id)
        self.review_contact_window.show()
        self.close()


    def centerTable(self):
        # Υπολογισμός και εφαρμογή νέων διαστάσεων και θέσης για τον πίνακα
        table_width = int(self.width() * 0.8)  #
        table_x = int((self.width() - table_width) // 2)
        self.table.setGeometry(table_x, 200, table_width, 214)

    def resizeEvent(self, event):
        # Επανακεντράρισμα του πίνακα όταν αλλάζει το μέγεθος του παραθύρου
        self.centerTable()
        super().resizeEvent(event)

    def loadData(self):
        # Σύνδεση με τη βάση δεδομένων
        db = connection.connection()  #σύνδεση με το MySQLconnection.py
        cursor = db.cursor()

        # Ανάκτηση δεδομένων από τον πίνακα
        sql_select = "SELECT * FROM reservationsdetails WHERE id_code = %s "
        cursor.execute(sql_select,(self.code,))
        rows = cursor.fetchall()

        # Προσθήκη δεδομένων στον πίνακα
        self.table.setColumnCount(2)  # Ορισμός αριθμού στηλών
        self.table.setRowCount(len(rows)*7)  # Ορισμός αριθμού γραμμών

        for row_num, row_data in enumerate(rows):
            for i, data in enumerate(['Code', 'Parking Name', 'Address', 'State', 'Date', 'Duration', 'Spot']):
                item_label = QTableWidgetItem(f"{data}:")
                item_label.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.table.setItem(row_num * 7 + i, 0, item_label)

                item_data = QTableWidgetItem(str(row_data[i]))
                item_data.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.table.setItem(row_num * 7 + i, 1, item_data)
        
        # exit
        cursor.close()
        db.close()
     
        # Κλείσιμο παραθύρου
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReservationsDetailsWindow()
    window.show()
    sys.exit(app.exec_())