import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.boshladik()
    def boshladik(self):
        self.oyna=QWidget()
        self.yozuv=QLabel(self.oyna)
        self.yozuv.move(100, 100)
        self.yozuv.setText("Hali  bosilmadi")
        
        self.kiritish=QLineEdit(self.oyna)
        self.kiritish.setGeometry(80, 70, 150, 30)
        
        self.btn=QPushButton(self.oyna)
        self.btn.move(100,120)
        self.btn.setText("Bosing")
        self.btn.clicked.connect(self.bos)
        
        self.oyna.setGeometry(350, 450, 300, 300)
        self.oyna.setWindowTitle("3-programma")
        self.oyna.show()
        
    def bos (self):
        self.yozuv.setText(self.st)
        self.yozuv.adjustSize()
        
app=QApplication(sys.argv)
ob=Window()
sys.exit(app.exec_())
        