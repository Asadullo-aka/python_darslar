import sys 
from PyQt5.QtWidgets import *
def application():
    app=QApplication(sys.argv)
    oyna=QWidget()
    OK=QPushButton("OKEY")
    cancel=QPushButton("Bekor qilish")
    h_box=QHBoxLayout(oyna)
    h_box.addStretch()
    h_box.addWidget(OK)
    h_box.addStretch()
    h_box.addWidget(cancel)
    h_box.addStretch()
     
    '''  v_box=QVBoxLayout(oyna)
    v_box.addStretch()
    v_box.addWidget(cancel)
    v_box.addStretch()'''
    
    oyna.setWindowTitle("ikkinchi dasturim")
    oyna.setGeometry(350, 400, 400, 400)
    oyna.show()
    sys.exit(app.exec_())
application()