# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 05:16:23 2021

@author: Asadullo
"""

class komanda ():
    def __init__(self,a,b,c,d):
        self .nomi=a
        self.soni=b
        self.tren=c
        self.kapi=d
    def chiqar(self):
        print("""
    nomi {} :
    soni {} :
    treniri {}:
    kapitani {} :""".format (self.nomi,self.soni,self.tren,self.kapi))
t1=komanda("liverpol",11,"kloo","henderson")
t2=komanda("liv",112,"klrep","henderson")
t3=komanda("live",121,"klerwp","henderson")
t4=komanda("livel",151,"kloolp","henderson")
t5=komanda("lipol",119,"kloowr","henderson")
te=list()
te.append(te1.nomi)
te.append(te2.nomi)
te.append(te3.nomi)
te.append(te4.nomi)
te.append(te5.nomi)
te.sort()
for i in te:
    if i==te1.nomi:
        te1.chiqar()
    
    

