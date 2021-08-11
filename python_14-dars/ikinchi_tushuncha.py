import sys 
from PyQt5 import QtWidgets
def kuysin():
    print("Ana Kuyding !!!!")
def application():
    app = QtWidgets.QApplication(sys.argv)
    oyna =QtWidgets.QMainWindow()
    yozuv =QtWidgets.QLabel(oyna)
    yozuv.setText("men Ishladim")
    yozuv.move(100,100)
    kirit=QtWidgets.QLineEdit(oyna)
    kirit.setGeometry(200, 100, 150, 40)
    btn=QtWidgets.QPushButton(oyna)
    btn.setGeometry(100, 200, 200, 50)
    btn.setText("Bosma kuyasan")
    btn.cliked.coonect(kuysin) 
    oyna.setGeometry(450, 250, 400, 400)
    oyna.setWindowTitle("Birnchi dasturim")
    sys.exit(app.exec())
application()    