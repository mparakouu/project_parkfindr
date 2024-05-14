from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
import MySQLdb as mdb
 
# εγω ειχα κατεβασμενα : brew install mysql-client (εντολη mac) , pip install mysql-connector-python , να εχετε τα αντιστοιχα 

# τρέχω για να διατηρώ την σύνδεση (ο καθένας στο path του)
# python /Users/georgiamparakou/Desktop/project_software_technology/project_parkfindr/mysql_connection.py
# ή
# python3 /Users/georgiamparakou/Desktop/project_software_technology/project_parkfindr/mysql_connection.py

 
class Window(QDialog):
    def __init__(self):
        super().__init__()
 
        # window 
        self.title = "Codeloop.org - PyQt5 Database"
        self.top = 150
        self.left = 180 
        self.width = 220
        self.height = 100
 
        
        self.DBConnection()
 
    def DBConnection(self):
        try:
            # Σύνδεση με την βάση
            db = mdb.connect('localhost', 'root', 'giannis', 'ParkFindr')
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Database connected!")
            terminate_button = msg_box.addButton("Terminate connection", QMessageBox.ActionRole)
            msg_box.exec_()

            # όταν terminate connection --> σταματάει την σύνδεση
            if msg_box.clickedButton() == terminate_button:
                sys.exit()
 
        except mdb.Error as e:
            # errors
            QMessageBox.about(self, 'Connection', 'Failed!')
            # exit when error
            sys.exit(1)
 

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())