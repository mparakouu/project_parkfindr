import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QMessageBox, QVBoxLayout, QWidget, QLabel, QSlider, QHBoxLayout, QScrollBar, QScrollArea, QSplitter
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess


class homeWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('ParkFindr')
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


        self.Choose_plan_label = QLabel('Select your duration time:', self)
        self.Choose_plan_label.setGeometry(70, 130, 200, 200) 
        self.Choose_plan_label.setStyleSheet('''
            color: #3D8AF7;
            font-family: "Asap";
            font-weight: 600;
            font-size: 18px;
            margin-left: 25px;
        ''') 


         # Δημιουργία του πίνακα με κύλιση
        scrollArea = QScrollArea(self)
        scrollArea.setGeometry(70, 250, 200, 200)  # Ρυθμίστε τις διαστάσεις και τη θέση ανάλογα με τις ανάγκες σας
        scrollWidget = QWidget()
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollArea.setWidget(scrollWidget)
        scrollArea.setWidgetResizable(True)

        # Προσθέστε τα στοιχεία του πίνακα στο scrollLayout
        for i in range(20):  # Παράδειγμα: Δημιουργία 20 ετικετών (labels) για επιλογή
            label = QLabel(f'Item {i}', self)  # Αντικαταστήστε αυτό με τα δεδομένα σας
            scrollLayout.addWidget(label)

        # Εμφάνιση του παραθύρου
        self.show()
       


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = homeWindow()
    window.show()
    sys.exit(app.exec_())