# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:50:12 2021

@author: Asadullo
"""

from PyQt5 import QtWidgets
import sys
class Dastur (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()#QtWidgets.QWidget vorislik olyabmiz
        
        self.window()# oynain yarat yabmiz
    def window(self):#windov degan metodni yaaaratdik
        self.resize(400, 400)# razmeri oynani
        self.setWindowTitle("Hello")# oynai nomi
        self.button=QtWidgets.QPushButton("Next")# next degan bosiladigan tugma yaratdik
        self.button.setEnabled(False)# next degan tugmani bosib bolmaydigaon qildik
        self.radiobutton=QtWidgets.QRadioButton("Tanlang ") # tanlag degan tugmacha yaratdik
        
        hbox=QtWidgets.QVBoxLayout()
        hbox.addWidget(self.radiobutton)
        hbox.addWidget(self.button)
        
        self.radiobutton.clicked.connect(self.och)
        self.setLayout(hbox)
        self.show()# show bizga korsatadi oynani ekranga chiqaradi 
    def och(self):
        self.button.setEnabled(True)
        
app=QtWidgets.QApplication(sys.argv)# app digan sozni hohlagan nomimizga ozgartirsak boladi
oyna=Dastur()
sys.exit(app.exec_())