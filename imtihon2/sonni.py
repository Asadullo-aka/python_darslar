def SonniOqi(son):
    dic1={1:"bir",2:"ikki",3:"uch",4:"to'rt",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
    dic2={1:"O'n",2:"Yigirma",3:"O'ttiz",4:"Qirq",5:"Ellik",6:"Oltmish",7:"Yetmish",8:"Sakson",9:"To'qson"}
    dic3={1:"Bir yuzi",2:"ikki yuzi",3:"uch yuzi",4:"to'rt yuzi",5:"besh yuzi",6:"olti yuzi",7:"Yetti yuzi",8:"skkiz yuzi",9:"to'qqiz yuzi"}
    dic4={1:"Bir ming",2:"ikki ming",3:"uch ming",4:"to'rt ming",5:"besh ming",6:"olti ming",7:"Yetti ming",8:"skkiz ming",9:"to'qqiz ming"}
    for r in range(1,10):
        if son//100000==r:
            print(dic3[r],end=" ")
    for t in range(1,10):
        if (son//10000)%10==t:
            print(dic2[t],end=" ")
    for o in range(1,10):
        if (son//1000)%10==o:
            print(dic4[o],end=" ")
    for i in range(1,10):
        if (son//100)%10==i:
            print(dic3[i],end=" ")
    for j in range(1,10):    
        if (son//10)%10==j:
            print(dic2[j],end=' ')
    for k in range(1,10):    
        if son%10==k:
            print(dic1[k])
d=int(input("Sonni kiriting: "))
SonniOqi(d)