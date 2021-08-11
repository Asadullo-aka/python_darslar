# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:03:41 2021

@author: Asadullo
"""
'''
def tub(son):
    list1=[]
   # a=0
    for s in range(2,son**2):
        k=0
        for i in range(2,s//2+1):
            if s%i==0:
                k+=1
        if k==0:
            list1.append(s)
            #a+=1
    print(son,'-ishchi',list1[son-1])
tub (int (input('son kriting')))
'''
''' 
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
tub (int (input ("son kiritng_")))   ''' 
a=3
b=3
d=0
while a!=0:
    if d==True:
        break
    else:
        e=input('login')
        if e=='Asadullo':
            print('gap yoo')
            while b!=0:
                f=int (input ('parol'))
                if  f==12345:
                    print ('gap yooo tugadi :)')
                    d+=1
                    break
                else:
                    print('xato')
                    b-=1
        else:
            print('xato')
            a-=1
            
        
        
        


































              