class Kompyuter:
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.narxi=b# 6 xona
        self.chastotas=c#2 xon
        self.ram=d
    def chiqar (self):
        print(f" nomi {self.nomi} \n>.narxi {self.narxi[:6]}\n>>chastotasi {self.chastotas} rami {self.ram[:2]} ")
comp=Kompyuter(input("noimi\n>>"),input("narxi\n>>"),input("chastotasi\n>>"),input("rami \n>>"))
comp.chiqar()
