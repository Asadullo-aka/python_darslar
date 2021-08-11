import  sys 
from PyQt5  import QtWidgets
from PyQt5.QtGui import QFont


class Oyna (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.start ()
    def start (self):
        fam="Qodirov"
        ism="Asadullo"
        shar="Qodirovich"
        yozuv1=QtWidgets.QLabel(fam,self)
        #yozuv1.move(len(fam)*15, 120)
        yozuv1.setFont(QFont("Times",20))
        yozuv2=QtWidgets.QLabel(ism,self)
        #yozuv2.move(len(fam)+15+len(ism)*15, 120)
        yozuv1.setFont(QFont("Times",20))
        yozuv3=QtWidgets.QLabel(shar,self)
        #yozuv3.move(len(fam)*15+len(shar)*10, 120)
        yozuv3.setFont(QFont("Times",20))
        h_box=QtWidgets.QHBoxLayout(self)
        h_box.addWidget(yozuv1)
        h_box.addWidget(yozuv2)
        h_box.addWidget(yozuv3)
        h_box.addStretch()
app=QtWidgets.QApplication(sys.argv)
ob=Oyna()
ob.setGeometry(300, 300, 600, 400)
ob.setWindowTitle("Uyga vazifa")
ob.show()
sys.exit(app.exec_())
                     
        
        