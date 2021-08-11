

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from random import *

class Window (QWidget):
    def __init__(self):
        super().__init__()
        
        self.go()
    def go (self):
        self.bulish=QPushButton("/", self)
        self.bulish.setFont(QFont("Times",20))
        self.bulish.setGeometry(150, 250, 100, 40)
        self.m=QMessageBox()
        
        self.son1=QLineEdit(self)
        self.son1.setGeometry(100, 100, 200, 60)
        self.son1.setFont(QFont("Times",15))
        self.son2=QLineEdit(self)
        self.son2.setGeometry(100, 180, 200, 60)
        self.son2.setFont(QFont("Times",20))
        
        self.yozuv=QLabel("Natija: ",self)
        self.yozuv.move(350,150)
        self.yozuv.setFont(QFont("Times",20))
        
        self.bulish.clicked.connect(self.devide)
    def devide(self):
        a=int(self.son1.text())
        b=int(self.son2.text())
        if b==0:
            error=QMessageBox(self)
            error.setWindowTitle("Xatolik")
            error.setText("Nolga bolib bolmaydi")
            error.setIcon(QMessageBox.Critical)
            error.setStandardButtons(QMessageBox.Cancel|QMessageBox.Reset|QMessageBox.Ok)
            error.setDetailedText("KO'P NARSA YOZILGAN")
            error.exec_()
        else:
            self.yozuv.setText(str(a)+"/"+str(b)+"="+str(a/b))
            self.yozuv.adjustSize()
        
            
            
app=QApplication(sys.argv)
ob=Window()
ob.setGeometry(350, 250, 600, 500)
ob.setWindowTitle("QMessageBox")
ob.show()
sys.exit(app.exec_())