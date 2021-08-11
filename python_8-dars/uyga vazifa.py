# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:14:03 2021

@author: Asadullo
"""
import random as r
def lot ():
    shans=5
    taxmin=r.randint(1,41)
    while shans !=0:
          son=int(input ('son: '))
          if son==taxmin:
              print('gap yoo ')
              break
          elif son<taxmin:
              print('sonni oshiring:')
              shans-=1
              print('sizda {} ta shans qoldi'.format(shans))
          elif son>taxmin:
              print('sonni paslating:')
              shans-=1
              print('sizda {} ta shans qoldi'.format(shans))
          if shans==0:
              print('siz qaytatan omadingizni sinab koring')
              break
lot()