'''class Komanda:
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.coach=b
        self.capitan=c
        self.soni =d
    def printf(self):
        print(f">>Komanda nomi {self.nomi} \n>>Komanda Murabiyi {self.coach} \n>>Komanda capitani {self.capitan} \n>> Komanda soni {self.soni}")
m=Komanda("baesa","ronaldo","linonel",11)
if m.soni<=11:
    m.printf()'''
class Komanda :
    def __init__ (self):
        for i in range (5):
            print(f"{i+1}-komanda")
            self.name[i]=input("komanda nomini kiriting\n>>")
            self.coach[i]=input("komnda murabiyini kiriing\n>>")
            self.capitan[i]=input("komanda Capitanini kriting\n>>")
            self.coni[i]=input("komanda soni kriting")
    def info (self):
        for i in range (5):
            print(f">>komnda nomi {self.name[i]} \n Komanda murabiyi {self.coach[i]} \n>>Komanda capitani {self.capitani[i]} Komanda soni {self.soni[i]}")
f=Komanda()
f.info()