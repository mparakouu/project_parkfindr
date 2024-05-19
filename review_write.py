import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox ,QTextEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor , QIcon 
from PyQt5.QtCore import Qt , QSize
import MySQLdb as mdb
import MySQLconnection as connection

class ReviewSubmitWindow(QMainWindow):
    def __init__(self, rating, review_for):
        super().__init__()
        self.initUI()
        self.rating = rating
        self.review_for = review_for
        

    def initUI(self):
        self.setWindowTitle('Customer Review')
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

        label_review = QLabel('Leave a review:' , self)
        label_review.setGeometry(30, 50, 434, 74)
        label_review.setObjectName('leave-a-review')
        label_review.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center

        '''  )

        self.review_input = QTextEdit(self)
        self.review_input.setGeometry(30, 140, 280, 420)
        self.review_input.setStyleSheet('''
            width: 344px;
            height: 492px;
            padding: 4px 8px 4px 8px;
            background: #FFFFFF;
            color: #7A7A7A;
            border-color: #232323;
            border-width: 1px;
            border-style: solid;
            border-radius: 3px 3px 3px 3px;
            font-family: "Helvetica";
            font-weight: 400;
            font-size: 14px;
            line-height: 1.3;
            text-align: left;

        ''')
        button_submit = QPushButton('Submit', self)
        button_submit.setGeometry(175, 590, 140, 48)
        button_submit.setObjectName('button-submit')
        button_submit.setCursor(QCursor(Qt.PointingHandCursor))
        button_submit.clicked.connect(self.submit_clicked) 
        button_submit.setStyleSheet('''
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

        button_back = QPushButton('Back', self)
        button_back.setGeometry(30, 590, 140, 48)
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
        
    def submit_clicked(self):
        print("Sumbit clicked") 
        review_text = self.review_input.toPlainText()
        #θα κάνω εδώ σύνδεση με την βάση δεδομένων και θα τα βάλω στον πίνακα που έφτιαξα 
        try:
            db = connection.connection()  #σύνδεση με το MySQLconnection.py
            cursor = db.cursor()


            sql = "INSERT INTO reviews (review_text, rating, review_for) VALUES (%s, %s, %s)"
            val = (review_text, self.rating, self.review_for)
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

            QMessageBox.information(self, "Success", "Your review has been submitted successfully!")
            self.close()

        except mdb.Error as e:
            print("Error:", e)
            QMessageBox.critical(self, "Database Error", f"An error occurred while submitting your review: {e}")

    def back_clicked(self):
        print("Back clicked") 
        from review_main import ReviewWindow 
        self.review_window = ReviewWindow()
        self.review_window.show()
        self.close()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReviewSubmitWindow()
    window.show()
    sys.exit(app.exec_())        