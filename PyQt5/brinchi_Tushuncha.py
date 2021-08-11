import sys
from PyQt5 import QtWidgets

def application():
    app =QtWidgets.QApplication(sys.argv)
    oyna=QtWidgets.QMainWindow()
    
    oyna =QtWidgets.QWidget()
    
    yozuv=QtWidgets.QLabel(oyna)
    yozuv.setText("Assalomu Aleykum")
    yozuv.move(50,50)
    
    yozuv=QtWidgets.QLabel(oyna)
    yozuv.setText("Valeykum Assalom")
    yozuv.move(50,100)
    
    yozuv=QtWidgets.QLabel(oyna)
    yozuv.setText("Hello World")
    yozuv.move(50,150)
    
    oyna.setGeometry(450, 250, 400, 400)
    oyna.setWindowTitle("Birnchui Dasturim")
    
    oyna.show()
    sys.exit(app.exec_())
application()