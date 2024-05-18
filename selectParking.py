import sys
import io
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QCursor, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QProcess
from PyQt5.QtWebEngineWidgets import QWebEngineView  # type: ignore #pip install PyQtWebEngine
import folium  # type: ignore #kante pip install folium


#κλαση για το παραθυρο με τα φλτρα
class FilterOptions(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet('''
            background-color: #75A9F9;
            border: 2px solid #3D8AF7;
            border-radius: 10px;
            padding: 5px;
        ''')
        layout = QVBoxLayout()

        button1 = QPushButton("Button 1", self)
        button1.setStyleSheet('''
            width: 100px;
            height: 40px;
            background-color: #3D8AF7;
            color: #FFFFFF;
            border: none;
            border-radius: 10px;
            font-family: "Helvetica";
            font-weight: bold;
            font-size: 16px;
        ''')
        layout.addWidget(button1)
        button1.clicked.connect(self.openFilter1)

        button2 = QPushButton("Button 2", self)
        button2.setStyleSheet('''
            width: 120px;
            height: 40px;
            background-color: #3D8AF7;
            color: #FFFFFF;
            border: none;
            border-radius: 10px;
            font-family: "Helvetica";
            font-weight: bold;
            font-size: 16px;
        ''')
        layout.addWidget(button2)
        button2.clicked.connect(self.openFilter2)

        self.setLayout(layout)
    
    def openFilter1(self):
        print("button 1 clicked")
        
    def openFilter2(self):
        print("button 2 clicked")
class selectParking(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Select Parking')
        self.setGeometry(100, 100, 340, 667)

        # περίγραμμα του iPhone
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

        label_park = QLabel('Select Parking:', self)
        label_park.setGeometry(90, 20, 434, 74)
        label_park.setStyleSheet('''
            width: 434px;
            height: 74px;
            color: #3D8AF7;
            font-family: "DynaPuff";
            font-weight: bold;
            font-size: 20px;
            text-align: center;

        ''')
        filtr = QPushButton(self)
        filtr.setIcon(QIcon('filter.png'))
        filtr.setIconSize(QSize(50, 50))
        filtr.setFixedSize(50, 50)
        filtr.setCursor(QCursor(Qt.PointingHandCursor))
        filtr.setGeometry(270, 36, 434, 74)
        filtr.setStyleSheet('''
                border: none;
                padding: 0;
                 color: #3D8AF7;
            ''')
        filtr.clicked.connect(self.showFilterOptions)

        self.filter_options = FilterOptions(self)
        self.filter_options.setGeometry(200, 86, 120, 80)
        self.filter_options.hide()


        button_back = QPushButton('Back', self)
        button_back.setGeometry(30, 550, 140, 48)
        button_back.setObjectName('button-14')
        button_back.setCursor(QCursor(Qt.PointingHandCursor))
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
        button_next.setGeometry(175, 550, 140, 48)
        button_next.setObjectName('button-15')
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

        webView = QWebEngineView(self)
        webView.setGeometry(20, 100, 300, 450)  
        coordinate = (38.261656677847824, 21.748691029725343)  # συντεταγμένες για Πάτρα
        m = folium.Map(
            title='patras',
            zoom_start=15,
            location=coordinate
        )


       # parking markers
        parking_locations = [
            (38.261656677847824, 21.748691029725343 , "1"),
            (38.259656677847824, 21.750691029725343 , "2"),
            (38.263656677847824, 21.746691029725343 , "3"),
            (38.261556377847824, 21.742691029725343 , "4")
        ]

        for lat, lon, id in parking_locations:
            folium.Marker(
                location=(lat, lon),
                popup=folium.Popup(f"ID: {id}", parse_html=True)
            ).add_to(m)
            
        data = io.BytesIO() 
        m.save(data, close_file=False)
        webView.setHtml(data.getvalue().decode()) 
        

    def showFilterOptions(self):
        if self.filter_options.isHidden():
            self.filter_options.show()
        else:
            self.filter_options.hide()
   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = selectParking()
    window.show()
    sys.exit(app.exec_())
