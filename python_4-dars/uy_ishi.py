# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:19:20 2021

@author: Asadullo
"""
print ('quydagi belgilardda kalkulyator ishledi :|| + || * || - || / || // || ** ||')
a=int (input('a_'))
c=input("belgi")
b=int (input('b_'))
if c=='+':
    print("javob_",a+b)
elif c=='*':
    print("javob_",a*b)
elif c=='-':
    print("javob_",a-b)
elif c=='/':
    print("javob_",a/b)
elif c=='//':
    print("javob_",a//b)
elif c=='**':
    print("javob_",a**b)
elif c=="%":
    print("javob_",a%b)
else :
    print("xatoo!!!!!")