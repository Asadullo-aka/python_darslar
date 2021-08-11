# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:54:40 2021

@author: user
"""

class COMP():
    def __init__(self,model,narx,ram,proc):
        self.model=model
        self.narx=narx
        self.ram=ram
        self.proc=proc
    def display(self):
        print("---------")
        print("Modeli : ",self.model )
        print("Narxi : ",self.narx[0:6] )
        print("Operativ xotira : ",self.ram )
        print("Chastota : ",self.proc )
k1=COMP(input("Nomi: "),input("Narxi: "),int(input("Operativ xotirasi: ")),input("Chastotasi: "))
if k1.ram>3 and k1.ram<17:
    k1.display()
#%%
for i in range(1000,9999):
    z=((i//1000)%10)+((i//100)%10)+((i//10)%10)+(i%10)
    if i%z==0:
        print("---------")
        print(i)
    


