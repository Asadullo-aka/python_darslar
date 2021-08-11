# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:54:31 2021

@author: Asadullo
"""
'''
summa = input ('summani kiriting')

if summa.isdigit() and int (summa) > 0 and int (summa) < 1000000:
    print('tashakur')
else :
     print('xato')    
'''
alphabet = ['a','o','i','u',"o'",'e',"A","O","I","U","E","Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

letter= input ('harf kiritng: ')

if not(letter in alphabet):
     print('Boshqa til')
elif letter=='a' or letter=='o' or letter=='i' or letter=="o'" or letter=='u' or letter=='e':
    print('unli harf')
else :
     print('undosh harf')