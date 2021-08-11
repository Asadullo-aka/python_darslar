class Soldat():
    def __init__(self,a,b,c,d):
        self.jinsi=a
        self.yoshi=b
        self.boyii=c
        self.vazni=d
    def printer(self):
        if self.jinsi=="erkak" and self.yoshi>18:
            if self.boyii<150 and self.vazni<75:
                print(""" Piyoda askarga qabul qilindi
              Jinsi: {}
              Yoshi: {}
              Bo'yi: {}
              Vazni: {}
 """.format(self.jinsi,self.yoshi,self.boyii,self.vazni))
            else:
                print(""" Tank Qo'shiniga qabul qilindi
              Jinsi: {}
              Yoshi: {}
              Bo'yi: {}
              Vazni: {}
 """.format(self.jinsi,self.yoshi,self.boyii,self.vazni))
        else:
            print("Qabul qilinmadi")
class Armiya(Soldat):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c,d)
    def prin(self):
        super().printer()

for i in range(4):
    askar=Armiya(input("Jinsi: "), int(input("Yoshi: ")), int(input("Bo'yi: ")), int(input("Vazni:" )))
    askar.prin()
    #%%
class Uchburchak():
    def __init__(self,a,b,c,d):
        self.A=a
        self.B=b
        self.C=c
        self.D=d
    def xisob(self):
        p=(self.A+self.B+self.C)/2
        self.uch=(p*(p-self.A)*(p-self.B)*(p-self.C))**(1/2)
        self.kv=self.D**2
        if self.uch>self.kv:
            print("Kvadrat Uchburchakning ichiga sig'adi")
        else:
            print("Uchburchak Kvadratning ichiga sig'adi")
               
class Kvadrat(Uchburchak):
    def __init__(self,a,b,c,d):
        super().__init__(a, b, c, d)
    def xis(self):
        super().xisob()

burchak=Kvadrat(int(input("Uchburchak tomoni: ")),int(input("Uchburchak tomoni: ")), int(input("Uchburchak tomoni: ")), int(input("Kvadrat tomoni: ")))        
burchak.xis()   