import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Oyna(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.start()
    def start (self):
        self.fam=QLineEdit(self)
        self.fam.move(100, 120)
        self.ism=QLineEdit(self)
        self.ism.move(100, 180)
        self.sana=QLineEdit(self)
        self.sana.move(100, 240)
        
        yozuv1=QLabel("Familiya",self)
        yozuv1.move(10,122)
        yozuv2=Qlabel("Ism",self)
        yozuv2.move(10,182)
        yozuv3=QLabel("Sana",self)
        yozuv3.move(10,242)
        
        run=QPushButton("Bajarilsin", self)
        run.setGeometry(150, 280, 80, 40)
        self.yozuv=QLabel(self)
        self.yozuv.move(350, 120)
        
        run.clicked.connect(self.push)
    def push(self):
        self.yozuv.setText(self.fam.text()+"\n\n\n\n"+self.ism.text()+"\n\n\n\n"+self.sana.text())
        self.yozuv.adjustSize()
dizayn=QApplication(sys.argv)
ob=Oyna()
ob.setGeometry(300,300,600,400)
ob.setWindowTitle("Uyga vazifa 2")
ob.show()
sys.exit(dizayn.exec_())        