# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:03:30 2021

@author: Asadullo
"""

[Forwarded from Mening fikrlarim]
from random import randint
joy=int(input("Joylar sonini kiriting: "))

joylar=[]

for f in range(joy):
    df=randint(0, 1)
    joylar.append(df)
    

print("""
      1.Joylar sonini ko'rish
      2.Avtomobil joylashtirish
      3.Avtomobil chiqarish
      """)
while True:
    amal=int(input("Amalni tanlang: "))
    
    if amal==1:
        print("Bo'sh joylar:{}".format(joylar.count(0)))
        print("Band joylar:{}".format(joylar.count(1)))
        print(joylar)
   
    elif amal==2:
        if joylar.count(0)==0:
            print("Afsus bo'sh joy yo'q")
            print(joylar)
            continue
        
        elif joylar.count(0)>0:
                while True:
                    ran_joy=randint(0,joy-1)            
                    if joylar[ran_joy]==0:
                        joylar[ran_joy]=1
                        print("Avtomobil {}-indexga joylashtirildi".format(ran_joy))
                        break
                    else:
                        continue

    elif amal==3:
        while True:
            f=int(input("Qaysi indexdigi joyni bo'shatasiz:"))
            if f>=0 and f<joy:
                if joylar[f]==0:
                    print("Bu joy shundoq ham bo'sh")
                    continue
                else:
                    joylar[f]=0
                    break
            else:
                print("Bunday indexdagi joy yo'q")
                continue
            
    elif amal==4:
        break