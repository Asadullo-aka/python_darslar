# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:50:16 2021

@author: Asadullo
"""

import random as r
a= r.randint(0,9)
b= r.randint(0,9)
c= r.randint(0,9)
print(a,b,c)
if a+b+c>7:
    print(a*100+b*10+c)

        

'''def teskari (soz):
    print(*soz,sep='\n')
    print(*soz[::-1], sep='\n')
teskari(input ('soz kiting'))
'''
'''
def soz (s):
    a= input('soz kiritng')
    if len (a)<s:
       pass
    else:
        print(a[-s:]+a[0:len(a)-s])
soz(int (input ('son_')))
    
'''