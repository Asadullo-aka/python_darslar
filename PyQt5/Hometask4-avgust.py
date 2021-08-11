import sys
from PyQt5.QtWidgets import *
import random as r
import time

class Task(QWidget):
    def __init__(self):
        super().__init__()
        self.begin()
    def begin(self):
        self.num = 0
        self.oyna = QWidget()
        self.oyna.setGeometry(350,350,300,300)
        
        self.lst = [1,2,3,4,5]
        r.shuffle(self.lst)
        
        self.oyna.setWindowTitle("Hometask")
        
        self.btn1 = QPushButton(self.oyna)
        self.btn1.setGeometry(130,80,30,20)
        self.btn1.setText("")
        self.btn1.clicked.connect(self.bos1)
      
        
        self.btn2 = QPushButton(self.oyna)
        self.btn2.setGeometry(70,100,30,20)
        self.btn2.setText("")
        self.btn2.clicked.connect(self.bos2)
        
        self.btn3 = QPushButton(self.oyna)
        self.btn3.setGeometry(130,100,30,20)
        self.btn3.setText("")
        self.btn3.clicked.connect(self.bos3)
        
        self.btn4 = QPushButton(self.oyna)
        self.btn4.setGeometry(190,100,30,20)
        self.btn4.setText("")
        self.btn4.clicked.connect(self.bos4)
        
        self.btn5 = QPushButton(self.oyna)
        self.btn5.setGeometry(130,120,30,20)
        self.btn5.setText("")
        self.btn5.clicked.connect(self.bos5)
        
        self.btn6 = QPushButton(self.oyna)
        self.btn6.setGeometry(122,150,30,20)
        self.btn6.setText("Restart")
        self.btn6.adjustSize()
        self.btn6.clicked.connect(self.begin)
        
        self.oyna.show()
        
    def bos1(self):
         self.btn1.setText(str(self.lst[0]))
         self.btn1.setGeometry(130,80,60,20)
         if self.btn1.text() == '1' and self.num == 0:
             self.btn1.close()
             self.num+=1
         elif self.btn1.text() == '2' and self.num == 1:
             self.btn1.close()
             self.num+=1
         elif self.btn1.text() == '3' and self.num == 2:
             self.btn1.close()
             self.num+=1
         elif self.btn1.text() == '4' and self.num == 3:
             self.btn1.close()
             self.num+=1
         elif self.btn1.text() == '5' and self.num == 4:
             self.btn1.close()
             self.num == 0
         else: 
             pass
         self.btn1.clicked.connect(self.bos11)
         
         
    def bos2(self):
        self.btn2.setText(str(self.lst[1]))
        self.btn2.setGeometry(70,100,60,20)
        if self.btn2.text() == '1' and self.num == 0:
             self.btn2.close()
             self.num+=1
        elif self.btn2.text() == '2' and self.num == 1:
             self.btn2.close()
             self.num+=1
        elif self.btn2.text() == '3' and self.num == 2:
             self.btn2.close()
             self.num+=1
        elif self.btn2.text() == '4' and self.num == 3:
             self.btn2.close()
             self.num+=1
        elif self.btn2.text() == '5' and self.num == 4:
             self.btn2.close()
             self.num == 0
        else: 
             pass
        self.btn2.clicked.connect(self.bos22)
    def bos3(self):
        self.btn3.setText(str(self.lst[2]))
        self.btn3.setGeometry(130,100,60,20)
        if self.btn3.text() == '1' and self.num == 0:
             self.btn3.close()
             self.num+=1
        elif self.btn3.text() == '2' and self.num == 1:
             self.btn3.close()
             self.num+=1
        elif self.btn3.text() == '3' and self.num == 2:
             self.btn3.close()
             self.num+=1
        elif self.btn3.text() == '4' and self.num == 3:
             self.btn3.close()
             self.num+=1
        elif self.btn3.text() == '5' and self.num == 4:
             self.btn3.close()
             self.num == 0
        else: 
             pass
        self.btn3.clicked.connect(self.bos33)
    def bos4(self):
        self.btn4.setText(str(self.lst[3]))
        self.btn4.setGeometry(190,100,60,20)
        if self.btn4.text() == '1' and self.num == 0:
             self.btn4.close()
             self.num+=1
        elif self.btn4.text() == '2' and self.num == 1:
             self.btn4.close()
             self.num+=1
        elif self.btn4.text() == '3' and self.num == 2:
             self.btn4.close()
             self.num+=1
        elif self.btn4.text() == '4' and self.num == 3:
             self.btn4.close()
             self.num+=1
        elif self.btn4.text() == '5' and self.num == 4:
             self.btn4.close()
             self.num == 0
        else: 
             pass
        self.btn4.clicked.connect(self.bos44)
    def bos5(self):
        self.btn5.setText(str(self.lst[4]))
        self.btn5.setGeometry(130,120,60,20)
        if self.btn5.text() == '1' and self.num == 0:
             self.btn5.close()
             self.num+=1
        elif self.btn5.text() == '2' and self.num == 1:
             self.btn5.close()
             self.num+=1
        elif self.btn5.text() == '3' and self.num == 2:
             self.btn5.close()
             self.num+=1
        elif self.btn5.text() == '4' and self.num == 3:
             self.btn5.close()
             self.num+=1
        elif self.btn5.text() == '5' and self.num == 4:
             self.btn5.close()
             self.num == 0
        else: 
             pass
        self.btn5.clicked.connect(self.bos55)
        
        
    def bos11(self):
        self.btn1.setGeometry(130,80,30,20)
        self.btn1.setText("")
        self.btn1.clicked.connect(self.bos1)
    def bos22(self):
        self.btn2.setGeometry(70,100,30,20)
        self.btn2.setText("")
        self.btn2.clicked.connect(self.bos2)
    def bos33(self):
        self.btn3.setGeometry(130,100,30,20)
        self.btn3.setText("")
        self.btn3.clicked.connect(self.bos3)
    def bos44(self):
        self.btn4.setGeometry(190,100,30,20)
        self.btn4.setText("")
        self.btn4.clicked.connect(self.bos4)
    def bos55(self):
        self.btn5.setGeometry(130,120,30,20)
        self.btn5.setText("")
        self.btn5.clicked.connect(self.bos5)
        
  
        
app = QApplication(sys.argv)
obj = Task()
sys.exit(app.exec_())

"""2) 5ta button ni ishlating. Ushbu buttonlar random sifatida 1dan 6gacha bo'lgan 
sonlar bilan raqamlangan, lekin raqamlari ko'rinmay turadi va siz ushbu raqamlarni
 ketma-ketligi topishingiz kerak, agar siz bosgan 1-button 1ga teng bo'lsa ushbu
 tugma yo'qolib qolsin va qolganlari ham shu tartibda yo'qolib borishi kerak"""