import sys
from PyQt5 import QtWidgets
def application():
    
    app=QtWidgets.QApplication(sys.argv)
    oyna=QtWidgets.QMainWindow()
    #oyna=QtWidgets.QWidget()
    yozuv=QtWidgets.QLabel(oyna)
    yozuv.setText("Assalomu aleykum Asadullo")#ichkariga 
    yozuv.adjustSize()# sozlarni toliq chiqarish
    yozuv.move(5,5)# yozuvni qayerga joylash
    oyna.setGeometry(450, 250, 400, 400)
    oyna.setWindowTitle("Birnchi dasturim")# oynani nomi
    #oyna.setFixedSize(300,300)
    oyna.show()# korsatish
    sys.exit(app.exec_())
application()    
    