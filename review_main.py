import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QCheckBox , QBoxLayout , QButtonGroup , QMessageBox 
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor , QIcon 
from PyQt5.QtCore import Qt , QSize
from review_write import ReviewSubmitWindow

#gia thn dhmiourgia toy 5-star rating
class RatingWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.rating=0
         

    def initUI(self):
        self.stars = []

        for i in range(5):
            star = QPushButton(self)
            star.setIcon(QIcon('white-star.png'))
            star.setIconSize(QSize(30, 30))
            star.setFixedSize(30, 30)
            star.setCursor(QCursor(Qt.PointingHandCursor))
            star.setStyleSheet('''
                border: none;
                padding: 0;
            ''')
            star.clicked.connect(self.star_clicked)
            self.stars.append(star)

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        for star in self.stars:
            layout.addWidget(star)
        self.setLayout(layout)

        self.button_group = QButtonGroup()
        for i, star in enumerate(self.stars):
            self.button_group.addButton(star, i + 1)

           

    def star_clicked(self):
        clicked_star = self.sender()
        clicked_index = self.stars.index(clicked_star)
        self.rating = clicked_index + 1  # Αποθήκευση του αριθμού των αστεριών
        for i, star in enumerate(self.stars):
            if i <= clicked_index:
                star.setIcon(QIcon('star.png'))
            else:
                star.setIcon(QIcon('white-star.png'))

        print(f"You rated {clicked_index + 1} stars")


class ReviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.star_rating = None

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

        label_review = QLabel('Review' , self)
        label_review.setGeometry(120, 50, 434, 74)
        label_review.setObjectName('review')
        label_review.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 24px;
            text-align: center;

        '''  )

        label_who = QLabel('Who would you like to review:', self)
        label_who.setGeometry(30, 130, 431, 74)
        label_who.setObjectName('who-whould-you-like-to-review-')
        label_who.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 18px;
            text-align: center;

         ''')

        self.label_parking = QCheckBox('  Parking Space', self)
        self.label_parking.setGeometry(30, 180, 431, 74)
        self.label_parking.setObjectName('parking-space-')
        self.label_parking.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_parking.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #000000;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;

         ''')
        

        self.label_app = QCheckBox('  ParkFindr App', self)
        self.label_app.setGeometry(30, 220, 431, 94)
        self.label_app.setObjectName('parkfindr-app-')
        self.label_app.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_app.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #000000;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;

         ''')

        label_who = QLabel('Rate from 1(bad) to 5(excellent):', self)
        label_who.setGeometry(30, 320, 431, 74)
        label_who.setObjectName('rate-')
        label_who.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 17px;
            text-align: center;

         ''')
        
        self.rating_widget = RatingWidget(self)
        self.rating_widget.setGeometry(70, 370, 200, 40)

        button_next = QPushButton('Next', self)
        button_next.setGeometry(175, 550, 140, 48)
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

        button_contact = QPushButton('Contact', self)
        button_contact.setGeometry(30, 550, 140, 48)
        button_contact.setObjectName('button-15')
        button_contact.setCursor(QCursor(Qt.PointingHandCursor))
        button_contact.clicked.connect(self.contact_clicked) #prepei na orisoyme poy pane otan kanei click
        button_contact.setStyleSheet('''
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



    def next_clicked(self):
        print("Next clicked") 

        review_for = None
        if self.label_parking.isChecked():
            review_for = "Parking Space"
        elif self.label_app.isChecked():
            review_for = "ParkFindr App"
        
        if not review_for:
            QMessageBox.warning(self, "Input Error", "Please select who you want to rate.")
            return
        
        self.star_rating = self.rating_widget.rating
        if self.star_rating == 0:
            QMessageBox.warning(self, "Input Error", "Please provide a rating.")
            return
        self.review_submit_window = ReviewSubmitWindow(self.star_rating, review_for) #θα τα χρειαστώ για όταν κάνω sumbit να αποθηκέυονται στην βάση δεδομένων 
        self.review_submit_window.show() 
        self.close()

    def contact_clicked(self):
        print("Contact clicked")  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReviewWindow()
    window.show()
    sys.exit(app.exec_())
