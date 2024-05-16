import sys
import io
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QCursor,QIcon
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtCore import QProcess
from signin import signInWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView # type: ignore #pip install PyQtWebEngine
import folium # type: ignore #kante pip install folium


class selectParking(QMainWindow):
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


        label_review = QLabel('Select Parking:' , self)
        label_review.setGeometry(90, 20, 434, 74)
        label_review.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;

        '''  )
        filtr = QPushButton(self)
        filtr.setIcon(QIcon('filter.png'))
        filtr.setIconSize(QSize(50, 50))
        filtr.setFixedSize(50, 50)
        filtr.setCursor(QCursor(Qt.PointingHandCursor))
        filtr.setGeometry(270,36,434,74)
        filtr.setStyleSheet('''
                border: none;
                padding: 0;
                 color: #3D8AF7;
            ''')
        
        coordinate = (38.261656677847824, 21.748691029725343)#συντεταγμενεσ για πατρα
        m = folium.Map(
                title='patras',
        	zoom_start=13,
        	location=coordinate
        )
        data=io.BytesIO()
        m.save(data,close_file=False)
        webView = QWebEngineView(self)
        webView.setHtml(data.getvalue().decode())
        QLayout.addWidget(webView)


        button_next = QPushButton('Back', self)
        button_next.setGeometry(30, 550, 140, 48)
        button_next.setObjectName('button-14')
        button_next.setCursor(QCursor(Qt.PointingHandCursor))
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

        button_contact = QPushButton('Next', self)
        button_contact.setGeometry(175, 550, 140, 48)
        button_contact.setObjectName('button-15')
        button_contact.setCursor(QCursor(Qt.PointingHandCursor))
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
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = selectParking()
    window.show()
    sys.exit(app.exec_())
    