t=0
i=3
d=3
while i!=0:
    if t==True:
        break
    a=input ('loginni kititng_')
    if a=="Asadullo":
        print("login togri")
        while d!=0:
           b=int (input ('parolni kiritng_'))
           if b==12345:
            print('xush kelibsiz')
             
            if d>0:
                t=t+1
                break 
           else :
            d-=1
            print('xato!!!!!!') 
    else :
        i-=1
        print("xatoo!!!!")
        