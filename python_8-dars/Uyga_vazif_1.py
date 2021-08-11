# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:28:29 2021

@author: Asadullo
"""
import random as r
import time
lis=[a for a in range (1,11)]
b=int (input ('limitni belgilang 10 tadan oshmasin'))
if b > 10:
    print('10 soniydan kegin qaytadan urunib koring')
    print('xatoo')
    time.sleep(3)
else:
   
    while b!=0:
        #print(lis)
        r.shuffle(lis)
        #print(lis)
        son=r.choice(lis)
        #print(son)
        a=int (input('1 dan 11 gacha bolgan sonlar orasidan bolgan son kiritng'))
        if son==a:
           time.sleep(2)
           print('   {}      win!!!!!'.format(son))
           break
        elif a > 11:
           time.sleep(2)
           print(' xatoo!!!!! limit soni bittaga kamaydi ')
           b-=1
           time.sleep(2)
           print(' xato!!!!!limit soni bittaga kamaydi  ')
           b-=1
           time.sleep(2)
           print(' Bum!!!!!limit soni bittaga kamaydi  ')
           b-=1
        elif son > a:
           print('{} kottaroq son kititing brat'.format(son))
           b-=1
           print('limtlar soni {} ta qoldi'.format(b))
        elif son < a:
           print('{} kichikraq son kititing brat'.format(son))
           b-=1
           print('limtlar soni {} ta qoldi'.format(b))