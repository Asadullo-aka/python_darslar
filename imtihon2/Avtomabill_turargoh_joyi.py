from random import randint
joy =int(input("Joylar sonni kiritng \n>>"))
joylar=list()
for i in range (joy):
    d=randint(0,1)
    joylar.append(d)
print("1.Joylar sonini korish\n2.Avtomabil joylashtirish\n3.Avtomoabil chiqarish")
while True:
    amal=int (input("Amalni tanlang\n>>"))
    if amal==1:
        print("Bosh joylar : {} ".format (joylar.count(0)))
        print("Band joylar : {} ".format(joylar.count(1)))
        print(joylar)
    elif amal==2:
        if joylar.count(0)==0:
            print("Afsus bosh joy yoq")
            print(joylar)
            continue
        elif joylar.count(0)>0:
            while True:
                ran_joy=randint(0, joy-1)
                if joylar[ran_joy]==0:
                    joylar[ran_joy]=1
                    print("Avtomobil {} -indexga joylashtirildi".format(ran_joy))
                    break
                else:
                    continue
    elif amal==3:
        while True:
            f=int(input("Qaysi indexdagi joyni baoshatasiz\n>>"))
            if f>=0 and f<joy:
                if joylar[f]==0:
                    print("Bu joy shundoq ham bo'sh")
                    continue
                else:
                    joylar[f]=0
                    break
            else:
                print("Bunday indexdagi joy yoq")
                continue
    elif amal>=4:
        break
         