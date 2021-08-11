import sys
from PyQt5.QtWidgets import *
def application():
    app=QApplication(sys.argv)
    oyna=QWidget()
    Ok=QPushButton("Okey")
    Cancel=QPushButton("Bekor qilish")
    h_box=QHBoxLayout(oyna)
    h_box.addStretch()
    h_box.addWidget(Ok)
    h_box.addStretch()
    h_box.addWidget(Cancel)
    h_box.addStretch()
    
    v_box=QVBoxLayout(oyna)
    v_box.addStretch()
    v_box.addWidget(Ok)
    v_box.addWidget(Cancel)
    v_box.addStretch()
    
    oyna.setWindowTitle("Ikkinchi dasturim")
    oyna.setGeometry(450, 100, 400, 400)
    oyna.show()
    sys.exit(app.exec_())
application()