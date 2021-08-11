'''print(int(128**(1/2)))
print("Asadullo\n>>>"*3)'''
#listni ischida qaysi eng kop takrorlanganini aniqlash
l=list()
son=int (input("list ichiga nechta son kiritmoqchiligingizni yozing\n>>"))
for i in range (0,son):
    l.append(int(input(f"{i+1}-son\n>>")))
print("______________________________________")
print(l)
go=0
x=set(l)
print(x)
for i in x:
    b=l.count(i)
    print(f"{i} soni {b}ta")
    z=0
    for j in range(0,b):
        z+=1
    if z>go:
        go=z
        d=i
print(f"{d}soni eng kop takrorlangan {go} ta")
