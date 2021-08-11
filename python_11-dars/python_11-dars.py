# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 09:24:02 2021

@author: Asadullo
"""
def ekub (a,b):
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
    if a==b:
        return a
    return ekub(a,b)
son=int(input ('son : '))
son1=int (input ('son1 : '))
print("ekub ({},{})={}".format(son,son1,ekub(son, son1)))


