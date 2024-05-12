import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QCheckBox , QBoxLayout , QButtonGroup
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor , QIcon 
from PyQt5.QtCore import Qt , QSize

#gia thn dhmiourgia toy 5-star rating
class RatingWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

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
        clicked_star = self.sender()  # Πάρε το αστέρι που πατήθηκε
        for i, star in enumerate(self.stars):
            if star == clicked_star:  # Βρες το αστέρι που πατήθηκε στη λίστα
                star.setIcon(QIcon('star.png'))  # Αλλαγή εικόνας
            else:
                star.setIcon(QIcon('white-star.png'))


class ReviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

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

        label_parking = QCheckBox(' Parking Space', self)
        label_parking.setGeometry(30, 190, 431, 74)
        label_parking.setObjectName('parking-space-')
        label_parking.setCursor(QCursor(Qt.PointingHandCursor))
        label_parking.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #000000;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;

         ''')
        

        label_app = QCheckBox(' ParkFindr App', self)
        label_app.setGeometry(30, 220, 431, 94)
        label_app.setObjectName('parkfindr-app-')
        label_app.setCursor(QCursor(Qt.PointingHandCursor))
        label_app.setStyleSheet('''
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
        
        rating_widget = RatingWidget(self)
        rating_widget.setGeometry(70, 370, 200, 40)

        button_next = QPushButton('Next', self)
        button_next.setGeometry(30, 550, 140, 48)
        button_next.setObjectName('button-14')
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
        button_next.clicked.connect(self.next_clicked) #prepei na orisoyme poy pane otan kanei click
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
        button_contact.setGeometry(175, 550, 140, 48)
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
        print("Next clicked") #edw tha baloyme leitoyrgia 

    def contact_clicked(self):
        print("Contact clicked") #edw tha baloyme leitoyrgia 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReviewWindow()
    window.show()
    sys.exit(app.exec_())
