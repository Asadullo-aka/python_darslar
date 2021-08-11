def dic(son):
    s={}
    b=[]
    for i in range(son):
        b.append(int(input('sonni kiritng__')))
        b.sort(reverse=True)
    for i in range(son):
        s[i]=b[i]
    print(s)
a=(int(input('nechta son kiritmoqcisiz__')))
dic(a)