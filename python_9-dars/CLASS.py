# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 11:19:10 2021

@author: Asadullo
"""

class student ():
    name ='Tomas'
    surname= 'Edison'
    age =45
st1= student () # st1 student sinfdagi obyekt
print(st1.surname,st1.name,st1.age)
ison=int ()# ison int sinfdagi obyekt
fson=float()# fson float sinfdagi obyekt
boolean=bool()# boolean bool sinfdagi obyekt
string=str()# strring str sinfdagi obyekt
#%% 
class animal ():
    name='Tiger'
    tipi='Yirqich'
    weigt=100
    def printanimal(self):
        print(self.name,self.weigt,self.tipi)
    def ozgartirish(self,a,b,c):
        self.name=a
        self.weigt=b
        self.tipi=c
t1=animal()
t1.printanimal()
t1.name='sigir'
t1.tipi='otxor'
t1.weigt=250
t1.printanimal()
t1.ozgartirish("ayiq",500,"yirtqich")
t1.printanimal()
