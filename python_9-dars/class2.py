# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 11:19:49 2021

@author: Asadullo
"""

class mashina ():
    def __delattr__(self):
        print("malumot o'chirildi")
    def __init__(self ,model,narx,otkuch):#class msthods(konsturcter)
        self .a=model
        self.b=narx
        self.c=otkuch
    def printmashina(self):
        print("""
     Mashina turi: {}
     Mashina naxi: {}
     Mashina kuchi: {}
                    """.format(self.a,self.b,self.c ))
m1=mashina('Mazda',100,2000)
m1.printmashina()
del(m1)
m1=mashina("lamborjini",100,3000)
