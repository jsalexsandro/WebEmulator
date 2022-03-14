from PyQt5.QtWidgets import QMainWindow,QFrame,QPushButton,QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from urllib.request import urlopen
import bs4
import pyautogui
import json
from requests import get

class WindowApp(QMainWindow):
    title  = "Iphone X Pro"
    width  = 300
    height = 600

    def __init__(self,use):
        super().__init__()
        self.local = "http://localhost:5500"
        if (use == True):
            try:
                print("Using 'device.config'")
                configs = json.loads(open("device.config","rt",encoding="utf-8").read())
                self.local = configs["url"]
                self.width = int(configs["width"])
                if (self.width < 250):
                    self.width = 250
                self.height = int(configs["height"])
                if (self.height < 250):
                    self.height = 250
            except:pass

        print("run:",self.local)

        self.setConfigs()
        self.Frame()
        self.StatusBar()
        self.Nocth()
        self.View()
        self.Buttons()
        self.LeftBar()
        self.setStyles()
        self.openLeftBar = False
        try:
            self.setStatusBar()
        except:pass

    def Move(self):
        x,y = pyautogui.position()
        self.move(x-(self.width/2),y-20)
        
    def Frame(self):
        self.frame = QFrame(self)
        self.frame.mouseMoveEvent = lambda _: self.Move()
        self.frame.setGeometry(0,0,self.width+15,self.height+15)
        self.frame.show()

    def Buttons(self):
        self.button_1 = QFrame(self)
        self.button_1.setGeometry(self.width+10,60,10,100)
        self.button_1.show()
        self.button_2 = QPushButton(self)
        self.button_2.setGeometry(self.width+10,180,10,40)
        self.button_2.clicked.connect(self.close)
        self.button_2.show()    

    def StatusBar(self):
        self.status = QFrame(self.frame)
        self.status.setGeometry(20,20,self.width-24,25)
        self.status.show()

    def setStatusBar(self):
        html = urlopen(self.local).read()
        res = bs4.BeautifulSoup(html,"html5lib")

        themecolor =  str(res.findAll("meta",{"name":"theme-color"})[0])
        tag = themecolor.split('"')
        color = ""
        for c,i in enumerate(tag):
            if ("content" in i):
                color = tag[c+1]
        print(color)
        self.status.setStyleSheet(f"background-color:{color}")

    def Nocth(self):
        self.notch = QFrame(self.frame)
        self.notch.setGeometry(((self.width/2 ) - 90)+10 ,5,180,40)
        self.notch.show()


    def View(self):
        self.web = QWebEngineView(self.frame)   
        self.web.setGeometry(20,45,self.width-24,self.height - 50)
        try :
            get(self.local)
            self.web.setUrl(QtCore.QUrl(self.local))
        except:
            self.web.setHtml(f"<h1>{self.local} not listen <h1>")
        self.web.show()

    def LeftBar(self):
        self.left = QFrame(self)
        self.left.setGeometry(self.width+50,0,60,90)
        self.left.close()

        self.close_btn = QPushButton(self)
        self.close_btn.setGeometry(self.width+50,0,30,30)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setFont(QFont("Times",15,QFont.Bold))
        self.close_btn.setText("×")
        self.close_btn.close()

        self.mini_btn = QPushButton(self)
        self.mini_btn.clicked.connect(self.showMinimized)
        self.mini_btn.setGeometry(self.width+80,0,30,30)
        self.mini_btn.setFont(QFont("Times",30))
        self.mini_btn.setText("-")
        self.mini_btn.close()

        self.close_bar = QPushButton(self)
        self.close_bar.setGeometry(self.width+50,30,60,60)
        self.close_bar.setFont(QFont("Times",30))
        self.close_bar.clicked.connect(self.Open)
        self.close_bar.setText("×")
        self.close_bar.close()
 
        self.reload = QPushButton(self)
        self.reload.setGeometry(self.width+50,90,60,60)
        self.reload.setFont(QFont("Times",30))
        self.reload.setText("⟳")
        self.reload.clicked.connect(self.Reload)
        self.reload.close()

    def setConfigs(self):
        self.setWindowTitle(self.title)
        self.setGeometry(20,20,self.width+200,self.height+100)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setStyles(self):
        self.frame.setStyleSheet("""
QFrame {
    background-color:#2a2b2b;
    border-radius:35px;
}        
""")

        self.status.setStyleSheet("""
QFrame {
    background-color:#ff0000;
    border-radius:0px;
}
""")

        self.notch.setStyleSheet("""
QFrame {
    border-radius:15px;
}        
""")

        self.button_1.setStyleSheet("""
QFrame {
    background-color:#2a2b2b;
}        
""")
        self.button_2.setStyleSheet("""
QPushButton {
    background-color:#2a2b2b;
    border:0px;
}
QPushButton:clicked {
    background-color:#333;
}
""")

        self.left.setStyleSheet("""
QFrame {
    background-color:#2a2b2b;
    border:0px;
}        
""")
        self.close_btn.setStyleSheet("""
QPushButton {
    background-color:#2a2b2b;
    border:0px;
    color:#fff;
}
QPushButton:hover {
    background-color:#333;
}       
""")
        self.mini_btn.setStyleSheet("""
QPushButton {
    background-color:#2a2b2b;
    border:0px;
    color:#fff;
}        
QPushButton:hover {
    background-color:#333;
}  
""")
        self.close_bar.setStyleSheet("""
QPushButton {
    background-color:#2a2b2b;
    border:0px;
    color:#fff;
}     
QPushButton:hover {
    background-color:#333;
}     
""")
        self.reload.setStyleSheet("""
QPushButton {
    background-color:#2a2b2b;
    border:0px;
    color:#fff;
}        
QPushButton:hover {
    background-color:#333;
}  
""")

    def Open(self):
        if self.openLeftBar == False:
            self.left.show()
            self.close_btn.show()
            self.mini_btn.show()
            self.close_bar.show()
            self.reload.show()
        else:
            self.close_btn.close()
            self.mini_btn.close()
            self.close_bar.close()
            self.reload.close()
            self.left.close()
        
        self.openLeftBar = not self.openLeftBar


    def Reload(self):
        self.web.reload()
        try:self.setStatusBar()
        except:pass

    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_F5:
            self.Reload()

        if event.key() == QtCore.Qt.Key_F1:
            self.Open()