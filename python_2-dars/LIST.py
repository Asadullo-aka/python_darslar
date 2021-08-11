# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:08:39 2021

@author: Asadullo
"""

#LIST
list1=[1,'hello',12.55,True]
print(type(list1))
print(list1[0])# 0 INDEKS
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[::-1])# TESKARI CHIQAR
print(list1[2:])# 2-INEKSDAN OXIRGACA CHIQAR 
print(list1[2:],list1[:2])# 

list2=[11,22,33,44,55,66,77,88,99,100]
print(list2[2:5])# 2- INDEKSDA 5 GACAH CIAQAR
print(list2[::2]) # INDEKSDA 2 TA  2 TA SAKRA
print(list2[1::2])
print(len(list2))