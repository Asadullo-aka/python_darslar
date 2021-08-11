from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys 

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle(" birnchi dasturim ")
        self.setGeometry(300,300, 600, 400)
        
        self.new_text=QtWidgets.QLabel(self)
        
        self.main_text=QtWidgets.QLabel(self)
        #self.main_text.setText("Assalomu aleykum ")
        self.main_text.adjustSize()
        self.main_text.move(18, 10)
        #self.new_text.setText("Assalomu aleykum Asadullo Qodirov")
        # main_text.setGeometry(45, 100, 150, 45)
        #main_text.setFixedWidth(200)
        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("Toshpolatov")
        self.btn.move(100, 100)
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)
        
        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("Asadullo")
        self.btn.move(150, 150)
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)
        
        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("Qodirovich")
        self.btn.move(200, 200)
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)
    
    
   
    def add_label(self):
       self.new_text.setText("Assalomu alaykum ")
       self.new_text.move(100,100)
       self.new_text.adjustSize()
     
       
def application():
    app=QApplication(sys.argv)
    window=Window()
    
   
    
    
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()
