import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QVBoxLayout, QWidget, QScrollArea, QRadioButton, QPushButton
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor


class DurationTime(QMainWindow):
    def __init__(self):
        super().__init__() 
        # δεν έχει γίνει επιλογή ώρας ακόμη
        self.selected_duration = None  
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('ParkFindr')
        self.setGeometry(100, 100, 340, 667) 

        # περίγραμμα του iphone 
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

        # εισαγωγή του logo 
        logo_png = QLabel(self)
        logo_png.setGeometry(50, 70, 250, 70)
        pixmap = QPixmap('logo.png')
        logo_png.setPixmap(pixmap.scaled(250, 250, QtCore.Qt.KeepAspectRatio))

        self.duration_time = QLabel('Select your duration time:', self)
        self.duration_time.setGeometry(48, 180, 250, 30)
        self.duration_time.setStyleSheet('''
            color: #75A9F9;
            font-family: "Quicksand";
            font-weight: bold;     
            font-size: 20px;
            text-align: left;
            word-wrap: break-word;                           
        ''')


        # πίνακας με μπάρα κύλιση
        array_with_scroll = QScrollArea(self)
        array_with_scroll.setGeometry(45, 250, 250, 200)
        scroll_widget = QWidget()
        scrollLayout = QVBoxLayout(scroll_widget)
        array_with_scroll.setWidget(scroll_widget)
        array_with_scroll.setWidgetResizable(True)
        array_with_scroll.setStyleSheet('''
            background: #FFFFFF;  
            border-radius: 1px;  
            padding: 5px; 
            QScrollBar:vertical {
                background-color: #3D8AF7;  
                color: #3D8AF7;
                width: 15px;
            }
            QScrollBar::handle:vertical { /* μπάρα κύλισης */
                background-color: #3D8AF7;  
            }
            QScrollBar::add-line:vertical {
                background: none;
            }
            QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        ''')

        # μπάρα κύλισης 
        array_with_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


         # κουμπί next
        next_button = QPushButton('Next', self)
        next_button.setGeometry(155, 550, 140, 35)
        next_button.setCursor(QCursor(Qt.PointingHandCursor))
        next_button.clicked.connect(self.next_button_pressed) 
        next_button.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
            background: #75A9F9;
            color: #FFFFFF;
            border-radius: 15px;  
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            line-height: 1.3;
            text-align: center;
            margin-left: 20px;  
            
        ''')

         # κουμπί back 
        back_button = QPushButton('Back', self)
        back_button.setGeometry(20, 550, 140, 35)
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        #back_button.clicked.connect(self.back_button_pressed) #θα πηγαίνει πίσω στον χάρτη --> select parking
        back_button.setStyleSheet('''
            padding: 8px 8px 8px 8px;
            box-shadow: 0px 5px 10px rgba(248, 95, 106, 0.23);
            background: #75A9F9;
            color: #FFFFFF;
            border-radius: 15px;  
            font-family: "Asap";
            font-weight: 600;
            font-size: 17px;
            line-height: 1.3;
            text-align: center;
            margin-left: 20px;  
        ''')



        duration_time_list = ['30 minutes', '1 hour', '2 hours', '3 hours', '4 hours', '5 hours', '6 hours', '7 hours', '8 hours', '24 hours']

        # όταν επιλέξουμε δεδομένο του πίνακα, ενεργοποιηση 
        self.buttons_with_data = []
        for duration in duration_time_list:
            data_button_chosen = QRadioButton(duration, self)
            data_button_chosen.setChecked(False)
            data_button_chosen.toggled.connect(self.pressed_data_button)
            scrollLayout.addWidget(data_button_chosen)
            self.buttons_with_data.append(data_button_chosen)
            data_button_chosen.setStyleSheet('''
                QRadioButton {
                    color: #3D8AF7;
                    font-family: "Asap";
                    font-weight: 600;
                    font-size: 16px;
                }
            ''')

        

        self.show()

    # όταν επιλεχθεί το κουμπί με την διάρκεια / duration time 
    def pressed_data_button(self):
        data_button = self.sender()
        if data_button.isChecked():
            self.selected_duration_time = data_button.text()

    # όταν πατηθεί το κουμπί next
    def next_button_pressed(self):
        if self.selected_duration_time:
            print("Duration time:", self.selected_duration_time)
        else:
            print("Please select a duration time!")
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DurationTime()
    window.show()
    sys.exit(app.exec_())
