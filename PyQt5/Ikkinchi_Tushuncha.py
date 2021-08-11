import sys
from PyQt5 import QtWidgets
def kuysin():
    print("ANA KUYDING!!!!")
def application():
    app=QtWidgets.QApplication(sys.argv)
    oyna=QtWidgets.QMainWindow()
    
    yozuv=QtWidgets.QLabel(oyna)
    yozuv.setText("Men Ishladim")
    yozuv.move(100, 100)
    
    kirit=QtWidgets.QLineEdit(oyna)#oyna ga soz kiritnf=sh
    kirit.setGeometry(200, 100, 150, 40)
    
    btn=QtWidgets.QPushButton(oyna)# tugma yaratish bosiladigan
    btn.setGeometry(100, 200, 200, 50)
    btn.setText("Bosma kuyasan")
    btn.clicked.connect(kuysin)
    
    oyna.setGeometry(450, 250, 400, 400)#razmeri
    oyna.setWindowTitle("Birnchi dasturim")# oyna nomi 
    oyna.show()
    sys.exit(app.exec_())
application()