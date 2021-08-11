# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:16:15 2021

@author: Asadullo
"""

def fib(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)
def fib1(n):
    f1=1
    f2=1
    for i in range (3,n+1):
        f1,f2=f2,f1+f2
    print(n,"chi fibonachi soni =",f2)
son=int (input ("son: "))
print(son,"chi fibonachi soni=",fib(son))
fib1(int (input("n= ")))