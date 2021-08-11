
import sys # sistemani ishlatish
from PyQt5.QtWidgets import *# koutbaxona chaqiryabmiz
from PyQt5.QtGui import *# yozuvlarni shiriflarni fondii ozgaratiradi 

class Kalkulayator(QWidget):# bu  bzga kutaubxoni elemenlarini vorislik ooslish
    def __init__(self):# malumot kiritamiz 
        super().__init__()# super orqali qwiijetdagi elemenlarni ozlashtirib claasssda ishlatyabmiz
        self.son=list()
        self.Amal()# uzimuz amal qoshyabmiz 
    def Amal(self):# 
        self.setStyleSheet("background-color: ;")
        self.ekran=QLineEdit(self)
        self.ekran.setGeometry(15, 15, 260, 30)
        self.setFixedSize(300,280)
        self.ekran.setFont(QFont("Times",15))
        #self.ekran.setPlaceholderText("")
        self.ekran.setStyleSheet("background-color : #e22a00; : 2px solid black; border-radius : 10px;")
        self.ekran.setStyleSheet("background-color : #e68c00; : 2px solid black; border-radius : 10px;")
        
        
        
        self.push1=QPushButton(self)
        self.push1.setGeometry(15, 60, 40, 40)
        self.push1.setFont(QFont("Areal Black",20))
        self.push1.setText("1")
        self.push1.clicked.connect(self.f1)
        #self.push1.setStyleSheet("background-color : #e68a00;border : 2px solid black; border-radius : 10px;")
       
        
        self.push2=QPushButton(self)
        self.push2.setGeometry(70, 60, 40, 40)
        self.push2.setFont(QFont("Areal Black",20))
        self.push2.setText("2")
        self.push2.clicked.connect(self.f2)
        
        self.push3=QPushButton(self)
        self.push3.setGeometry(125, 60, 40, 40)
        self.push3.setFont(QFont("Areal Black",20))
        self.push3.setText("3")
        self.push3.clicked.connect(self.f3)
        
        self.push4=QPushButton(self)
        self.push4.setGeometry(15, 115, 40, 40)
        self.push4.setFont(QFont("Areal Black",20))
        self.push4.setText("4")
        self.push4.clicked.connect(self.f4)
        
        self.push5=QPushButton(self)
        self.push5.setGeometry(70, 115, 40, 40)
        self.push5.setFont(QFont("Areal Black",20))
        self.push5.setText("5")
        self.push5.clicked.connect(self.f5)
        
        self.push6=QPushButton(self)
        self.push6.setGeometry(125, 115, 40, 40)
        self.push6.setFont(QFont("Areal Black",20))
        self.push6.setText("6")
        self.push6.clicked.connect(self.f6)
        
        self.push7=QPushButton(self)
        self.push7.setGeometry(15, 170, 40, 40)
        self.push7.setFont(QFont("Areal Black",20))
        self.push7.setText("7")
        self.push7.clicked.connect(self.f7)
        
        self.push8=QPushButton(self)
        self.push8.setGeometry(70, 170, 40, 40)
        self.push8.setFont(QFont("Areal Black",20))
        self.push8.setText("8")
        self.push8.clicked.connect(self.f8)
        
        self.push9=QPushButton(self)
        self.push9.setGeometry(125, 170, 40, 40)
        self.push9.setFont(QFont("Areal Black",20))
        self.push9.setText("9")
        self.push9.clicked.connect(self.f9)
        
        self.pushf=QPushButton(self)
        self.pushf.setGeometry(15, 225, 40, 40)
        self.pushf.setFont(QFont("Areal Black",20))
        self.pushf.setText("%")
        self.pushf.clicked.connect(self.ff)
        
        self.push0=QPushButton(self)
        self.push0.setGeometry(70, 225, 40, 40)
        self.push0.setFont(QFont("Areal Black",20))
        self.push0.setText("0")
        self.push0.clicked.connect(self.f0)
        
        self.pushn=QPushButton(self)
        self.pushn.setGeometry(125, 225, 40, 40)
        self.pushn.setFont(QFont("Areal Black",20))
        self.pushn.setText(".")
        self.pushn.clicked.connect(self.fn)
        
        self.pushp=QPushButton(self)
        self.pushp.setGeometry(180, 60, 40, 40)
        self.pushp.setFont(QFont("Areal Black",20))
        self.pushp.setText("+")
        self.pushp.clicked.connect(self.fp)
    
        self.pushm=QPushButton(self)
        self.pushm.setGeometry(180, 115, 40, 40)
        self.pushm.setFont(QFont("Areal Black",20))
        self.pushm.setText("-")
        self.pushm.clicked.connect(self.fm)
        
        self.pushk=QPushButton(self)
        self.pushk.setGeometry(180, 170, 40, 40)
        self.pushk.setFont(QFont("Areal Black",20))
        self.pushk.setText("*")
        self.pushk.clicked.connect(self.fk)
    
        self.pushb=QPushButton(self)
        self.pushb.setGeometry(180, 225, 40, 40)
        self.pushb.setFont(QFont("Areal Black",20))
        self.pushb.setText("/")
        self.pushb.clicked.connect(self.fb)
    
        self.pushc=QPushButton(self)
        self.pushc.setGeometry(235, 60, 40, 40)
        self.pushc.setFont(QFont("Areal Black",20))
        self.pushc.setText("c")
        self.pushc.clicked.connect(self.fc)
        
        self.pushx=QPushButton(self)
        self.pushx.setGeometry(235, 115, 40, 40)
        self.pushx.setFont(QFont("Areal Black",20))
        self.pushx.setText("x")
        self.pushx.clicked.connect(self.fx)
        
        self.pusht=QPushButton(self)
        self.pusht.setGeometry(235, 170, 40, 95)
        self.pusht.setFont(QFont("Areal Black",20))
        self.pusht.setText("=")
        self.show()
        self.pusht.clicked.connect(self.ft)
        
    def f1(self):
        self.ekran.setText(self.ekran.text()+"1")
        self.son.append("")
    def f2(self):
        self.ekran.setText(self.ekran.text()+"2")
        self.son.append("")
    def f3(self):
        self.ekran.setText(self.ekran.text()+"3")
        self.son.append("")
    def f4(self):
        self.ekran.setText(self.ekran.text()+"4")
        self.son.append("")
    def f5(self):
        self.ekran.setText(self.ekran.text()+"5")
        self.son.append("")
    def f6(self):
        self.ekran.setText(self.ekran.text()+"6")
        self.son.append("")
    def f7(self):
        self.ekran.setText(self.ekran.text()+"7")
        self.son.append("")
    def f8(self):
        self.ekran.setText(self.ekran.text()+"8")
        self.son.append("")
    def f9(self):
        self.ekran.setText(self.ekran.text()+"9")
        self.son.append("")
    def f0(self):
        self.ekran.setText(self.ekran.text()+"0")
        self.son.append("")
    def ff(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :  
            self.ekran.setText(self.ekran.text()+"%")
            self.son.append("%")
    def fn(self):
         if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :
             self.ekran.setText(self.ekran.text()+".")
             self.son.append(".")
    def fp(self):
         if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :
             self.ekran.setText(self.ekran.text()+"+")
             self.son.append("+")
    def fm(self):
         if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :
             self.ekran.setText(self.ekran.text()+"-")
             self.son.append("-")
    def fk(self):
         if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :
             self.ekran.setText(self.ekran.text()+"*")
             self.son.append("*")
    def fb(self):
         if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="*" and self.son[-1]!="-" and self.son[-1]!="/" and self.son[-1]!="." :
             self.ekran.setText(self.ekran.text()+"/")
             self.son.append("/")
    def fc(self):
        self.ekran.setText("")
    def fx(self):
        kam=self.ekran.text()
        self.ekran.setText(self.ekran.text()+"x")
        self.ekran.setText(kam[:len(kam)-1])
    def ft(self):
        natija=eval(self.ekran.text())
        self.ekran.setText(str(natija))
  
    
        
        
app=QApplication(sys.argv)
ob=Kalkulayator()
ob.resize(300,280)
ob.setWindowTitle("Kalkulyator")
ob.show() 
sys.exit(app.exec_())# ikks burchakda gi