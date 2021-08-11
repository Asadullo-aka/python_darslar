# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:11:29 2021

@author: Asadullo
"""

import colorama as c
print (c.Style.BRIGHT)
print (c.Back.YELLOW)
print (c.Fore.GREEN+'salom')
print (c.Style.RESET_ALL)
print ('salom')
#%%
def son2(son):
    return son+2
print(son2(10))
son3=lambda x: print (x+3)
son3(10)


sonlar= lambda x,y: x+y
print(sonlar(10,5))