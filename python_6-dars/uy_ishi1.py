# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:02:42 2021

@author: Asadullo
"""

'''
def teskari (s):
    if (s[::-1])==s:
        print('ajoyib soz')
    else: 
        print('ajoyib emas')
a= input ("soz kiritng_ ")
teskari(a)
'''
# =============================================================================
# 
# =============================================================================
#%%RECURSIVE FUNTION
def tub (n):
    list1=[]
    d=0
    for i in range(2,n**2):
        
        k=0
        for a in range (2,i//2+1):            
           if i%a==0:
                k+=1
        if k==0:
               # print(i,end=" ")
                list1.append(i)
                d=d+1
               # print(list1)
    print(n,"-ishchi ",list1[n-1])
tub (int (input ("son kiritng_")))           