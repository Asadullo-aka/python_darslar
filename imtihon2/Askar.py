class Askar :
    def __init__(self,a,b,c,d):
        self.jinsi=a
        self.yoshi=b
        self.boyi=c
        self.vazni=d
    def printf(self):
        if self.jinsi=='erkak' and self.yoshi>=18 and self.boyi>165 and self.vazni>65:
            print(f"<<Piyoda qoshinlariga  qabull qilindingiz>>\n Jinsi {self.jinsi}\n yoshi {self.yoshi}\n Boyi {self.boyi}\n Vazni {self.vazni}")
        elif self.jinsi=='erkak' and self.yoshi<18 and self.boyi<165 and self.vazni<65:
            print(f"<<Tank qoshinlariga  qabull qilindingiz>>\n Jinsi {self.jinsi}\n yoshi {self.yoshi}\n Boyi {self.boyi} Vazni {self.vazni}")
        else:
            print("siz bizning standartga tori kelmadingiz")
    def __str__(self):
        return "Men Askarlarni Sarallash funksyasi bn shugullanaman"
class General(Askar):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
    def printf(self):
        super().printf()
Armiya=General(input("jinsingizni kiriting\n>>"),int(input("Yoshingizni kiritng\n>>")),int(input("byingizni kiritng\n>>")),int(input("vazningizni kiritng\n>>")))
Armiya.printf()
Armiya=Askar(input("jinsingizni kiriting\n>>"),int(input("Yoshingizni kiritng\n>>")),int(input("byingizni kiritng\n>>")),int(input("vazningizni kiritng\n>>")))
Armiya.printf()    