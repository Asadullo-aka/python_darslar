# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:02:07 2021

@author: Asadullo
"""

def SonniOqi(son):
    dic1={1:"bir",2:"ikki",3:"uch",4:"to'rt",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
    dic2={1:"O'n",2:"Yigirma",3:"O'ttiz",4:"Qirq",5:"Ellik",6:"Oltmish",7:"Yetmish",8:"Sakson",9:"To'qson"}
    for f in range(1,10):
        if son//10==f:print(dic2[f],end=" ")
    for j in range(1,10):    
        if son%10==j:print(dic1[j])
d=int(input("Sonni kiriting: "))
SonniOqi(d)