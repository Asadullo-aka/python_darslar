# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:46:45 2021

@author: Asadullo
"""

def a (s):
    d= input ('son kiritng_')
    if len (d)<=s:
        pass
    else:
        print(d[s:]+d[:s])
a(int( input ('son_')))