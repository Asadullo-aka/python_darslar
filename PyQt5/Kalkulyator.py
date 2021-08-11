# Vazifa_1
import sys
from PyQt5.QtWidgets import *

class Hisob(QWidget):
    def __init__(self):
        super().__init__()
        self.hisobla()
    def hisobla(self):
        self.oyna = QWidget()
        self.oyna.setGeometry(300, 300, 300, 300)
        
        self.oyna.setWindowTitle("Kalkulyator")
        
        self.a = QLineEdit(self.oyna)
        self.a.move(100,100)
    
        
        self.b = QLineEdit(self.oyna)
        self.b.move(100,130)
    
       
        self.natija = QLabel(self.oyna)
       
        self.button = QPushButton(self.oyna)
        self.button.move(100,170)
        self.button.setText("+")
        self.button.clicked.connect(self.bos)
        
        self.button1 = QPushButton(self.oyna)
        self.button1.move(100,190)
        self.button1.setText("-")
        self.button1.clicked.connect(self.bos1)
        
        self.button2 = QPushButton(self.oyna)
        self.button2.move(100,210)
        self.button2.setText("*")
        self.button2.clicked.connect(self.bos2)
        
        self.button3 = QPushButton(self.oyna)
        self.button3.move(200,190)
        self.button3.setText("//")
        self.button3.clicked.connect(self.bos3)
        
        self.button4 = QPushButton(self.oyna)
        self.button4.move(200,170)
        self.button4.setText("%")
        self.button4.clicked.connect(self.bos4)
        
        self.button5 = QPushButton(self.oyna)
        self.button5.move(200,210)
        self.button5.setText("Daraja")
        self.button5.clicked.connect(self.bos5)
        
        self.oyna.show()
        
    def bos(self):
        self.c =  int(self.a.text()) + int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "+" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
     
         
    def bos1(self):
        self.c =  int(self.a.text()) - int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "-" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
         
    def bos2(self):
        self.c =  int(self.a.text()) * int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "*" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
         
    def bos3(self):
        self.c =  int(self.a.text()) // int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "//" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
        
         
    def bos4(self):
        self.c =  int(self.a.text()) % int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "%" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
        
         
    def bos5(self):
        self.c =  int(self.a.text()) ** int(self.b.text())
      
        self.natija.setText("Result: " + self.a.text() + "**" + self.b.text() + "= " +str(self.c))
        self.natija.move(110,70)
        self.natija.adjustSize()
        
app = QApplication(sys.argv)
a = Hisob()
sys.exit(app.exec_())