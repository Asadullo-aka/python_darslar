

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Kalkulyator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.son=list()
        self.Amal()
    def Amal(self):
        
        self.ekran=QLineEdit(self)
        self.ekran.setGeometry(15,15,220,30)
        self.ekran.setFont(QFont("Times",15))
        
        
      
        self.pushx=QPushButton(self)
        self.pushx.setGeometry(250,15,30,30)
        self.pushx.setText("x")
        self.pushx.clicked.connect(self.fx)
        
        
        self.push1=QPushButton(self)
        self.push1.setGeometry(15,60,40,40)
        self.push1.setText("1")
        self.push1.clicked.connect(self.f1)
        
        self.push2=QPushButton(self)
        self.push2.setGeometry(70,60,40,40)
        self.push2.setText("2")
        self.push2.clicked.connect(self.f2)
        
        self.push3=QPushButton(self)
        self.push3.setGeometry(125,60,40,40)
        self.push3.setText("3")
        self.push3.clicked.connect(self.f3)
        
        self.push4=QPushButton(self)
        self.push4.setGeometry(15,115,40,40)
        self.push4.setText("4")
        self.push4.clicked.connect(self.f4)
        
        self.push5=QPushButton(self)
        self.push5.setGeometry(70,115,40,40)
        self.push5.setText("5")
        self.push5.clicked.connect(self.f5)
        
        self.push6=QPushButton(self)
        self.push6.setGeometry(125,115,40,40)
        self.push6.setText("6")
        self.push6.clicked.connect(self.f6)
        
        self.push7=QPushButton(self)
        self.push7.setGeometry(15,170,40,40)
        self.push7.setText("7")
        self.push7.clicked.connect(self.f7)
        
        self.push8=QPushButton(self)
        self.push8.setGeometry(70,170,40,40)
        self.push8.setText("8")
        self.push8.clicked.connect(self.f8)
        
        self.push9=QPushButton(self)
        self.push9.setGeometry(125,170,40,40)
        self.push9.setText("9")
        self.push9.clicked.connect(self.f9)
        
        self.pushf=QPushButton(self)
        self.pushf.setGeometry(15,225,40,40)
        self.pushf.setText("%")
        self.pushf.clicked.connect(self.ff)
        
        self.push0=QPushButton(self)
        self.push0.setGeometry(70,225,40,40)
        self.push0.setText("0")
        self.push0.clicked.connect(self.f0)        
        
        self.pushn=QPushButton(self)
        self.pushn.setGeometry(125,225,40,40)
        self.pushn.setText(".")
        self.pushn.clicked.connect(self.fn)
        
        
        self.pushk=QPushButton(self)
        self.pushk.setGeometry(180,60,40,40)
        self.pushk.setText("*")
        self.pushk.clicked.connect(self.fk)
        
        
        self.pushc=QPushButton(self)
        self.pushc.setGeometry(235,60,40,40)
        self.pushc.setText("c")
        self.pushc.clicked.connect(self.fc)
        
        
        self.pushb=QPushButton(self)
        self.pushb.setGeometry(180,115,40,40)
        self.pushb.setText("/")
        self.pushb.clicked.connect(self.fb)
        
        
        self.pushd=QPushButton(self)
        self.pushd.setGeometry(235,115,40,40)
        self.pushd.setText("**")
        self.pushd.clicked.connect(self.fd)
        
        
        self.pushp=QPushButton(self)
        self.pushp.setGeometry(180,170,40,40)
        self.pushp.setText("+")
        self.pushp.clicked.connect(self.fp)
        
        
        self.pushm=QPushButton(self)
        self.pushm.setGeometry(180,225,40,40)
        self.pushm.setText("-")
        self.pushm.clicked.connect(self.fm)
        
        self.pusht=QPushButton(self)
        self.pusht.setGeometry(235,170,40,95)
        self.pusht.setText("=")
        self.pusht.clicked.connect(self.ft)
        
        self.show()
        
    def f1(self):
        self.ekran.setText(self.ekran.text()+"1")
        self.son.append("1")
    def f2(self):
        self.ekran.setText(self.ekran.text()+"2")
        self.son.append("2")
    def f3(self):
        self.ekran.setText(self.ekran.text()+"3")
        self.son.append("3")
    def f4(self):
        self.ekran.setText(self.ekran.text()+"4")
        self.son.append("4")
    def f5(self):
        self.ekran.setText(self.ekran.text()+"5")
        self.son.append("5")
    def f6(self):
        self.ekran.setText(self.ekran.text()+"6")
        self.son.append("6")
    def f7(self):
        self.ekran.setText(self.ekran.text()+"7")
        self.son.append("7")
    def f8(self):
        self.ekran.setText(self.ekran.text()+"8")
        self.son.append("8")
    def f9(self):
        self.ekran.setText(self.ekran.text()+"9")
        self.son.append("9")
    def f0(self):
        self.ekran.setText(self.ekran.text()+"0")
        self.son.append("0")
    def ff(self):
        if self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-": 
            self.ekran.setText(self.ekran.text()+"%")
            self.son.append("%")
    def fn(self):
        if self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+".")
            self.son.append(".")
    def fk(self):
        if  self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+"*")
            self.son.append("*")
    def fc(self):
        self.ekran.setText("")
        #self.son.append("%")
    def fb(self):
        if  self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+"/")
            self.son.append("/")
    def fd(self):
        if  self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+"**")
            self.son.append("**")
    def fp(self):
        if  self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+"+")
            self.son.append("+")
    def fm(self):
        if  self.son[-1]!="%" and self.son[-1]!="." and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!="**" and self.son[-1]!="+" and self.son[-1]!="-":
            self.ekran.setText(self.ekran.text()+"-")
            self.son.append("-")
    def fx(self):
         kam=self.ekran.text()
         self.ekran.setText(self.ekran.text()+"x")
         self.ekran.setText(kam[:len(kam)-1])
    def ft(self):
        natija=eval(self.ekran.text())
        self.ekran.setText(str(natija))

app=QApplication(sys.argv)
ob=Kalkulyator()
ob.resize(300, 280)
ob.setWindowTitle("Kakulyator")
ob.show()
sys.exit(app.exec_())