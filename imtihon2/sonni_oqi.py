def  soni(son):
    dic ={1:"bir",2:"ikki",3:"uch",4:"tort",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"toqqiz"}
    dic1 ={1:"on",2:"yigirma",3:"ottiz",4:"qiqrq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"to'qson"}
    for i in range (1,10):
        if son//10==i:print(dic1[i],end="")
    for j in range (1,10):
        if son%10==j:print(dic[j],end="")
d=soni( int (input("sonni kiritng\n>>")))
