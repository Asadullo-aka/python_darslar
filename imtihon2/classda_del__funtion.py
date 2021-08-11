class Meva :
    def __del__(self):
        print("malumot ochirildi")
    def __init__(self,a,b,c,d):
        self.nomi=a
        self.narxi=b
        self.navi=c
        self.davlati=d
    def info (self):
        print(f"> Nomi {self.nomi}\n> Narxi {self.narxi}\n> Navi {self.navi}\n> Davalti {self.davlati}")
olam=Meva ("olma",10000,"besh yulduz","O'zbekiston")
olam.info()
apelsin=Meva(input("nomi\n>"),int(input("naxi\n>")),input("navi\n>"),input("davlati\n>"))
apelsin.info()
del(olam)
