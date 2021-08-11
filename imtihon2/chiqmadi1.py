#Mojiza son 
l=list()
son=int (input("listga nechta son kiritmoqchisiz \n>>"))
for i in range (0,son):
    l.append(int(input(f"{i+}-son\n>>")))
num=int(input("Boluvchi sonni kiritng\n>."))
a=sum(l)
print(f"list elementlari {l}\n")
print(f"list elementlari yigindisi {a}\n")
if a%num==0:
    print("Mojiza")
else:
    print("Mojiza emas")
    
